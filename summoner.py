import json

import cassiopeia as cass
from cassiopeia import Summoner


def print_summoner(name: str, region: str):
    summoner = Summoner(name=name, region=region)
    print("Name:", summoner.name)
    print("ID:", summoner.id)
    print("Account ID:", summoner.account_id)
    print("Level:", summoner.level)
    print("Revision date:", summoner.revision_date)
    print("Profile icon ID:", summoner.profile_icon.id)
    print("Profile icon name:", summoner.profile_icon.name)


def test(event, context):
    print_summoner("Matty The Sloth", "NA")


def get_summary(event, context):
    summoner_name = event.get('pathParameters').get('summoner_name')
    summoner_region = event.get('pathParameters').get('summoner_region') or 'NA'

    summoner = Summoner(name=summoner_name, region=summoner_region)

    body = {
        "account_id": summoner.account_id,
        "level": summoner.level
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


if __name__ == "__main__":
    print_summoner("Matty The Sloth", "NA")