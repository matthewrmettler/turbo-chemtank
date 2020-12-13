import json

from cassiopeia import Summoner

from helper.matches import match_summary
from helper.champs import mastery_summary


def print_summoner(name: str, region: str):
    summoner = Summoner(name=name, region=region)
    print("Name:", summoner.name)
    print("ID:", summoner.id)
    print("Account ID:", summoner.account_id)
    print("Level:", summoner.level)
    print("Revision date:", summoner.revision_date)



def test(event, context):
    print_summoner("Matty The Sloth", "NA")


def get_summary(event, context):
    try:
        summoner_name = event.get('pathParameters').get('summoner_name')
        summoner_region = event.get('pathParameters').get('summoner_region') or 'NA'

        summoner = Summoner(name=summoner_name, region=summoner_region)

        body = {
            "account_id": summoner.account_id,
            "level": summoner.level,
            "matches": match_summary(summoner),
            "mastery": mastery_summary(summoner)
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }


    except Exception as e:
        error_msg = "Unexpected error: %s" % str(e)
        response = {
            "statusCode": 500,
            "body": json.dumps(error_msg)
        }

    return response

if __name__ == "__main__":
    print_summoner("Matty The Sloth", "NA")