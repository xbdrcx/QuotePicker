import os
import requests
from random import randrange
from bs4 import BeautifulSoup

os.system('cls')

URLS = [
    "https://www.brainyquote.com/topics/inspirational-quotes",
    "https://www.brainyquote.com/topics/attitude-quotes",
    "https://www.brainyquote.com/topics/brainy-quotes",
    "https://www.brainyquote.com/topics/change-quotes"
]

numUrls = len(URLS)

page = requests.get(URLS[randrange(numUrls)])

soup = BeautifulSoup(page.content, "html.parser")

quotes = soup.find_all(style="display: flex;justify-content: space-between")
authors = soup.find_all(title="view author")

numQuotes = len(quotes)

pick = randrange(numQuotes)

print("\n", quotes[pick].text, "\n - ", authors[pick].text, "\n\n\n")

input("Press Any Key To Exit.")