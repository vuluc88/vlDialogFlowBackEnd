from settings import *
from dialog_flow import dialog


##
## setup the Api resource routing here
##
api.add_resource(dialog.IntentsList, '/intents')
api.add_resource(dialog.Intent, '/intents/<string:intent_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
