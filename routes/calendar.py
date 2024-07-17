from flask import Flask, render_template
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # render the home page

@app.route('/calendar')
def get_calendar_data():
    # Send a GET request to the website
    url = "https://www.day.lt/"
    response = requests.get(url)
    response.encoding = 'windows-1257'

    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with class 'date_number' for day number
    date_div = soup.find('div', class_='date_number')
    # Find the div with class 'weekday' for day name
    weekday_div = soup.find('div', class_='weekday')
    # Find the span with title 'Metai' for year
    year_span = soup.find('span', title='Metai')
    # Find the div with class 'center' for proverb
    proverb_div = soup.find('div', class_='center')
    # Find the p for year type
    year_type = soup.find('p', title="Metai pagal rytų horoskopą")
    # Find p for zodiac sign
    zodiac = soup.find('p', title="Zodiako ženklas - Žuvys (02.20-03.20)")
     # Find all img tags on the page
    images = soup.find_all('img')
    
    # Extract the text within the span for each element
    day_number = date_div.get_text() if date_div else 'Day number not found'
    day_name = weekday_div.get_text() if weekday_div else 'Day name not found'
    year = year_span.get_text() if year_span else 'Year not found'
    proverb = proverb_div.get_text() if proverb_div else 'Quote not found'
    year_type = year_type.get_text() if year_type else 'Year_type not found'
    zodiac = zodiac.get_text() if zodiac else 'zodiac not found'
        # Get the URLs of the images
    image_urls = [urljoin(url, image.get('src')) for image in images if image.get('alt') in ["Drakonas", "Žuvys (02.20-03.20)"]]
    
    # Return the data to the template
    return day_number, day_name, year, proverb, year_type, zodiac, image_urls

if __name__ == '__main__':
    app.run(debug=True)
