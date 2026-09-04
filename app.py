from flask import Flask, jsonify, request, render_template
import psycopg2
import subprocess
import tempfile
import os

def get_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        port=int(os.environ.get("DB_PORT", 5432)),
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )

@app.route("/")
def home():
    return "Backend is alive!"

@app.route("/questions")
def get_questions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, difficulty FROM questions;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    result = [{"id": r[0], "title": r[1], "difficulty": r[2]} for r in rows]
    return jsonify(result)
@app.route("/question/<int:question_id>")
def get_question(question_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, description, difficulty FROM questions WHERE id = %s;",
        (question_id,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return jsonify({"error": "Question not found"}), 404
    return jsonify({"id": row[0], "title": row[1], "description": row[2], "difficulty": row[3]})

@app.route("/exam")
def exam():
    return render_template("index.html")

@app.route("/testcases/<int:question_id>")
def get_testcases(question_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, input, expected_output FROM testcases WHERE question_id = %s;",
        (question_id,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    result = [{"id": r[0], "input": r[1], "expected_output": r[2]} for r in rows]
    return jsonify(result)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    question_id = data.get("question_id")
    code = data.get("code")
    language = data.get("language")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT input, expected_output FROM testcases WHERE question_id = %s;",
        (question_id,)
    )
    testcases = cur.fetchall()
    cur.close()
    conn.close()

    if not testcases:
        return jsonify({"error": "No testcases found for this question"}), 404

    results = []
    with tempfile.TemporaryDirectory() as tmpdir:
        if language == "python":
            src_path = os.path.join(tmpdir, "solution.py")
            with open(src_path, "w") as f:
                f.write(code)
            run_cmd = ["python3", src_path]

        elif language == "c":
            src_path = os.path.join(tmpdir, "solution.c")
            binary_path = os.path.join(tmpdir, "solution")
            with open(src_path, "w") as f:
                f.write(code)
            compile_proc = subprocess.run(
                ["gcc", src_path, "-o", binary_path],
                capture_output=True, text=True, timeout=10
            )
            if compile_proc.returncode != 0:
                return jsonify({"error": "Compilation failed", "details": compile_proc.stderr}), 400
            run_cmd = [binary_path]

        elif language == "java":
            src_path = os.path.join(tmpdir, "Solution.java")
            with open(src_path, "w") as f:
                f.write(code)
            compile_proc = subprocess.run(
                ["javac", src_path],
                capture_output=True, text=True, timeout=15, cwd=tmpdir
            )
            if compile_proc.returncode != 0:
                return jsonify({"error": "Compilation failed", "details": compile_proc.stderr}), 400
            run_cmd = ["java", "-cp", tmpdir, "Solution"]

        else:
            return jsonify({"error": "Unsupported language. Use 'python', 'c', or 'java'."}), 400

        for input_data, expected_output in testcases:
            try:
                proc = subprocess.run(
                    run_cmd,
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                actual_output = proc.stdout.strip()
                passed = actual_output == expected_output.strip()
                results.append({
                    "input": input_data,
                    "expected": expected_output,
                    "actual": actual_output,
                    "passed": passed,
                    "stderr": proc.stderr.strip()
                })
            except subprocess.TimeoutExpired:
                results.append({
                    "input": input_data,
                    "expected": expected_output,
                    "actual": None,
                    "passed": False,
                    "stderr": "Time limit exceeded"
                })

    all_passed = all(r["passed"] for r in results)
    return jsonify({"all_passed": all_passed, "results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
