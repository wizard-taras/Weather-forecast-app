import requests

API_KEY = '1c37254fa04635df77561dbfce714e1e'


def get_data(place, forecast_days, kind):
    url = f'https://api.openweathermap.org/data/2.5/forecast?id={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    num_of_values = 8 * forecast_days
    filtered_data = filtered_data[:num_of_values]
    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    elif kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Kerch', forecast_days=3, kind='Temperature'))
