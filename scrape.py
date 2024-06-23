import requests
from bs4 import BeautifulSoup
from flask import Flask, request, render_template

app = Flask(__name__)

def scrape_ebay(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        for item in soup.select('.s-item'):
            name = item.select_one('.s-item__title')
            price = item.select_one('.s-item__price')
            rating = item.select_one('.s-item__reviews-count')
            if name and price:
                products.append({
                    'name': name.get_text(),
                    'price': price.get_text(),
                    'rating': rating.get_text() if rating else 'No rating'
                })
        return products, None
    except requests.exceptions.MissingSchema:
        return [], "Invalid URL: No scheme supplied. Please include 'http://' or 'https://'."
    except requests.exceptions.ConnectionError as e:
        return [], f"Connection error: Not an actual URL."
    except requests.exceptions.HTTPError as e:
        return [], f"HTTP error: Cannot access the URL. Make sure it is a correct URL of eBay."
    except Exception as e:
        return [], f"An error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    products = []
    error = None
    if request.method == 'POST':
        url = request.form['url']
        sort_by = request.form['sort_by']
        min_price = request.form.get('min_price', None)
        max_price = request.form.get('max_price', None)
        products, error = scrape_ebay(url)
        if sort_by == 'price':
            products = sorted(products, key=lambda x: float(x['price'].replace('ILS ', '').replace(',', '')))
            if min_price:
                min_price = float(min_price)
                products = [product for product in products if float(product['price'].replace('ILS ', '').replace(',', '')) >= min_price]
            if max_price:
                max_price = float(max_price)
                products = [product for product in products if float(product['price'].replace('ILS ', '').replace(',', '')) <= max_price]
        elif sort_by == 'name':
            products = sorted(products, key=lambda x: x['name'])
    return render_template('index.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
