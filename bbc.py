from datetime import datetime
import requests
from bs4 import BeautifulSoup

BBC_URL = 'https://www.bbc.com/news'

def grab_bbc():
    now = datetime.utcnow()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S.%f')

    try:
        page = requests.get(BBC_URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        headline = soup.find('h3').text.strip()

    except:
        headline = '**COLLECTION ERROR**'
    
    return timestamp, headline
