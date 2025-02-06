from bs4 import BeautifulSoup
from src.utils.characteristicsProduct import characteristicsProduct

import requests

def showProductDetails(productID):

    #URL PRODUCT DETAILS
    url = f"https://www.ebay.com/itm/{productID}"

    #FETCH PRODUCT BY EBAY URL
    fetchUrl = requests.get(url)
    response = BeautifulSoup(fetchUrl.text, 'html.parser')

    #FILTER DATA PANEL
    infoPanel = response.find('div', id="RightSummaryPanel")
    characteristics = response.find('div', class_="ux-layout-section-module-evo")

    title = infoPanel.find('span', class_="ux-textspans")
    auctionPrice = infoPanel.find('div', class_="x-bid-price")
    immediatePrice = infoPanel.find('div', class_="x-bin-price")

    productDetails = {
        "title": title.text,
        "auctionPrice": auctionPrice.find('div',class_="x-price-primary").text if auctionPrice else "No hay precio de Subasta",
        "immediatePrice": immediatePrice.find('div',class_="x-price-primary").text if immediatePrice else "No hay precio inmediato",
    }


    characteristicsDetails = {
        "characteristics": characteristicsProduct(characteristics)
    }

    return [productDetails,characteristicsDetails]

