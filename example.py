import random

dinnerOptions = [
    "Chicken",
    "Beef",
    "Pork",
    "Fish",
    "Vegetarian"
]


def lambda_handler(event, context):
    dinner = random.choice(dinnerOptions)
    response = {
            'version': '1.0',
            'response': {
                'outputSPeech': {
                    'type': 'PlainText',
                    'text': dinner,
                }
            }
        }
    return response
