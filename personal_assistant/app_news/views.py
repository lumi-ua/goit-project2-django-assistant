from datetime import datetime
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import environ
env = environ.Env()

def main(request):
    return render(request, 'app_news/index.html')


@login_required
def get_news(request):
    news = []
    base_url = "https://www.pravda.com.ua/news/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class="container_sub_news_list_wrapper mode1"] div[class="article_news_list"]')

    for el in content:
        result = {}
        time_element = el.find('div', {'class': 'article_time'})
        title_element = el.find('div', {'class': 'article_header'})

        # Перевірка наявності елементів
        if time_element and title_element:
            result['time'] = time_element.text
            result['title'] = title_element.text
            news.append(result)

    return render(request, 'app_news/scrape_news.html', {'news': news})


@login_required
def get_sport_news(request):
    sport_news = []
    base_url = "https://sport.ua/uk/uk"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', class_='news-items').find_all('div', class_='item')
    # print(content)
    for el in content:
        result = {}
        result['time'] = el.find('span', class_='item-date').text.strip()
        result['sport'] = el.find('span', class_='item-sport').text.casefold()
        result['news'] = el.find('div', {'class': 'item-title'}).text.strip()
        sport_news.append(result)
        # print(sport_news)
    return render(request, 'app_news/scrape_news_sport.html', {'sport_news': sport_news})


@login_required
def get_currency(request):
    currency = []
    date_now = datetime.now().strftime('%Y-%m-%d')
    base_url = 'https://minfin.com.ua/ua/currency/banks/usd/'
    response = requests.get(base_url + date_now + '/')
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('tbody', class_='list').find_all('tr')
    # print(content)
    for el in content:
        result = {}
        result['bank'] = el.find('a', {'class': 'mfm-black-link'}).text.strip()
        result['buy'] = el.find('td', {'class': 'responsive-hide mfm-text-right mfm-pr0'}).text.strip()
        if len(result['buy']) == 0:
            result['buy'] = '0.000'
        result['sale'] = el.find('td', {'class': 'responsive-hide mfm-text-left mfm-pl0'}).text.strip()
        if len(result['sale']) == 0:
            result['sale'] = '0.000'
        result['date'] = el.find('td', {'class': 'respons-collapsed mfcur-table-refreshtime'}).text.strip()

        currency.append(result)
    return render(request, 'app_news/scrape_currency.html', {'currency': currency})


from django.shortcuts import render
import requests

@login_required
def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        days = request.POST.get('days') or '1'  # За замовчуванням 1 день, якщо не вказано

        api_key = env('YOUR_OPENWEATHERMAP_API_KEY')  # Потрібно використати ваш API ключ OpenWeatherMap
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Для отримання температури у градусах Цельсія
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            return render(request, 'app_news/weather_form.html',
                          {'city':city, 'temperature': temperature, 'description': description})
        else:
            return render(request, 'app_news/weather_form.html', {'error': 'Failed to fetch weather data'})

    return render(request, 'app_news/weather_form.html')

