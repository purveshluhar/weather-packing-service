"""
Program defines function to get packing list and generate the final message
"""

def generate_packing_list(weather_arr: bytearray, criteria: dict):
    """
    Function to generate packing list
    :param weather_arr:
    :param criteria:
    :return:
    """

    packing_dict = {}
    for weather in weather_arr:
        packing_dict[weather] = criteria[weather]["packing-list"]

    return packing_dict


def message_generator(weather_arr: bytearray, packing_dict: dict):
    """
    Function to generate the message summary and packing list in string format
    :param weather_arr:
    :param packing_dict:
    :return:
    """

    weather_str = ""
    if len(weather_arr) > 1:
        weather_str += "There will be"
        for index, weather in enumerate(weather_arr):
            weather_str += f" some days of {weather}"

            if index != len(weather_arr) - 1:
                weather_str += " and"
            else:
                weather_str +=  "."
    else:
        if weather_arr[0] == "rain" or weather_arr[0] == "drizzle":
            weather_str += "It's going to rain during your trip."
        elif weather_arr[0] == "snow":
            weather_str += "Be prepared fro snow."
        else:
            weather_str += (f"It's going to be {weather_arr[0]} during"
                                   f" your trip.")

    packing_str = "Don't forget to pack your"
    for index, (key, values) in enumerate(packing_dict.items()):
        for val_index, value in enumerate(values):
            if index == len(packing_dict) - 1 and val_index == len(values) - 1:
                packing_str += f" and {value}."
            else:
                packing_str += f" {value},"

    return weather_str + " " + packing_str
