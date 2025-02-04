from bs4 import BeautifulSoup
import requests, json

def showProductDetails(productID):

    #URL PRODUCT DETAILS
    url = f"https://www.ebay.com/itm/{productID}"

    #FETCH PRODUCT BY EBAY URL
    fetchUrl = requests.get(url)
    response = BeautifulSoup(fetchUrl.text, 'html.parser')

    #Filter Product Details
