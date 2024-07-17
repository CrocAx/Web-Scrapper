from flask import Flask, render_template
from routes.calendar import get_calendar_data  # Import the function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calendar')
def calendar(): 
    # Call the function and unpack the returned values
    day_number, day_name, year, proverb, year_type, zodiac, image_urls = get_calendar_data()

    return render_template('calendar.html', day_number=day_number, day_name=day_name, year=year, proverb=proverb, year_type=year_type, zodiac=zodiac, image_urls=image_urls)
if __name__ == '__main__':
    app.run(debug=True)
