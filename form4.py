from bs4 import BeautifulSoup
from cik_match import get_ticker
import requests


def form4(cik):
    url = 'https://www.secform4.com/insider-trading/' + str(cik) + '.htm'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, features="html.parser")
    data = []
    table = soup.find('table', attrs={'class':'sort-table'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    return data 
