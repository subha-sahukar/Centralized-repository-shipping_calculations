import csv
import random

def load_questions(filename):
    questions = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions[row['question']] = row['answer']
    return questions

def run_quiz(questions):
    score = 0
    question_keys = list(questions.keys())
    random.shuffle(question_keys)  # Shuffle questions for variety
    
    for question in question_keys:
        answer = input(f"{question} ")
        if answer.strip().lower() == questions[question].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {questions[question]}.")

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    questions = load_questions('questions.csv')
    run_quiz(questions)
