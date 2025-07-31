"""
Program defines function to get weather summary
"""

def summarize_weather(data: bytearray, criteria: dict):
    """
    Function processes the dict to give weather summary
    :param data: client request array
    :param criteria: defined criteria dict
    :return:
    """

    arr = []
    for key in data:
        key:dict
        for ckey, cvalue in criteria.items():
            # Check high temperature
            if cvalue["temp_max"] == "" or key["temp_max"] <= cvalue["temp_max"]:
                # Check low temperature
                if cvalue["temp_min"] == "" or key["temp_min"] >= cvalue[
                    "temp_min"]:
                    # Check weather condition
                    if cvalue["main"] == "" or key["main"] == cvalue["main"]:
                        if ckey not in arr:
                            arr.append(ckey)

    return arr
