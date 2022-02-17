from question_model import Question
from data import QuestionData
from quiz_brain import QuizBrain
from ui import GUI

question_bank = []
for question in QuestionData().get_question():
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_interface=GUI(quiz)



