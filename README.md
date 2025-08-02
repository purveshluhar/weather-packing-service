# Weather Packing Microservice
The microservice will respond with a weather summary and provide packing recommendations based on the trip's weather conditions received from the main program.

## Requesting Data

To request data, send a list request using ZeroMQ communication pipeline 
with the following format:
### Request Format
```
[
    {'temp_max': 80, 'temp_min': 61, 'main': "Clear"}, 
    {'temp_max': 80, 'temp_min': 61, 'main': "Drizzle"}
]
```

- `"temp_max` : Max temperature of the day (°F or °C)
- `"temp_min` : Min temperature of the day (°F or °C)
- `"main` : Weather condition of the day (e.g., "Clear", "Rain", "Snow", 
  "Drizzle", "Clouds")
- The request is a list of daily weather objects, for each day of the trip.
#### Example Code
```
import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5600")

weather_data = [
    {'temp_max': 80, 'temp_min': 61, 'main': "Clear"},
    {'temp_max': 80, 'temp_min': 61, 'main': "Drizzle"}
]

socket.send_json(weather_data)
```

## Receiving Data
The response from the microservice will be in string format containing 
weather summary and packing list for the duration of the trip or an invalid 
message.
### Response Format
#### Example - Valid Request Data
```
"There will be some days of hot and some days of drizzle. Don't forget to 
pack your sunscreen, sun hat, sandals, sunglasses, rain jacket, umbrella, and 
rain boots."
```
#### Example - Invalid Request Data
```
"Received Invalid Data!"
```
#### Example Code
```
import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5600")

weather_data = [
    {'temp_max': 80, 'temp_min': 61, 'main': "Clear"},
    {'temp_max': 80, 'temp_min': 61, 'main': "Drizzle"}
]

socket.send_json(weather_data)

message = socket.recv()
```

## Setup Instructions
### 1. Clone the Repo
```
git clone https://github.com/purveshluhar/weather-packing-service.git
cd weather-packing-service
```
### 2. Create a .env file
```
PORT_SERVICE=5600
```
- Default port: 5600
- Configure the .env file to change port
### 3. Install dependencies
```
pip install python-dotenv
```
### 4. Optional: Update criteria.json
If you need to modify or extend the weather-based packing logic, you can update 
the criteria.json file.
This file defines the matching criteria for different weather types and 
what packing recommendations to generate.

- `"temp_max"`: Maximum temperature threshold for the weather type 
- `"temp_min"`: Minimum temperature threshold for the weather type
- `"main"`: Expected weather condition (e.g., "Clear", "Rain", "Snow", 
  "Drizzle", "Clouds")
- `"packing-list"`: A list of recommended items to pack for this weather type
- `"message"`: A custom message that will be sent to the client for this 
weather type
### 5. Run Microservice in Background
```
python3 main.py &
```
### 6. To run tests
```
python3 -m tests.test_client
```