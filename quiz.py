
questions = [
    {
        "question": "What is 5 + 3?",
        "options": ["6", "8", "9"],
        "answer": "2"
    },
    {
        "question": "Which is a Python data type?",
        "options": ["LIST", "LOOP", "PRINT"],
        "answer": "1"
    },
    {
        "question": "Which keyword defines a function?",
        "options": ["class", "def", "return"],
        "answer": "2"
    }
]


def display_question(q):
    print("\n" + q["question"])

    for index, option in enumerate(q["options"], start=1):
        print(f"{index}. {option}")


def get_answer():
    while True:
        answer = input("Enter your answer (1, 2, or 3): ")

        if answer in ["1", "2", "3"]:
            return answer

        print("Invalid input!")


def check_answer(answer, correct_answer):
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0


def run_quiz():
    score = 0

    for q in questions:
        display_question(q)

        answer = get_answer()

        score += check_answer(answer, q["answer"])

    print(f"\nFinal score: {score}/{len(questions)}")


run_quiz()

