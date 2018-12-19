from flask import jsonify, request
from flask_restful import reqparse, abort, Resource
from settings import DIALOGFLOW_API

import subprocess
import requests

parser = reqparse.RequestParser()
#output = subprocess.run("gcloud auth application-default print-access-token", shell=True, stdout=subprocess.PIPE, universal_newlines=False)
output = subprocess.check_output("gcloud auth application-default print-access-token", shell=True)
gcloud_token = output.decode('utf-8').strip()
headers = {'Authorization': 'Bearer %s' % gcloud_token}

class Webhook(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        return {'msg': 'success'}, 201

class IntentsList(Resource):
    def get(self):
        #call dialogflow api to get all intents
        r = requests.get(DIALOGFLOW_API['DF_API_GET_LIST_INTENTS'], headers=headers)
        return r.json(), r.status_code

    def post(self):
        json_data = request.get_json(force=True)
        payload = json_data
        #call dialogflow api to create intent
        r = requests.post(DIALOGFLOW_API['DF_API_CREATE_INTENT'], headers=headers, json=payload)
        return r.json(), r.status_code

class Intent(Resource):
    def get(self, intent_id):
        #call dialogflow api to get intent info
        r = requests.get(DIALOGFLOW_API['DF_API_GET_INTENT'] + intent_id, headers=headers)
        return r.json(), r.status_code
