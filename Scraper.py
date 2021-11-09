import sqlite3
import bs4, requests


def createPriceTable(conn,TableName):
    cursor = conn.cursor()
    cursor.execute(
        ' CREATE TABLE IF NOT EXISTS '+ TableName + '(Price FLOAT)'
    )
    conn.commit()

def addPrice(conn,TableName,Price):
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO '+ TableName + '(Price) VALUES (' + Price + ')'
    )
    conn.commit()

def readPrice(conn,TableName):
    cursor = conn.cursor()
    cursor.execute('SELECT MIN(Price) FROM '+ TableName)
    for row in cursor:
        print(f'The lowest price for this item is -> {row}\n')


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

def getPricePC(productUrl):
    #getting price from PC Componentes

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Language': 'en-US'
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    html_contents = res.text

    soup = bs4.BeautifulSoup(html_contents, 'html.parser')
    elems = soup.select('#precio-main > span.baseprice') #get the selector path for the price
    elemsCents = soup.select('#precio-main > span.cents')  
                                                     
    return elems[0].text.strip() + elemsCents[0].text.strip().replace(',', '.')


def getDiscount(productUrl):
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

conn = sqlite3.connect('scraped_prices.db')

print('\n------------------------------------------- Vagabond books -------------------------------------------\n\n')

try:
    vagabond3price = getPriceBT('https://www.bertrand.pt/livro/vagabond-3-takehiko-inoue/15711331')
    vagabond3disc = getDiscount('https://www.bertrand.pt/livro/vagabond-3-takehiko-inoue/15711331')
    print(f'Vagabond vol.3 on Bertrand -> {vagabond3price} €')
    print(f'Discount -> {vagabond3disc}')
    createPriceTable(conn,'VAG_3')
    addPrice(conn,'VAG_3',vagabond3price)
except:
    print('Vagabond vol.3 is not available on Bertrand')

try:
    vagabond3price = getPriceAmz('https://www.amazon.es/dp/1421522454/ref=monarch_sidesheet')
    print(f'Vagabond vol.3 on Amazon -> {vagabond3price} €')
    createPriceTable(conn,'VAG_3')
    addPrice(conn,'VAG_3',vagabond3price)
except:
    print('Vagabond vol.3 is not available on Amazon')

try:
    readPrice(conn,'VAG_3')
except:
    print('Vagabond vol.3 has no value stored\n')

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
    vagabond7price = getPriceBT('https://www.bertrand.pt/livro/vagabond-7-takehiko-inoue/15921656')
    vagabond7disc = getDiscount('https://www.bertrand.pt/livro/vagabond-7-takehiko-inoue/15921656')
    print(f'Vagabond vol.7 on Bertrand-> {vagabond7price} €')
    print(f'Discount -> {vagabond7disc}')
    createPriceTable(conn,'VAG_7')
    addPrice(conn,'VAG_7',vagabond7price)
except:
    print('Vagabond vol.7 is not available on Bertrand')

try:
    vagabond3price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421522810/ref=pd_sbs_6/257-9648762-5541941?pd_rd_w=i9Ei6&pf_rd_p=dcd633b7-cb38-4615-862b-a9bd1fbbb388&pf_rd_r=3WB5J8V8ZRWFB8J3C7XP&pd_rd_r=e764c31a-581d-4dee-a71f-f043cd85168f&pd_rd_wg=uptad&pd_rd_i=1421522810&psc=1')
    print(f'Vagabond vol.7 on Amazon -> {vagabond7price} €')
    createPriceTable(conn,'VAG_7')
    addPrice(conn,'VAG_7',vagabond7price)
except:
    print('Vagabond vol.7 is not available on Amazon')

try:
    readPrice(conn,'VAG_7')
except:
    print('Vagabond vol.7 has no value stored\n')

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

print('\n------------------------------------------- Gaming PC -------------------------------------------\n\n')

try:
    priceLG = getPricePC('https://www.pccomponentes.pt/lg-29wn600-w-29-led-ips-ultrawide-fullhd-freesync')
    print('LG LG 29WN600-W 29" LED IPS UltraWide FullHD FreeSync price -> ' + priceLG + ' €')
    createPriceTable(conn,'TV_LG')
    addPrice(conn,'TV_LG',priceLG)
    readPrice(conn,'TV_LG')
except:
    print('LG 29WN600-W 29" LED IPS UltraWide FullHD FreeSync not available on PC Componentes')

try:
    priceWCAM = getPricePC('https://www.pccomponentes.pt/trust-gxt-1160-vero-streaming-webcam-fullhd')
    print('Trust GXT 1160 Vero Streaming Webcam FullHD price -> ' + priceWCAM + ' €')
    createPriceTable(conn,'WEBCAM')
    addPrice(conn,'WEBCAM',priceWCAM)
    readPrice(conn,'WEBCAM')
except:
    print('Trust GXT 1160 Vero Streaming Webcam FullHD not available on PC Componentes')

try:
    priceKBoard = getPricePC('https://www.pccomponentes.pt/tempest-k9-rgb-backlit-teclado-gaming-rgb')
    print('Tempest K9 RGB Backlit Teclado Gaming RGB price -> ' + priceKBoard + ' €')
    createPriceTable(conn,'KEYBOARD')
    addPrice(conn,'KEYBOARD',priceKBoard)
    readPrice(conn,'KEYBOARD')
except:
    print('Tempest K9 RGB Backlit Teclado Gaming RGB not available on PC Componentes')

try:
    priceCpu5 = getPricePC('https://www.pccomponentes.pt/amd-ryzen-5-5600x-37ghz')
    print(f'AMD Ryzen 5 5600X 3.7GHz price -> {priceCpu5} €')
    createPriceTable(conn,'CPU_R5')
    addPrice(conn,'CPU_R5',priceCpu5)
    readPrice(conn,'CPU_R5')
except:
    print('AMD Ryzen 5 5600X 3.7GHz not available on PC Componentes')

try:
    priceCpu7 = getPricePC('https://www.pccomponentes.pt/amd-ryzen-7-5800x-38ghz')
    print(f'AMD Ryzen 7 5800X 3.8GHz price -> {priceCpu7} €')
    createPriceTable(conn,'CPU_R7')
    addPrice(conn,'CPU_R7',priceCpu7)
    readPrice(conn,'CPU_R7')
except:
    print('AMD Ryzen 7 5800X 3.8GHz not available on PC Componentes')

try:
    priceSSD = getPricePC('https://www.pccomponentes.pt/samsung-980-ssd-1tb-pcie-30-nvme-m2')
    print(f'Samsung 980 SSD 1TB PCIe 3.0 NVMe M.2 price -> {priceSSD} €')
    createPriceTable(conn,'SSD')
    addPrice(conn,'SSD',priceSSD)
    readPrice(conn,'SSD')
except:
    print('Samsung 980 SSD 1TB PCIe 3.0 NVMe M.2 price not available on PC Componentes')

conn.close()