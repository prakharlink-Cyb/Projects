quiz = {
    "What is the capital of India?": "Delhi",
    "What is 5 + 7?": "12",
    "Which keyword is used to define a function in Python?": "def",
    "What data type is used to store True or False values?": "bool",
    "Which symbol is used for comments in Python?": "#"
}


score = 0

for question,answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct")
        score +=1

    else:
        print(f" Wrong! The correct answer is: {answer}")
    

print(f"🎯 Your final score is: {score} / {len(quiz)}")
