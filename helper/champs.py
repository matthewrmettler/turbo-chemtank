from cassiopeia import Summoner


def mastery_summary(summoner):
    good_with = summoner.champion_masteries.filter(lambda cm: cm.level >= 6)
    return [cm.champion.name for cm in good_with][:10]