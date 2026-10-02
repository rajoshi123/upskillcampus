#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("===================================")
print("       WELCOME TO QUIZ GAME")
print("===================================")

score = 0

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language are we using to create this quiz?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which of these is a Python data type?",
        "options": ["A. list", "B. table", "C. record", "D. column"],
        "answer": "A"
    },
    {
        "question": "What is the output of 10 // 3 in Python?",
        "options": ["A. 3", "B. 3.33", "C. 4", "D. 30"],
        "answer": "A"
    }
]

for i, q in enumerate(questions, start=1):
    print("\nQuestion", i)
    print(q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", q["answer"])

print("\n===================================")
print("           QUIZ COMPLETED")
print("===================================")

percentage = (score / len(questions)) * 100

print("Your score:", score, "/", len(questions))
print("Percentage:", percentage, "%")

if percentage == 100:
    print("Excellent performance!")
elif percentage >= 60:
    print("Good job!")
else:
    print("Keep practicing!")

print("Thank you for playing!")


# In[ ]:




