import random


# --- populate arrays with prayer phrases --- #

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

REFRESHMENTS = "please bless these doughnuts and cookies and stuff to strengthen and nourish our bodies. "

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


IDEAS = [
    "ask to protect the missionaries, ",
    "ask to have the spirit in your house, ",
    "ask to be led to the right choices, ",
    "express gratitude for your blessings, ",
    "be thankful for your health and safety, ",
    "express gratitude for your loved ones, ",
    "ask how to help your loved ones, ",
    "ask how to serve more, ",
    "bless the refreshments, ",
    "ask for heavenly father's guidance, "
]

# kind of an easter egg - a rote prayer from Alma 31:15
LONG_PRAYER = (
    'Holy, holy God; we believe that thou art God, and we believe that thou art holy, and that thou wast a spirit, and that thou '
    'art a spirit, and that thou wilt be a spirit forever. Holy God, we believe that thou hast separated us from our brethren; '
    'and we do not believe in the tradition of our brethren, which was handed down to them by the childishness of their fathers; '
    'but we believe that thou hast elected us to be thy holy children; and also thou hast made it known unto us that there shall be '
    'no Christ. But thou art the same yesterday, today, and forever; and thou hast elected us that we shall be saved, whilst all '
    'around us are elected to be cast by thy wrath down to hell; for the which holiness, O God, we thank thee; and we also thank '
    'thee that thou hast elected us, that we may not be led away after the foolish traditions of our brethren, which doth bind them '
    'down to a belief of Christ, which doth lead their hearts to wander far from thee, our God. And again we thank thee, O God, that '
    'we are a chosen and a holy people. Amen. '
)


# --- entry point --- #

def lambda_handler (event, context):

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])

    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])

    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended()



# --- response handlers --- #

def on_intent (request, session):

    intent = request['intent']['name']

    if intent == 'BasicPrayer':
        output = random.choice(INTRO) + "".join(random.sample(THANKFUL, 2)) + "".join(random.sample(ASK, 2)) + random.choice(CLOSING)
        return build_response(output)

    elif intent == 'DinnerPrayer':
        output = random.choice(INTRO) + random.choice(THANKFUL) + random.choice(THANKFUL_FOOD) + random.choice(ASK) + random.choice(ASK_FOOD) + random.choice(CLOSING)
        return build_response(output)

    elif intent == 'RefreshmentPrayer':
        output = random.choice(INTRO) + REFRESHMENTS + random.choice(CLOSING)
        return build_response(output)

    elif intent == 'PrayerIdeas':
        output = "You could " + "or ".join(random.sample(IDEAS, 3))
        return build_response(output)

    elif intent == 'LongPrayer':
        return build_response(LONG_PRAYER)

    elif intent == "AMAZON.StopIntent":
        return on_session_ended()

    else:
        return build_response('error, unknown intent')


def on_session_ended():
    output = "amen. hallelujah."

    return build_response(output)


# --- build simple json response --- #

def build_response(output):

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






