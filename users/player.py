import json

QUESTIONS = {}
with open('RevisedQuestions.json', 'r') as myfile:
  QUESTIONS = json.loads(myfile.read())


class Player:
  def __init__(self, number, score=0):
    self.number = number
    self.score = score
    self.questions_asked = []
    self.state = 'start'

  def questions(self, input):
    input = ''.join(input.split())
    out = []
    for next_question in QUESTIONS[self.state]['next_question']:
      if input.lower() == next_question['input'].lower():
        self.state = next_question['next_question']
        if 'point' in next_question['point']:
          self.score += next_question['point']
          out.append(self.score)
          break
    while True:
      out.append(QUESTIONS[self.state]['content'])
      if 'next_state' not in QUESTIONS[self.state]:
        print('in if statement')
        break
      self.state = QUESTIONS[self.state]['next_question']

    return out
