import random



INTRO = """
dear father in heaven
"""

THANKFUL = """
we thank thee that we can gather here together today.
"""


ASK = """
we ask that we can be blessed with your spirit.
"""

CLOSING = """
we say these things in the name of thy son, jesus christ, amen.
"""




# --- entry point --- 

def lambda_handler (event, context):

    return build_response();

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])

    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])

    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended()



# --- response handlers ---

def on_intent (request, session):
    #called on intent

    intent = request['intent']
    intent_name = request['intent']['name']




    return #TODO

def build_response (output):
    # build simple json response

    output = INTRO + THANKFUL + ASK + CLOSING

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            }
        }
    }
    return response;


def on_session_ended():
    output = "amen. hallelujah."

    return build_response(output)







