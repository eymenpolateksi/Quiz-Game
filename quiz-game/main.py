from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in range(0, len(question_data)):
    text = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

a = QuizBrain(question_bank)
a.next_question()