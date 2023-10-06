import requests
from bs4 import BeautifulSoup as bs
import pandas as p
global df

sites = open("./sites.txt","r").readlines()

data = []
total = len(sites) - 1

def make_spreadsheet(data):
    df = p.DataFrame(data, columns=['Part No','Part Name','Descriptions'])
    return df.to_csv('terraclean.csv', index=False)

def get_data(sites):
    counter = 0
    for url in sites:
        try:
            raw_html = requests.get(url)
            print(counter," / ",total,"\n")
            if raw_html.status_code == 200:
                soup = bs(raw_html.text, 'html.parser')
                part = str(soup.find('h3',class_='hb-heading').span.extract().get_text()).replace("<br/>","")
                part_no = part[-7:]
                desc = str(soup.find_all('div',class_='woocommerce-product-details__short-description')).replace\
                ('<div class="woocommerce-product-details__short-description"><div class="prodRight2InfoBox">',"")
                data.append([part_no, part, desc])
                counter += 1
        except Exception as e:
            print(f"An error occurred: {e}")
    return make_spreadsheet(data)

#
#

def __init__():
    get_data(sites)
