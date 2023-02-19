import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.logging import logger
from os.path import exists
import random
import json
import pickle
from users.player import Player

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

CORPUS = {}

with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def handle_request():
    logger.debug(request.form)

    player = None
    #look if number for player exists
    if exists(f"users/{request.form['From']}.pkl"):
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            player = pickle.load(p)
    else:
        player = Player(request.form['From'])

    sent_input = str(request.form['Body']).lower()
    if sent_input in CORPUS['input']:
        response = random.choice(CORPUS['input'][sent_input])
    else:
        CORPUS['input'][sent_input] = ['DID NOT FIND']
        with open('chatbot_corpus.json', 'w') as myfile:
            myfile.write(json.dumps(CORPUS, indent=4 ))

    message = g.sms_client.messages.create(
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])

    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(player, p)

    return json_response( status = "ok" )
