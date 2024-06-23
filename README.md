eBay Products Data Scraping Tool
This tool allows you to scrape product data from eBay by providing a URL to the product listing page. It extracts information such as product name, price, and rating, and displays it in a user-friendly interface.

How to Use
Clone or download this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Run the Flask application by executing python app.py in your terminal.
Open your web browser and navigate to http://127.0.0.1:8000.
Enter the URL of the eBay product listing page and click "Scrape".
Optionally, you can sort the scraped products by name or price range.
Requirements
Python 3.x
Flask
BeautifulSoup4
Requests
File Structure
scrape.py: Contains the web scraping logic using BeautifulSoup.
app.py: Flask application for the web interface and backend logic.
templates/index.html: HTML template for the web interface.
static/style.css: CSS file for styling the web interface.
static/script.js: JavaScript file for client-side scripting.
Credits
This project was created by Niv Caspi.

