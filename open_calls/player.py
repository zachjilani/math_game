import json

QUESTIONS = {}
with open('Questions.json', 'r') as myfile:
  QUESTIONS = json.loads(myfile.read())


class Player:
  def __init__(self, number, score):
    self.number = number
    self.score = score
    self.questions_asked = []


  def load_questions():
    return True


  def save_player(self, question):
    self.questions_asked.append(question)

