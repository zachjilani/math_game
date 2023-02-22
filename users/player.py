import json

QUESTIONS = {}
with open('RevisedQuestions.json', 'r') as myfile:
  QUESTIONS = json.loads(myfile.read())


class Player:
  def __init__(self, number, score=0):
    self.number = number
    self.score = score
    self.questions_asked = []


  def save_player(self, question):
    self.questions_asked.append(question)

  def questions(self, input):
    state = 'start'
    out = []
    for next_question in QUESTIONS[state]['next_state']:
      if input.lower() == next_question['input'].lower():
        state = next_question['next_state']
        if 'point' in next_question['point']:
          self.score += next_question['point']
          out.append(self.score)
    # while True:
    #   out.append(QUESTIONS[state]['content'])
    #   if 'next_state' not in QUESTIONS[state]:
    #     break
    #   state = QUESTIONS[state]['next_state']

    return out
