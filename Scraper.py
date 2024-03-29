#!/usr/bin/env python3

import sqlite3
import bs4, requests
import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def Scraper():
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
        #elems = soup.select('#price')
        elems = soup.select('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span.a-offscreen') #get the selector path for the price
        return elems[0].text.replace(',','.').replace('€','').strip()


    def getPriceBT(productUrl):
        #getting price from Bertrand
        
        # Set the path to the Brave executable
        chromium_path = '/usr/bin/brave'
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920x1080')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        options.binary_location = chromium_path

        # Create a new instance of the Chrome driver in headless mode
        driver = webdriver.Chrome(options=options)

        driver.get(productUrl)
        driver.implicitly_wait(10)

        # Find the element and extract its text
        element = driver.find_element(By.XPATH, '//*[@id="productPageRightSectionTop-saleAction-price-current"]')
        price = element.text.strip().replace(',', '.').replace('€','')

        # Close the browser
        driver.quit()

        return price
    
    def getAvailable(productUrl):
        #getting price from PcDiga
        
        # Set the path to the Brave executable
        chromium_path = '/usr/bin/brave'
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920x1080')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        options.binary_location = chromium_path

        # Create a new instance of the Chrome driver in headless mode
        driver = webdriver.Chrome(options=options)

        driver.get(productUrl)
        driver.implicitly_wait(10)

        # Find the element and extract its text
        element = driver.find_element(By.XPATH, '//*[@id="productPageRightSectionTop-salesInfo-notAvailable"]/div/span')
        available_status = element.text.strip()

        # Close the browser
        driver.quit()

        return available_status

    conn = sqlite3.connect('/home/shakaw/Documents/PythonProjects/ShakawPy/Scraper/scraped_prices.db')

    #* PC Diga - not scaping atm

    # def getPricePcD(productUrl):
    #     #getting price from PcDiga
        
    #     # Set the path to the Brave executable
    #     chromium_path = '/usr/bin/brave'
    #     options = Options()
    #     options.add_argument('--headless')
    #     options.add_argument('--window-size=1920x1080')
    #     options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    #     options.binary_location = chromium_path

    #     # Create a new instance of the Chrome driver in headless mode
    #     driver = webdriver.Chrome(options=options)

    #     driver.get(productUrl)
    #     driver.implicitly_wait(10)

    #     # Find the element and extract its text
    #     element = driver.find_element(By.XPATH, '//*[@id="body-overlay"]/div[2]/div[1]/main/div[2]/div[2]/div/div/div[1]/div/div[1]/div')
    #     price = element.text.strip().replace(',', '.').replace('€','')

    #     # Close the browser
    #     driver.quit()

    #     return price


    #* Kinda not works sometimes... KuantuKusta - not scraping from here atm
    # def getPriceKK(productUrl):
    #     #getting price from KuantoKusta
        
    #     # Set the path to the Brave executable
    #     chromium_path = '/usr/bin/brave'
    #     options = Options()
    #     options.add_argument('--headless')
    #     options.add_argument('--window-size=1920x1080')
    #     options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    #     options.binary_location = chromium_path

    #     # Create a new instance of the Chrome driver in headless mode
    #     driver = webdriver.Chrome(options=options)

    #     driver.get(productUrl)
    #     driver.implicitly_wait(10)

    #     # Find the element and extract its text
    #     try:
    #         element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/div[5]/div/div/div[2]/span/text()')
    #         print(element.text.strip().replace(',', '.').replace('€',''))
    #     except:
    #         element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/div[5]/div/div/div[3]/span')
    #         print(element.text.strip().replace(',', '.').replace('€',''))
    #     price = element.text.strip().replace(',', '.').replace('€','')
    #     # Close the browser
    #     driver.quit()

    #     return price


    #* PC Componentes - not scraping from here atm

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
        vagabond10price = getPriceBT('https://www.bertrand.pt/livro/vagabond-vol-10-takehiko-inoue/15987162')
        vagabond10avail = getAvailable('https://www.bertrand.pt/livro/vagabond-vol-10-takehiko-inoue/15987162')
        if vagabond10avail != "NOTIFIQUEM-ME QUANDO DISPONÍVEL":
            print(f'Vagabond vol.10 on Bertrand-> {vagabond10price} €')
        else:
            print('Vagabond vol.10 is not available on Bertrand')
        createPriceTable(conn,'VAG_10')
        addPrice(conn,'VAG_10',vagabond10price)
    except:
        print('Error getting Vagabond vol.10 info on Bertrand')

    try:
        vagabond10price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421529157/ref=sr_1_2?dchild=1&keywords=vagabond+vol%2C10&qid=1635865293&qsid=257-9648762-5541941&sr=8-2&sres=B01B99K6TA%2C1421529157%2C1591163404%2C1421549298%2CB00HKW3XZU%2CB09HQW2CZC%2CB09DT9DYWV%2CB0923D58GQ%2CB0184W8UWK%2C4063729478%2C8415922957%2C8415922949%2C8893760886%2CB08YN1LVV8%2CB07H9HZ753%2CB0006OBUWW%2CB0170945UO%2CB016ZZPJT0%2CB00TY5H6LS%2CB00RY9M4EK')
        print(f'Vagabond vol.10 on Amazon -> {vagabond10price} €')
        createPriceTable(conn,'VAG_10')
        addPrice(conn,'VAG_10',vagabond10price)
    except:
        print('Error getting Vagabond vol.10 info on Amazon')

    try:
        readPrice(conn,'VAG_10')
    except:
        print('Vagabond vol.10 has no value stored\n')


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

    print('\n------------------------------------------- MOPA -------------------------------------------\n\n')

    try:
        vileda_mopa = getPriceAmz('https://www.amazon.es/-/pt/dp/B005U94N9A/ref=lp_2165653031_1_2?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&th=1')
        print(f'Vileda Ultramax Mopa on Amazon -> {vileda_mopa} €')
        createPriceTable(conn,'MOPA')
        addPrice(conn,'MOPA',vileda_mopa)
    except:
        print('Error getting Vileda Ultramax Mopa info on Amazon')

    try:
        readPrice(conn,'MOPA')
    except:
        print('Vileda Ultramax Mopa has no value stored\n')

    conn.close()

    time.sleep(30);

if __name__ == '__main__':
    Scraper()