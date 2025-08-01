"""
Helper function to check data requested from the client

Includes:
- check_data()
"""

def check_data(data:bytearray):
    """
    Checks the data requested from the client and returns if the data is
    valid or invalid with the invalid response message.
    :param data: arr, Data requested from the client
    :return: bool, str
    """

    req_key = ['temp_max', 'temp_min', 'main']
    message = ""

    for value in data:
        value:dict
        # Check the received data
        if len(value) != len(req_key):
            message += "Invalid Data, Try again!"
            return False, message
        else:
            for key, cvalue in value.items():
                if key not in req_key:
                    message = "Invalid Keys, Try again!"
                    return False, message
                if key == 'temp_max' or key == 'temp_min':
                    if not isinstance(cvalue, (int, float)):
                        message = "Invalid Values, Try again!"
                        return False, message
                elif key == 'main':
                    if not isinstance(cvalue, str):
                        message = "Invalid Values, Try again!"
                        return False, message

    return True, message
