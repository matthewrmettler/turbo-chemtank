import json


def test(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def get_summary(event, context):
    summoner_name = event.get('pathParameters').get('summoner_name')

    body = {
        "message": "TODO: Summary of {}.".format(summoner_name)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response