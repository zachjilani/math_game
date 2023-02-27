import json

QUESTIONS = {}
with open('RevisedQuestions.json', 'r') as myfile:
  QUESTIONS = json.loads(myfile.read())


class Player:
  def __init__(self, number, score=0):
    self.number = number
    self.score = score
    self.state = 'start'

  def questions(self, input):
    input = ''.join(input.split())
    print(f'input before loop: {input} state before loop: {self.state}')
    out = []
    for next_question in QUESTIONS[self.state]['next_question']:
      print(f'input after loop: {input} state after loop: {self.state}')
      if input.lower() == next_question['input'].lower():
        print(f'in if, input matches.{input} state: {self.state}')
        self.state = next_question['next_question']
        if 'point' in next_question:
          self.score += int(next_question['point'])
          out.append(f'Score: {self.score}')
        break
      if input.lower() != next_question['input'].lower() and input.lower() != 'start':
        self.score -= int(next_question['point'])
        out.append(f'Incorrect! Score: {self.score}')
    while True:
      out.append(QUESTIONS[self.state]['content'])
      print(self.state)
      if 'next_question' not in QUESTIONS[self.state] or type(QUESTIONS[self.state]['next_question'] != str):
        break
      self.state = QUESTIONS[self.state]['next_question']

    return out
