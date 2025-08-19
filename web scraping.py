import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'http://quotes.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all quote elements
    quotes = soup.find_all('div', class_='quote')
    
    # Create a list to store the quotes
    quotes_list = []
    
    # Loop through each quote element and extract the text and author
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        quotes_list.append({'text': text, 'author': author})
    
    # Print the collected quotes
    for item in quotes_list:
        print(f"Quote: {item['text']} - Author: {item['author']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
