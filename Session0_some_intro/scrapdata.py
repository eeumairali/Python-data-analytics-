import requests
from bs4 import BeautifulSoup
import sqlite3

connection = sqlite3.connect('quotes.db')
cursor = connection.cursor()
# Create a table to store quotes if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    author TEXT NOT NULL
)''')

number = 1
for i in range(1, 11):  # Loop through the first 10 pages

    website = f'https://quotes.toscrape.com/page/{i}/'
    response = requests.get(website)


    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        print('' + '-' * 50)
        print(f'Page: {i}, Quote Number: {number}')
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f'Quote: {text}\nAuthor: {author}\n')
        number += 1
        # Insert the quote into the database
        cursor.execute('INSERT INTO quotes (text, author) VALUES (?, ?)', (text, author))

        connection.commit()
        
