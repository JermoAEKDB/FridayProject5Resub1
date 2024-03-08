import sqlite3

connection = sqlite3.connect('FridayProj5.db')
cursor = connection.cursor()

def executeQuestions():
    cursor.execute('SELECT * FROM QuestAns')
    return cursor.fetchall()

QNA = executeQuestions()

Right = 0
Wrong = 0

print("Welcome to my Quiz Bowl!")

for row in QNA:
    question = row[1]
    answer = row[2]

    print(question)
    user_answer = input("Provide answer: ")

    if user_answer.lower() == answer.lower():
        print("Great Answer! +1 point")
        Right += 1
    else:
        print("Incorrect! The answer is:", answer)
        Wrong += 1

print("Here are your final scoring totals (Right:Wrong) -", Right, ":", Wrong)

connection.close()
