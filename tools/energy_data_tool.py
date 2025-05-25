from external.energy_api import fetch_energy_data


def get_local_energy_data(location, power_type="THERMAL"):
    return fetch_energy_data(location, power_type)
