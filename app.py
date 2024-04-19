from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)


quiz_data = {
    1: {
        'title': 'Video Games',
        'questions': [
            {
                'question_text': 'Which game introduced the character Mario?',
                'options': ['Super Mario Bros.', 'Mario Kart', 'Mario Party', 'Mario Sports Mix'],
                'correct_option': 0
            },
            {
                'question_text': 'What is the name of the protagonist in "The Legend of Zelda: Breath of the Wild"?',
                'options': ['Link', 'Samus', 'Peach', 'Yoshi'],
                'correct_option': 0
            },
            {
                'question_text': 'Which game series is known for its "Eat, Pray, Love" theme?',
                'options': ['Final Fantasy', 'The Sims', 'Mass Effect', 'Animal Crossing'],
                'correct_option': 1
            },
            {
                'question_text': 'In which game does the player control a giant robot?',
                'options': ['Mega Man', 'God of War', 'Super Smash Bros.', 'Robotron 2084'],
                'correct_option': 3
            },
            {
                'question_text': 'Which game is known for its "Everybodys Gone to the Rapture" theme?',
                'options': ['The Last of Us', 'The Witcher 3: Wild Hunt', 'Horizon Zero Dawn', 'God of War'],
                'correct_option': 0
            }
        ]
    },
    2: {
        'title': 'Python Dictionaries',
        'questions': [
            {
                'question_text': 'Which line of code correctly adds an item to the `fruits` dictionary with a key of `grapes` and a value of 15?',
                'options': [
                    'fruits[\'grapes\']',
                    'fruits[\'grapes\'] = 15',
                    'insert \'grapes\' in fruits',
                    'fruits[15] = \'grapes\''
                ],
                'correct_option': 1
            },
            {
                'question_text': 'What does the following code print?',
                'options': [
                    "['Janice', 'Emily', 'John', 'Eleanor']",
                    "['Janice', 'Emily', 'John']",
                    "['John']",
                    "['Janice', 'Emily', 'John', 'Eleanor']"
                ],
                'correct_option': 2
            },
            {
                'question_text': 'What does the following code print?',
                'options': [
                    "['Emily', 'John', 'Erik']",
                    "['Janice', 'Emily', 'John']",
                    "['Janice', 'Emily', 'John', 'Eleanor']",
                    "['Janice', 'Emily', 'John', 'Eleanor']"
                ],
                'correct_option': 0
            },
            {
                'question_text': 'What is the value of `counter` after the code is run?',
                'options': ['5', '10', '9', '11'],
                'correct_option': 2
            }
        ]
    }
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quizzes")
def quizzes():
    return render_template("quizzes.html", quizzes=quiz_data)


@app.route("/quiz/<int:quiz_id>", methods=["GET", "POST"])
def quiz(quiz_id):
    if request.method == "GET":
        return render_template("quiz.html", quiz=quiz_data[quiz_id], quiz_id=quiz_id, enumerate=enumerate)
    elif request.method == "POST":
        session["user_answers"] = request.form
        return redirect(url_for("result", quiz_id=quiz_id))


def calculate_score(questions, user_answers):
    correct_answers= 0
    for question_index, question in enumerate(questions):
        if question_index in user_answers.keys() and user_answers[question_index] == question["correct_option"]: #1. checkt ob question_indes in dictionary user answer drinne ist, 2. checkt ob gleiche zahl
            correct_answers += 1
    return correct_answers, len(questions)


@app.route("/result/<int:quiz_id>") 
def result(quiz_id):
    correct_answers, total_answers = calculate_score(quiz_data[int(quiz_id)]["questions"], session["user_answers"])
    return render_template("result.html", correct=correct_answers, total=total_answers)       


if __name__ == "__main__":
    app.run(debug=True)

