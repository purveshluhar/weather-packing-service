# Weather Packing Microservice
The microservice will respond with a weather summary and provide packing recommendations based on the trip's weather conditions received from the main program.
***
## Requesting Data
***
To request data, send a list request using ZeroMQ communication pipeline 
with the following format:
### Request Format
<pre>
```[
    {'temp_max': 80, 'temp_min': 61, 'main': "Clear"}, 
    {'temp_max': 80, 'temp_min': 61, 'main': "Drizzle"}
]```
</pre>

- `"temp_max` : Max temperature of the day
- `"temp_min` : Min temperature of the day
- `"main` : Weather condition of the day
- `{}`: Above required parameters for every day of the duration of the trip.
#### Example Code
<pre>
```import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5600")

weather_data = [
    {'temp_max': 80, 'temp_min': 61, 'main': "Clear"},
    {'temp_max': 80, 'temp_min': 61, 'main': "Drizzle"}
]

socket.send_json(weather_data)```
</pre>
***
## Receiving Data
The response from the microservice will be in string format containing 
weather summary and packing list for the duration of the trip or an invalid 
message.
### Response Format
#### Valid Example
<pre>
```"There will be some days of hot and some days of drizzle. Don't forget to 
pack your sunscreen, sun hat, sandals, sunglasses, rain jacket, umbrella, and 
rain boots."```
</pre>
#### Invalid Example
<pre>
```"Received Invalid Data!"```
</pre>
#### Example Code
<pre>
```import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5600")

weather_data = [
    {'temp_max': 80, 'temp_min': 61, 'main': "Clear"},
    {'temp_max': 80, 'temp_min': 61, 'main': "Drizzle"}
]

socket.send_json(weather_data)

message = socket.recv()```
</pre>
***
## Setup Instructions
### 1. Clone the Repo
<pre>
```git clone https://github.com/purveshluhar/weather-packing-service.git
cd weather-packing-service```
</pre>
### 2. Create a .env file
<pre>
```PORT_SERVICE=5600```
</pre>
- Default port: 5600
- Configure the .env file to change port
### 3. Install dependencies
<pre>
```pip install python-dotenv```
</pre>
### 4. Run Microservice in Background
<pre>
```python3 main.py &```
</pre>