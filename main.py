import random



INTRO = [
    "dear father in heaven, ",
    "oh god, the eternal father, ",
    "dear heavenly father, ",
    "heavenly father, "
]

THANKFUL = [
    "we thank thee that we can gather here together today. ",
    "we thank thee for our many blessings. ",
    "we thank thee for all that you have given us. ",
    "we are grateful for the beautiful weather you have given us. "
]


ASK = [
    "we ask that we can be blessed with your spirit. ",
    "please bless us to be kind and loving. ",
    "please bless us to carry your spirit with us. "
]


CLOSING = [
    "we say these things in the name of thy son, jesus christ, amen. ",
    "in the name of jesus christ, amen. "
]




# --- entry point --- 

def lambda_handler (event, context):

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])

    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])

    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended()



# --- response handlers ---

def on_intent (request, session):
    #called on intent

    #intent = request['intent']
    intent_name = request['intent']['name']

    if intent_name == 'BasicPrayer':

        output = random.choice(INTRO) + "".join(random.sample(THANKFUL, 2)) + "".join(random.sample(ASK, 2)) + random.choice(CLOSING)
        return build_response(output)


    elif intent_name == 'DinnerPrayer':
        output = INTRO + THANKFUL + "please bless the food to strengthen and nourish our bodies." + CLOSING
        return build_response(output)

    elif intent_name == 'RefreshmentPrayer':
        output = INTRO + THANKFUL + "please bless these doughnuts and cookies to strengthen and nourish our bodies." + CLOSING
        return build_response(output)

    else:
        return build_response('error, unknown intent')


def build_response(output):
    # build simple json response

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







