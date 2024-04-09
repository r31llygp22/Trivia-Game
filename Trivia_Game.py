import random

questions = {
    'General Knowledge': [
        {"Who wrote 'Romeo and Juliet'?": "Shakespeare"},
        {"What is the largest planet in our solar system?": "Jupiter"},
        {"What is the smallest planet in our solar system?": "Mercury"},
        {"What is 2+2?": "4"}
    ],
    'Science': [
        {"What is the chemical symbol for water?": "H2O"},
        {"What is chemistry the study of?": "Matter"},
        {"What is the study of earth?": "Geology"},
    ],
    'History': [
        {"In which year did WWI end?": "1918"},
        {"Who was the first President of the United States?": "George Washington"},
        {"What ancient civilization built the pyramids?": "Egyptians"},
        {"Who was the German leader of WW2?": "Hitler"},
    ],
    'Geography': [
        {"What is the capital of the Dominican Republic?": "Santo Domingo"},
        {"Where is Ecuador located?": "South America"},
        {"How many continents are there?": "7"},
        {"What is the largest Ocean?": "Pacific Ocean"},
    ],
    'Movies and Tv shows': [
        {"What is the most famous superhero franchise?": "Marvel"},
        {"In what year was the Godfather released?": "1972"},
        {"How many seasons does Breaking Bad have?": "Five Seasons"},
        {"What is the highest-rated tv show episode on IMDb and from what show does it come?": "Ozymandias from Breaking Bad"},
    ]
}

def ask_question(category):
    random_question = random.choice(questions[category])
    question_text = list(random_question.keys())[0]
    correct_answer = list(random_question.values())[0]

    questions[category].remove(random_question)

    return question_text, correct_answer

def play_game():
    score = 0
    total_questions = 0

    categories = list(questions.keys())
    random.shuffle(categories)

    for category in categories:
        print(f"\nCategory: {category}")
        question, correct_answer = ask_question(category)
        print("Question:", question)

        user_answer = input("Your answer: ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1

        total_questions += 1
        if total_questions == 10:
            break

        if not questions[category]:
            break

    print("\nGame Over!")
    print(f"Your final score is: {score}")

    if score >= 7:
        print("Congrats, you answered more than 7 questions :).")
    else:
        print("You lose, didn't answer more than 7 questions :(")

play_game()