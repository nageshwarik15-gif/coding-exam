\# 🧑‍💻 Online Coding Exam Platform



A web-based coding examination platform designed to help students practice programming, attempt timed coding exams, and receive automated feedback on their code submissions.



\## 📌 Overview



The \*\*Online Coding Exam Platform\*\* is a full-stack web application that provides an interactive environment for conducting programming examinations.



Students can explore coding questions, write programs in supported programming languages, submit their solutions, and view their results through a user-friendly examination interface.



The platform uses a Python Flask backend, PostgreSQL database, and Docker for containerized development and deployment.



\## ✨ Key Features



\* ⏱️ \*\*Timed Coding Exams\*\* — 30-minute examination timer.

\* 📝 \*\*Programming Questions\*\* — Coding problems with descriptions and difficulty levels.

\* 💻 \*\*Multi-Language Support\*\* — Write solutions in Python, C, and Java.

\* ▶️ \*\*Automated Code Evaluation\*\* — Execute submitted programs against test cases.

\* 📊 \*\*Exam Results\*\* — View scores, percentages, and passed or failed questions.

\* 🔄 \*\*Question Navigation\*\* — Move between questions using Previous and Next controls.

\* 💾 \*\*Code Persistence\*\* — Save code for individual questions during an exam.

\* 🗄️ \*\*Database Integration\*\* — Store coding questions and test cases in PostgreSQL.

\* 🐳 \*\*Docker Support\*\* — Run the application using Docker and Docker Compose.



\## 🛠️ Tech Stack



| Technology        | Purpose                       |

| ----------------- | ----------------------------- |

| Python            | Backend programming           |

| Flask             | Web application framework     |

| HTML              | Page structure                |

| CSS               | User interface styling        |

| JavaScript        | Frontend interactions         |

| PostgreSQL        | Database management           |

| Docker            | Containerization              |

| Docker Compose    | Multi-container orchestration |

| C / Java / Python | Supported coding languages    |



\## 🏗️ Architecture



```text

┌─────────────────────────────┐

│       Student Browser       │

│      HTML / CSS / JS        │

└──────────────┬──────────────┘

&#x20;              │ HTTP Requests

&#x20;              ▼

┌─────────────────────────────┐

│       Flask Backend         │

│        app.py               │

│                             │

│  • Question Management      │

│  • Code Submission          │

│  • Code Execution           │

│  • Result Processing        │

└──────────────┬──────────────┘

&#x20;              │ Database Queries

&#x20;              ▼

┌─────────────────────────────┐

│       PostgreSQL            │

│                             │

│  • Questions                │

│  • Test Cases               │

└─────────────────────────────┘



&#x20;      Docker Environment

```



\## 📂 Project Structure



```text

coding-exam/

│

├── app.py                  # Flask application

├── templates/              # HTML templates

├── static/                 # CSS and JavaScript assets

├── Dockerfile              # Backend container configuration

├── docker-compose.yml      # Application and database services

├── requirements.txt        # Python dependencies

├── README.md               # Project documentation

└── .gitignore              # Ignored files

```



> The structure above is an illustrative layout. Update it to match the actual folders in your repository.



\## 🚀 Getting Started



\### Prerequisites



Install the following tools:



\* \[Docker Desktop](https://www.docker.com/products/docker-desktop/)

\* \[Git](https://git-scm.com/)



\### 1. Clone the repository



```bash

git clone https://github.com/nageshwarik15-gif/coding-exam.git

```



\### 2. Open the project directory



```bash

cd coding-exam

```



\### 3. Build and start the application



```bash

docker compose up --build

```



\### 4. Open the application



Visit:



```text

http://localhost:5000

```



> Make sure Docker Desktop is running before starting the application.



\### 5. Stop the application



```bash

docker compose down

```



\## 🗄️ Database



The application uses PostgreSQL to manage coding questions and test cases.



Example entities include:



\* `questions` — Stores question titles, descriptions, and difficulty levels.

\* `testcases` — Stores test inputs and expected outputs for coding problems.



\## 🧪 Code Evaluation



The platform supports programming submissions in:



\* Python

\* C

\* Java



Submitted programs are evaluated against test cases, and the platform calculates the corresponding results.



\*\*Security note:\*\* Running arbitrary student code requires proper isolation and resource limits. This project should not be exposed publicly as a code-execution service without additional sandboxing and security controls.



\## 🎯 Project Objectives



\* Provide an interactive online coding examination experience.

\* Automate programming assessment using test cases.

\* Reduce manual evaluation effort.

\* Practice real-world full-stack development.

\* Learn containerized application deployment.



\## 🔮 Future Enhancements



\* User registration and authentication.

\* Admin dashboard for managing questions.

\* Leaderboards and performance analytics.

\* More programming language support.

\* Stronger code-execution sandboxing.

\* Exam history and student progress tracking.



\## 👩‍💻 Author



\*\*Shivanshi\*\*



GitHub: \[nageshwarik15-gif](https://github.com/nageshwarik15-gif)



\## 📄 License



This project does not currently specify a license.



\---



⭐ If you find this project useful, consider giving it a star on GitHub.



