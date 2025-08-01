"""
Helper function to process the data requested from the client and summarize
the weather during the trip

Includes:
- summarize_weather()
"""

def summarize_weather(data: bytearray, criteria: dict):
    """
    Processes the given weather data from the client during the trip and
    summarizes it according to the criteria defined.
    :param data: arr, Data requested from the client
    :param criteria: list, Includes criteria which defines packing list for
    weather type
    :return: arr, Contains all weather defined per criteria
    """

    arr = []
    for value in data:
        value:dict
        for ckey, cvalue in criteria.items():
            # Check high temperature
            if cvalue["temp_max"] == "" or value["temp_max"] < cvalue["temp_max"]:
                # Check low temperature
                if cvalue["temp_min"] == "" or value["temp_min"] > cvalue[
                    "temp_min"]:
                    # Check weather condition
                    if cvalue["main"] == "" or value["main"] == cvalue["main"]:
                        if ckey not in arr:
                            arr.append(ckey)

    return arr

