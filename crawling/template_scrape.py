'''
In this script:
We use the requests library to send an HTTP GET request to the specified URL.
We check if the request was successful (status code 200).
We use BeautifulSoup to parse the HTML content of the web page.
We find and extract specific elements (in this case, article titles and links) using BeautifulSoup.
'''

# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and extract specific elements (e.g., article titles and links)
        articles = soup.find_all('article')

        for article in articles:
            # Extract the title
            title_tag = article.find('h2')
            title = title_tag.text.strip() if title_tag else 'Title not found'

            # Extract the link
            link_tag = article.find('a')
            link = link_tag['href'] if link_tag and 'href' in link_tag.attrs else 'Link not found'

            # Print the title and link
            print(f'Title: {title}')
            print(f'Link: {link}')
            print()

    except requests.exceptions.RequestException as e:
        print(f'Failed to retrieve the web page: {e}')

if __name__ == '__main__':
    # URL of the website to scrape
    url = 'https://example.com/news/'

    # Call the function to scrape news articles
    scrape_news(url)