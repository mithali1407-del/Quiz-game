import random
import time

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. def", "B. function", "C. function", "D. define"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question" : "Who is the President of India?",
        "options" : ["A. Droupadi Murmu", "B. Narendra Modi", "C. Amit Shah", "D. Rajnath Singh"],
        "answer" : "A"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

random.shuffle(questions)

score = 0

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)

    start = time.time()
    answer = input("Your answer (A/B/C/D): ").upper()
    end = time.time()

    if end - start > 10:
        print("⏰ Time's up!")
        continue

    if answer == q["answer"]:
        print("YAEYYY! u got it✅")
        score += 1
    else:
        print("Nope its wrong!❌")

print("\nYour Score:", score)

with open("score.txt", "a") as file:
    file.write(f"Score: {score}\n")
