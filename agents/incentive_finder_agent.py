from external.incentive_api import fetch_incentives


def find_government_incentives(location):
    return fetch_incentives(location)
