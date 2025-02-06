import requests
from bs4 import BeautifulSoup


def searchProduct(productName):

    #URL EBAY

    url = f"https://www.ebay.com/sch/i.html?_nkw={productName}&_sacat=0&_from=R40&_dmd=2&_sop=10&_ipg=120"

    #Fetching URL

    fetchUrl = requests.get(url)
    elementsFetchUrl = BeautifulSoup(fetchUrl.text, 'html.parser')

    #Filter Wrapper Products

    products = elementsFetchUrl.findAll('div', class_="s-item__wrapper")

    #Create Products List

    listProducts = []
    for product in products:
        title = product.find('div', class_="s-item__title").text
        price = product.find('span', class_="s-item__price").text
        date = product.find('span', class_="BOLD")

        if date:
            date = date.get_text()
        else:
            date = "No hay fecha"

        if "Shop on eBay" in title:
            continue

        listProducts.append({
            'title': title,
            'price': price.replace("S/. ",""),
            'date': date,
            'link': product.a['href']
        })
    return listProducts







