# pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_items(search_query, max_pages=1):
    # Initialize a DataFrame to store the results
    columns = ['Title', 'Image URL', 'Price'] 
    df = pd.DataFrame(columns=columns)

    for page in range(1, max_pages + 1):
        # Construct the URL with the search query and page number
        url = f'https://example.com/search?q={search_query}&page={page}'

        try:
            # Send an HTTP GET request to the URL
            response = requests.get(url)
            response.raise_for_status()

            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and extract item information (title, image URL, price)
            items = soup.find_all('div', class_='item')

            for item in items:
                title = item.find('h2').text.strip()
                image_url = item.find('img')['src']
                price = item.find('span', class_='price').text.strip()

                # Append the item to the DataFrame
                df = df.append({'Title': title, 'Image URL': image_url, 'Price': price}, ignore_index=True)

        except requests.exceptions.RequestException as e:
            print(f'Failed to retrieve page {page}: {e}')
            break

    return df

if __name__ == '__main__':
    search_query = 'laptop'  # Replace with your search query
    max_pages = 3  # Set the maximum number of pages to scrape

    # Call the function to scrape items
    df = scrape_items(search_query, max_pages)

    # Get the current date for the filename
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Save the DataFrame to a CSV file with a date-based filename
    csv_filename = f'{current_date}-{search_query}-web scraped.csv'
    df.to_csv(csv_filename, index=False)

    print(f'Scraped {len(df)} items and saved to {csv_filename}')