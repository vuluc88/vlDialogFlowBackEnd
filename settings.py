from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

AGENT_NAME = '37e03b6b-4659-4e98-b782-f92b7bb28bfa'
DF_API_DOMAIN = 'https://dialogflow.googleapis.com'
DF_API_VERSION = 'v2'
DF_API_PROJECT_ID = 'newagent-2948d'

DIALOGFLOW_API = {
    'DF_API_GET_LIST_INTENTS' : '/'.join([DF_API_DOMAIN, DF_API_VERSION, 'projects', DF_API_PROJECT_ID, 'agent', 'intents']),
    'DF_API_GET_INTENT' : '/'.join([DF_API_DOMAIN, DF_API_VERSION, 'projects', DF_API_PROJECT_ID, 'agent', 'intents/']),
    'DF_API_CREATE_INTENT' : '/'.join([DF_API_DOMAIN, DF_API_VERSION, 'projects', DF_API_PROJECT_ID, 'agent', 'intents']),
}
