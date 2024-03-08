# FridayProject5Resub1
This repository contains the contents for my Friday Project 5 submission.
Database Connection:
Connects to the SQLite database named 'FridayProj5.db'.
Uses the 'QuestAns' table for storing questions and answers.

Question Execution:
Retrieves all rows from the 'QuestAns' table.
Iterates through each question-answer pair.

Game Loop:
Presents each question to the user.
Collects user input as answers.

Scoring:
Compares user answers (case-insensitive) with correct answers.
Updates 'Right' and 'Wrong' counters accordingly.

Results Display:
Prints individual question results.
Displays the final scoring totals (Right:Wrong).

Connection Closure:
Closes the SQLite connection after completing the quiz.

Example Usage:
Execute the script to play the Quiz Bowl game.

Note:
Ensure 'FridayProj5.db' exists with the required schema.