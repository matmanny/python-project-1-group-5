# This part of the code defines the questions and answers for the quiz
questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What programming language are we using?", "answer": "python"},
    {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
    {"question": "How many continents are there on Earth?", "answer": "7"}
]

score = 0
wrong_answers = []

# This part of the code asks the questions
for q in questions:
    user_answer = input(q["question"] + " ").lower()

    if user_answer == q["answer"]:
        score += 1
    else:
        wrong_answers.append((q["question"], q["answer"]))

# This part of the code displays results
print("\nQuiz Finished!")
print("Your score:", score, "/", len(questions))

# This part of the code shows correct answers for wrong questions
if wrong_answers:
    print("\nQuestions you got wrong:")
    for question, correct in wrong_answers:
        print("Question:", question)
        print("Correct answer:", correct)
        print()
else:
    print("Great job! You got all questions correct.")