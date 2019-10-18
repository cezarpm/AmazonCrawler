import requests
from bs4 import BeautifulSoup

def get_product(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    if(soup.find(id="productTitle")):

        title = soup.find(id="productTitle").get_text()

    else:
        title = soup.find(id="ebooksProductTitle").get_text()

    price = soup.find(
        "span", {"class": "a-size-medium a-color-price"}).get_text()

    print(title.strip(), price.strip())    

get_product('https://www.amazon.com.br/Smart-Philips-32PHG5813-78-Preto/dp/B075KFH2QW/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=tv&qid=1571420737&sr=8-2')