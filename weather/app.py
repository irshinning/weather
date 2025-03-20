from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # 获取天气数据
    weather_data = get_weather_data()
    return render_template('index.html', weather=weather_data)

def get_weather_data(city: str):
    # 使用天气 API 获取数据，例如 OpenWeatherMap
    api_key = '575d0052c583213cf70e3eb6c88c0c94'  # 替换为你的 API 密钥
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)