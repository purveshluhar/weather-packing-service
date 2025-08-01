"""
Main function to run the weather-packing microservice

Includes:
- run_service()
"""

import json
from dotenv import load_dotenv
import os
from helper_func.packing_message_generator import generate_packing_list, message_generator
from helper_func.weather_summary import summarize_weather
from helper_func.socket_handler import (send_message_str, setup_socket_server,
                                        recv_message_json)
from helper_func.check_data import check_data

def run_service():
    """
    Main function to run the service
    :return:
    """

    # Load the PORT from .env
    load_dotenv()
    port = os.getenv("PORT")

    # Set up the socket
    socket = setup_socket_server(port)

    while True:
        # Request data from client
        recv_data = recv_message_json(socket)

        is_valid, message = check_data(recv_data)

        # If not valid data type
        if not is_valid:
            send_message_str(socket, message)
            continue

        # Load the criteria_data JSON file
        with open("criteria.json", "r") as fd:
            criteria_data = json.load(fd)

        # Generate the weather summary
        weather_list = summarize_weather(recv_data, criteria_data)

        # Generate the packing list
        packing_list = generate_packing_list(weather_list, criteria_data)

        # Generate the message
        message = message_generator(weather_list, packing_list, criteria_data)

        # Send the message to the client
        send_message_str(socket, message)

if __name__ == "__main__":
    run_service()
