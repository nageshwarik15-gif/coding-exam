-- Create the questions table
CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    difficulty VARCHAR(50) NOT NULL
);

-- Create the testcases table
CREATE TABLE IF NOT EXISTS testcases (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    input TEXT NOT NULL,
    expected_output TEXT NOT NULL
);

-- Insert 10 coding questions
INSERT INTO questions (id, title, description, difficulty) VALUES

(1, 'Two Sum',
'Given an array of integers and a target value, find the indices of two numbers whose sum equals the target. Print the two indices separated by a space.',
'Hard'),

(2, 'Longest Substring Without Repeating Characters',
'Given a string, find the length of the longest substring that contains no repeated characters.',
'Hard'),

(3, 'Merge Overlapping Intervals',
'Given a list of intervals, merge all overlapping intervals. The first line contains the number of intervals. Print the merged intervals in sorted order.',
'Hard'),

(4, 'Maximum Subarray Sum',
'Given an array of integers, find the maximum possible sum of a contiguous subarray.',
'Medium'),

(5, 'Detect a Cycle in a Linked List',
'Given a directed graph, determine whether it contains a cycle. The first line contains the number of vertices and edges, followed by the edges. Print YES if a cycle exists; otherwise, print NO.',
'Hard'),

(6, 'Coin Change',
'Given coin denominations and a target amount, find the minimum number of coins required to make the target amount. Print -1 if it is impossible.',
'Hard'),

(7, 'Longest Increasing Subsequence',
'Given an array of integers, find the length of the longest strictly increasing subsequence.',
'Hard'),

(8, 'Minimum Path Sum',
'Given a grid of positive integers, find the minimum sum of a path from the top-left corner to the bottom-right corner. You may move only right or down.',
'Hard'),

(9, 'Binary Search Tree Validation',
'Given a binary tree in level-order format, determine whether it is a valid binary search tree. Use -1 to represent a missing node. Print TRUE or FALSE.',
'Hard'),

(10, 'Dijkstra Shortest Path',
'Given a weighted directed graph, find the shortest distance from a source vertex to a destination vertex. Print the shortest distance.',
'Hard')

ON CONFLICT (id) DO NOTHING;

-- Reset the sequence after inserting fixed IDs
SELECT setval(
    pg_get_serial_sequence('questions', 'id'),
    COALESCE((SELECT MAX(id) FROM questions), 1),
    true
);

-- Insert test cases
INSERT INTO testcases (question_id, input, expected_output) VALUES

(1, '2 7 11 15
9', '0 1'),

(1, '3 2 4
6', '1 2'),

(2, 'abcabcbb', '3'),

(2, 'bbbbb', '1'),

(3, '4
1 3
2 6
8 10
9 12', '1 6
8 12'),

(4, '9
-2 1 -3 4 -1 2 1 -5 4', '6'),

(5, '4 4
0 1
1 2
2 3
3 1', 'YES'),

(5, '4 3
0 1
1 2
2 3', 'NO'),

(6, '3
1 2 5
11', '3'),

(6, '2
2 4
3', '-1'),

(7, '8
10 9 2 5 3 7 101 18', '4'),

(8, '3 3
1 3 1
1 5 1
4 2 1', '7'),

(9, '7
5 3 7 2 4 6 8', 'TRUE'),

(9, '3
5 1 4', 'FALSE'),

(10, '5 6
0 1 4
0 2 1
2 1 2
1 3 1
2 3 5
3 4 3
0 4', '7');

-- Verify the inserted data
SELECT * FROM questions;
SELECT * FROM testcases;