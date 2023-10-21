from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather/<city>')
def get_weather(city):
    # Replace this with your weather data retrieval logic
    weather_data = {
        "city": city,
        "temperature": "25°C",
        "conditions": "Sunny",
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

