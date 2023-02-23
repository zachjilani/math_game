import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.logging import logger
from os.path import exists
import random
import json
import pickle
from users.player import Player

response = 'space'
yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

def handle_request():

    player = None
    #look if number for player exists
    if exists(f"users/{request.form['From']}.pkl"):
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            player = pickle.load(p)
    else:
        player = Player(request.form['From'])
    output = player.questions(request.form['Body'])
    for msg in output:
        message = g.sms_client.messages.create(
            body = msg,
            from_ = yml_configs['twillio']['phone_number'],
            to = request.form["From"]
				)
        print(message)

    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(player, p)

    return json_response( status = "ok" )
