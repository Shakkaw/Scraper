import bs4, requests

def getPriceAmz(productUrl):
    #getting price from Amazon
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
    return elems[0].text.strip()


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
    return elems[0].text.strip()

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
                                                     
    return elems[0].text.strip() + elemsCents[0].text.strip() + "€"


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

print('------------------------------------------- Vagabond books -------------------------------------------')

try:
    vagabond3price = getPriceBT('https://www.bertrand.pt/livro/vagabond-3-takehiko-inoue/15711331')
    vagabond3disc = getDiscount('https://www.bertrand.pt/livro/vagabond-3-takehiko-inoue/15711331')
    print('Vagabond vol.3 on Bertrand -> ' + vagabond3price)
    print('Discount -> ' + vagabond3disc)
except:
    print('Vagabond vol.3 is not available on Bertrand')

try:
    vagabond3price = getPriceAmz('https://www.amazon.es/dp/1421522454/ref=monarch_sidesheet')
    print('Vagabond vol.3 on Amazon -> ' + vagabond3price)
except:
    print('Vagabond vol.3 is not available on Amazon\n')

try:
    vagabond4price = getPriceBT('https://www.bertrand.pt/livro/vagabond-takehiko-inoue/15790066')
    vagabond4disc = getDiscount('https://www.bertrand.pt/livro/vagabond-takehiko-inoue/15790066')
    print('Vagabond vol.4 on Bertrand -> ' + vagabond4price)
    print('Discount -> ' + vagabond4disc)
except:
    print('Vagabond vol.4 is not available on Bertrand')

try:
    vagabond4price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421522462/ref=pd_sbs_5/257-9648762-5541941?pd_rd_w=D7M0e&pf_rd_p=dcd633b7-cb38-4615-862b-a9bd1fbbb388&pf_rd_r=CXBBYJ6V5FDGNRY002DS&pd_rd_r=593cae26-9713-447f-8fb0-8907a3f533d6&pd_rd_wg=NisD1&pd_rd_i=1421522462&psc=1')
    print('Vagabond vol.4 on Amazon -> ' + vagabond4price)
except:
    print('Vagabond vol.4 is not available on Amazon\n')

try:
    vagabond6price = getPriceBT('https://www.bertrand.pt/livro/vagabond-6-takehiko-inoue/15832345')
    vagabond6disc = getDiscount('https://www.bertrand.pt/livro/vagabond-6-takehiko-inoue/15832345')
    print('Vagabond vol.6 on Bertrand -> ' + vagabond6price)
    print('Discount -> ' + vagabond6disc)
except:
    print('Vagabond vol.6 is not available on Bertrand')

try:
    vagabond6price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421522802/ref=pd_sbs_2/257-9648762-5541941?pd_rd_w=IHr2z&pf_rd_p=dcd633b7-cb38-4615-862b-a9bd1fbbb388&pf_rd_r=QSR7Q1ZYGNNK6ERDWBK4&pd_rd_r=b49a2056-9d1e-47e1-b6aa-d32f0efe5354&pd_rd_wg=d1MP9&pd_rd_i=1421522802&psc=1')
    print('Vagabond vol.6 on Amazon -> ' + vagabond6price)
except:
    print('Vagabond vol.6 is not available on Amazon\n')

try:
    vagabond7price = getPriceBT('https://www.bertrand.pt/livro/vagabond-7-takehiko-inoue/15921656')
    vagabond7disc = getDiscount('https://www.bertrand.pt/livro/vagabond-7-takehiko-inoue/15921656')
    print('Vagabond vol.7 on Bertrand-> ' + vagabond7price)
    print('Discount -> ' + vagabond7disc)
except:
    print('Vagabond vol.7 is not available on Bertrand')

try:
    vagabond3price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421522810/ref=pd_sbs_6/257-9648762-5541941?pd_rd_w=i9Ei6&pf_rd_p=dcd633b7-cb38-4615-862b-a9bd1fbbb388&pf_rd_r=3WB5J8V8ZRWFB8J3C7XP&pd_rd_r=e764c31a-581d-4dee-a71f-f043cd85168f&pd_rd_wg=uptad&pd_rd_i=1421522810&psc=1')
    print('Vagabond vol.7 on Amazon -> ' + vagabond7price)
except:
    print('Vagabond vol.7 is not available on Amazon\n')

try:
    vagabond10price = getPriceBT('https://www.bertrand.pt/livro/vagabond-10-takehiko-inoue/15987162')
    vagabond10disc = getDiscount('https://www.bertrand.pt/livro/vagabond-10-takehiko-inoue/15987162')
    print('Vagabond vol.10 on Bertrand-> ' + vagabond10price)
    print('Discount -> ' + vagabond10disc)
except:
    print('Vagabond vol.10 is not available on Bertrand')

try:
    vagabond10price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421529157/ref=sr_1_2?dchild=1&keywords=vagabond+vol%2C10&qid=1635865293&qsid=257-9648762-5541941&sr=8-2&sres=B01B99K6TA%2C1421529157%2C1591163404%2C1421549298%2CB00HKW3XZU%2CB09HQW2CZC%2CB09DT9DYWV%2CB0923D58GQ%2CB0184W8UWK%2C4063729478%2C8415922957%2C8415922949%2C8893760886%2CB08YN1LVV8%2CB07H9HZ753%2CB0006OBUWW%2CB0170945UO%2CB016ZZPJT0%2CB00TY5H6LS%2CB00RY9M4EK')
    print('Vagabond vol.10 on Amazon -> ' + vagabond10price)
except:
    print('Vagabond vol.10 is not available on Amazon\n')

try:
    vagabond12price = getPriceBT('https://www.bertrand.pt/livro/vagabond-takehiko-inoue/16241581')
    vagabond12disc = getDiscount('https://www.bertrand.pt/livro/vagabond-takehiko-inoue/16241581')
    print('Vagabond vol.12 on Bertrand -> ' + vagabond12price)
    print('Discount -> ' + vagabond12disc)
except:
    print('Vagabond vol.12 is not available on Bertrand')

try:
    vagabond12price = getPriceAmz('https://www.amazon.es/-/pt/dp/1421573342/ref=sr_1_1?dchild=1&keywords=vagabond+vol%2C12&qid=1635865313&qsid=257-9648762-5541941&sr=8-1&sres=1421573342%2CB08PMT7D2N%2CB0923DVKD4%2C1421549298%2C8415922957%2C8415922949%2CB017SIWRGG%2CB01M8MEWTJ%2CB008V4OH7O%2CB008V4NYGE%2CB008SNP4OI%2CB07VS9QH1D%2CB00RY9M4EK%2CB00PH9FB5I%2CB0006OBUXG%2CB012HUPMNU%2CB08X4X24QJ%2C1421533235%2C1421528622%2C1421533243')
    print('Vagabond vol.12 on Amazon -> ' + vagabond12price)
except:
    print('Vagabond vol.12 is not available on Amazon\n')


print('------------------------------------------- Gaming PC -------------------------------------------\n')

try:
    priceLG = getPricePC('https://www.pccomponentes.pt/lg-29wn600-w-29-led-ips-ultrawide-fullhd-freesync')
    print('\nLG LG 29WN600-W 29" LED IPS UltraWide FullHD FreeSync price -> ' + priceLG)
except:
    print('LG 29WN600-W 29" LED IPS UltraWide FullHD FreeSync not available')

try:
    priceWCAM = getPricePC('https://www.pccomponentes.pt/trust-gxt-1160-vero-streaming-webcam-fullhd')
    print('\nTrust GXT 1160 Vero Streaming Webcam FullHD price -> ' + priceWCAM)
except:
    print('Trust GXT 1160 Vero Streaming Webcam FullHD not available')

try:
    priceKBoard = getPricePC('https://www.pccomponentes.pt/tempest-k9-rgb-backlit-teclado-gaming-rgb')
    print('\nTempest K9 RGB Backlit Teclado Gaming RGB price -> ' + priceKBoard)
except:
    print('Tempest K9 RGB Backlit Teclado Gaming RGB not available')