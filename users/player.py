import json

QUESTIONS = {}
with open('RevisedQuestions.json', 'r') as myfile:
  QUESTIONS = json.loads(myfile.read())

state = 'start'

class Player:
  def __init__(self, number, score=0):
    self.number = number
    self.score = score
    self.questions_asked = []


  def save_player(self, question):
    self.questions_asked.append(question)

  def questions(self, input):
    out = []
    for next_question in QUESTIONS[state]['next_question']:
      print(f'before state change: {state}')
      print(f'input: {input}')
      if input.lower() == next_question['input'].lower():
        state = next_question['next_question']
        print(f'after state change: {state}')
        print(f'input after: {input}')
        if 'point' in next_question['point']:
          self.score += next_question['point']
          out.append(self.score)
          break
    while True:
      out.append(QUESTIONS[state]['content'])
      if 'next_state' not in QUESTIONS[state]:
        break
      state = QUESTIONS[state]['next_question']

    return out
