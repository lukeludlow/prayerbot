import random



INTRO = [
    "dear father in heaven, ",
    "oh god, the eternal father, ",
    "dear heavenly father, ",
    "heavenly father, ",
    "our father in heaven, "
]

PURPOSE = [
    "we are so blessed to be gathered here as a family. ",
    "we come together this day to pray. "
]

THANKFUL = [
    "we thank thee that we can gather here together today. ",
    "we thank thee for our many blessings. ",
    "we thank thee for all that you have given us. ",
    "we are grateful for the beautiful weather you have given us. ",
    "we thank thee for the scriptures and the guidance they give us. ",
    "we thank thee for our prophet and apostles. "
]

THANKFUL_FOOD = [
    "we thank thee for the delicious meal before us. ",
    "we are grateful for all who worked to provide us this meal. "
]

ASK = [
    "we ask that we can be blessed with your spirit. ",
    "please bless us to be kind and loving. ",
    "please bless us to carry your spirit with us. "
]

ASK_FOOD = [
    "please bless this food. ",
    "please bless this food to strengthen and nourish our bodies. ",
    "please bless this food to be nourishing to our bodies and strengthening to our minds. ",
    "please bless this food to make us healthy and strong. "
]


CLOSING = [
    "we say these things in the name of thy son, jesus christ, amen. ",
    "in the name of jesus christ, amen. ",
    "we humbly beseech these blessings, oh father, in the name of thy only begotten son, jesus christ, amen."
]


SACRAMENT_PRAYER = """
O God, the Eternal Father, we ask thee in the name of thy Son, Jesus Christ, to bless and sanctify this bread to the souls of all those who partake of it; that they may eat in remembrance of the body of thy Son, and witness unto thee, O God, the Eternal Father, that they are willing to take upon them the name of thy Son, and always remember him, and keep his commandments which he hath given them, that they may always have his Spirit to be with them. Amen. 
"""




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
    intent = request['intent']['name']

    if intent == 'BasicPrayer':
        output = random.choice(INTRO) + "".join(random.sample(THANKFUL, 2)) + "".join(random.sample(ASK, 2)) + random.choice(CLOSING)
        return build_response(output)


    elif intent == 'DinnerPrayer':
        output = INTRO + THANKFUL + "please bless the food to strengthen and nourish our bodies." + CLOSING
        return build_response(output)


    elif intent == 'RefreshmentPrayer':
        output = INTRO + THANKFUL + "please bless these doughnuts and cookies to strengthen and nourish our bodies." + CLOSING
        return build_response(output)

    elif intent == 'SacramentPrayer':
        return build_response(SACRAMENT_PRAYER)

    elif intent == "AMAZON.StopIntent":
        return on_session_ended()

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







