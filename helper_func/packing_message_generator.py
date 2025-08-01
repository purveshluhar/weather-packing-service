"""
Helper functions to generate packing list for the trip and generate the final
message which includes weather summary and packing list.

Includes:
- generate_packing_list()
- message_generator()
"""

def generate_packing_list(weather_arr: bytearray, criteria: dict):
    """
    Generates packing list as per the given weather types and criteria.
    :param weather_arr: arr, Data containing all the weather during the trip
    :param criteria: list, Includes criteria which defines packing list for
    weather type
    :return: list, Packing items
    """

    packing_dict = {}
    for weather in weather_arr:
        packing_dict[weather] = criteria[weather]["packing-list"]

    return packing_dict


def message_generator(weather_arr: bytearray, packing_dict: dict,
                      criteria:dict):
    """
    Generates a message as per the weather and packing list during the trip.
    :param weather_arr: arr, Data containing all the weather during the trip
    :param packing_dict:
    :param criteria: list, Includes criteria which defines packing list
    for weather type
    :return: str
    """

    weather_str = ""

    if len(weather_arr) > 1:
        weather_str += "There will be"
        for index, weather in enumerate(weather_arr):
            weather_str += f" some days of {weather.lower()}"

            if index != len(weather_arr) - 1:
                weather_str += " and"
            else:
                weather_str +=  "."
    else:
        weather_str += (f"{criteria[weather_arr[0]]["message"]} "
                        f"{weather_arr[0].lower()} during your trip.")

    packing_str = "Don't forget to pack your"
    for index, (key, values) in enumerate(packing_dict.items()):
        for val_index, value in enumerate(values):
            if index == len(packing_dict) - 1 and val_index == len(values) - 1:
                packing_str += f" and {value.lower()}."
            else:
                packing_str += f" {value.lower()},"

    return weather_str + " " + packing_str
