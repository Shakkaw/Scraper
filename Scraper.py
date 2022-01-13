#!/usr/bin/env python

import sqlite3
import bs4, requests
import datetime
import time

def createPriceTable(conn,TableName):
    cursor = conn.cursor()
    create_item_table = f'''CREATE TABLE IF NOT EXISTS {TableName} (
                            Price FLOAT,
                            AddedDate timestamp);'''
    cursor.execute(create_item_table)
    conn.commit()

def addPrice(conn,TableName,Price):
    dt = datetime.datetime.now()
    cursor = conn.cursor()
    info = (Price, dt)
    add_item_price = (f'INSERT INTO {TableName}(Price, AddedDate) VALUES (?, ?);')
    cursor.execute(add_item_price, info)
    conn.commit()

def readPrice(conn,TableName):
    cursor = conn.cursor()
    cursor.execute('SELECT MIN(Price) FROM '+ TableName)
    for row in cursor:
        print(f'The lowest price for this item is -> {row[0]}\n')


def getPriceAmz(productUrl):
    # getting price from Amazon

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Language': 'en-US'
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    html_contents = res.text

    soup = bs4.BeautifulSoup(html_contents, 'html.parser')
    elems = soup.select('#price')
    #elems = soup.select('#price_inside_buybox') #get the selector path for the price
    return elems[0].text.strip().replace(',', '.')



def getPriceBT(productUrl):
    # getting price from Bertrand

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Language': 'en-US'
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    html_contents = res.text

    soup = bs4.BeautifulSoup(html_contents, 'html.parser')
    elems = soup.select('#productPageRightSectionTop-saleAction-price-current') #get the selector path for the price
    return elems[0].text.strip().replace(',', '.').replace('€','')

def getDiscount(productUrl):
    # getting % discount from Bertrand
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Language': 'en-US'
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    html_contents = res.text

    soup = bs4.BeautifulSoup(html_contents, 'html.parser') 
    elems = soup.select('#productPageRightSectionTop-stickers-discount > div > div') #get the selector path for the discount
    return elems[0].text.strip()

conn = sqlite3.connect('/home/shakaw/Documents/PythonProjects/ShakawPy/Scraper/scraped_prices.db')


#* no longer scraping from this site so commenting out this part

# def getPricePC(productUrl):
#     #getting price from PC Componentes

#     headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
#     'Accept-Language': 'en-US'
#     }
#     res = requests.get(productUrl, headers=headers)
#     res.raise_for_status()
#     html_contents = res.text

#     soup = bs4.BeautifulSoup(html_contents, 'html.parser')
#     elems = soup.select('#precio-main > span.baseprice') #get the selector path for the price
#     elemsCents = soup.select('#precio-main > span.cents')  
                                                     
#     return elems[0].text.strip() + elemsCents[0].text.strip().replace(',', '.')

print('\n------------------------------------------- Vagabond books -------------------------------------------\n\n')

try:
    vagabond4price = getPriceBT('https://www.bertrand.pt/livro/vagabond-takehiko-inoue/15790066')
    vagabond4disc = getDiscount('https://www.bertrand.pt/livro/vagabond-takehiko-inoue/15790066')
    print(f'Vagabond vol.4 on Bertrand -> {vagabond4price} €')
    print(f'Discount -> {vagabond4disc}')
    createPriceTable(conn,'VAG_4')
    addPrice(conn,'VAG_4',vagabond4price)
except:
    print('Vagabond vol.4 is not available on Bertrand')

try:
    vagabond4price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421522462/ref=pd_sbs_5/257-9648762-5541941?pd_rd_w=D7M0e&pf_rd_p=dcd633b7-cb38-4615-862b-a9bd1fbbb388&pf_rd_r=CXBBYJ6V5FDGNRY002DS&pd_rd_r=593cae26-9713-447f-8fb0-8907a3f533d6&pd_rd_wg=NisD1&pd_rd_i=1421522462&psc=1')
    print(f'Vagabond vol.4 on Amazon -> {vagabond4price} €')
    createPriceTable(conn,'VAG_4')
    addPrice(conn,'VAG_4',vagabond4price)
except:
    print('Vagabond vol.4 is not available on Amazon')

try:
    readPrice(conn,'VAG_4')
except:
    print('Vagabond vol.4 has no value stored\n')

try:
    vagabond6price = getPriceBT('https://www.bertrand.pt/livro/vagabond-6-takehiko-inoue/15832345')
    vagabond6disc = getDiscount('https://www.bertrand.pt/livro/vagabond-6-takehiko-inoue/15832345')
    print(f'Vagabond vol.6 on Bertrand -> {vagabond6price} €')
    print(f'Discount -> {vagabond6disc}')
    createPriceTable(conn,'VAG_6')
    addPrice(conn,'VAG_6',vagabond6price)
except:
    print('Vagabond vol.6 is not available on Bertrand')

try:
    vagabond6price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421522802/ref=pd_sbs_2/257-9648762-5541941?pd_rd_w=IHr2z&pf_rd_p=dcd633b7-cb38-4615-862b-a9bd1fbbb388&pf_rd_r=QSR7Q1ZYGNNK6ERDWBK4&pd_rd_r=b49a2056-9d1e-47e1-b6aa-d32f0efe5354&pd_rd_wg=d1MP9&pd_rd_i=1421522802&psc=1')
    print(f'Vagabond vol.6 on Amazon -> {vagabond6price} €')
    createPriceTable(conn,'VAG_6')
    addPrice(conn,'VAG_6',vagabond6price)
except:
    print('Vagabond vol.6 is not available on Amazon')

try:
    readPrice(conn,'VAG_6')
except:
    print('Vagabond vol.6 has no value stored\n')

try:
    vagabond10price = getPriceBT('https://www.bertrand.pt/livro/vagabond-10-takehiko-inoue/15987162')
    vagabond10disc = getDiscount('https://www.bertrand.pt/livro/vagabond-10-takehiko-inoue/15987162')
    print(f'Vagabond vol.10 on Bertrand-> {vagabond10price} €')
    print(f'Discount -> {vagabond10disc}')
    createPriceTable(conn,'VAG_10')
    addPrice(conn,'VAG_10',vagabond10price)
except:
    print('Vagabond vol.10 is not available on Bertrand')

try:
    vagabond10price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421529157/ref=sr_1_2?dchild=1&keywords=vagabond+vol%2C10&qid=1635865293&qsid=257-9648762-5541941&sr=8-2&sres=B01B99K6TA%2C1421529157%2C1591163404%2C1421549298%2CB00HKW3XZU%2CB09HQW2CZC%2CB09DT9DYWV%2CB0923D58GQ%2CB0184W8UWK%2C4063729478%2C8415922957%2C8415922949%2C8893760886%2CB08YN1LVV8%2CB07H9HZ753%2CB0006OBUWW%2CB0170945UO%2CB016ZZPJT0%2CB00TY5H6LS%2CB00RY9M4EK')
    print(f'Vagabond vol.10 on Amazon -> {vagabond10price} €')
    createPriceTable(conn,'VAG_10')
    addPrice(conn,'VAG_10',vagabond10price)
except:
    print('Vagabond vol.10 is not available on Amazon')

try:
    readPrice(conn,'VAG_10')
except:
    print('Vagabond vol.10 has no value stored\n')

try:
    vagabond12price = getPriceBT('https://www.bertrand.pt/livro/vagabond-takehiko-inoue/16241581')
    vagabond12disc = getDiscount('https://www.bertrand.pt/livro/vagabond-takehiko-inoue/16241581')
    print(f'Vagabond vol.12 on Bertrand -> {vagabond12price} €')
    print(f'Discount -> {vagabond12disc}')
    createPriceTable(conn,'VAG_12')
    addPrice(conn,'VAG_12',vagabond12price)
except:
    print('Vagabond vol.12 is not available on Bertrand')

try:
    vagabond12price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421573342/ref=sr_1_1?dchild=1&keywords=vagabond+vol%2C12&qid=1635865313&qsid=257-9648762-5541941&sr=8-1&sres=1421573342%2CB08PMT7D2N%2CB0923DVKD4%2C1421549298%2C8415922957%2C8415922949%2CB017SIWRGG%2CB01M8MEWTJ%2CB008V4OH7O%2CB008V4NYGE%2CB008SNP4OI%2CB07VS9QH1D%2CB00RY9M4EK%2CB00PH9FB5I%2CB0006OBUXG%2CB012HUPMNU%2CB08X4X24QJ%2C1421533235%2C1421528622%2C1421533243')
    print(f'Vagabond vol.12 on Amazon ->  {vagabond12price} €')
    createPriceTable(conn,'VAG_12')
    addPrice(conn,'VAG_12',vagabond12price)
except:
    print('Vagabond vol.12 is not available on Amazon')

try:
    readPrice(conn,'VAG_12')
except:
    print('Vagabond vol.12 has no value stored\n')

#* leaving one instance here in case needed in the future

# print('\n------------------------------------------- Gaming PC -------------------------------------------\n\n')

# try:
#     priceLG = getPricePC('https://www.pccomponentes.pt/lg-29wn600-w-29-led-ips-ultrawide-fullhd-freesync')
#     print('LG LG 29WN600-W 29" LED IPS UltraWide FullHD FreeSync price -> ' + priceLG + ' €')
#     createPriceTable(conn,'TV_LG')
#     addPrice(conn,'TV_LG',priceLG)
#     readPrice(conn,'TV_LG')
# except:
#     print('LG 29WN600-W 29" LED IPS UltraWide FullHD FreeSync not available on PC Componentes')

conn.close()

time.sleep(30);