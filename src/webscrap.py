from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from json import dumps

def getData(q):
    my_list = []

    url_base = 'https://shopee.com.br/search?keyword='

    option = Options()
    # option.headless = False
    option.add_argument('--headless')
    option.add_argument('window-size=1920x1080')
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    nav = webdriver.Chrome(options=option)

    nav.get(url_base + q)

    # wait for load
    sleep(3)

    # Get scroll height
    last_height = nav.execute_script("return document.body.scrollHeight")

    while True:
        # Select an ipnput to be able to use send_keys
        input = nav.find_element_by_tag_name('input')

        # send a hit in Page Down key
        input.send_keys(Keys.PAGE_DOWN)

        # wait for another action
        sleep(0.3)

        # Calculate new scroll height and compare with last scroll height
        new_height = nav.execute_script("return document.body.scrollHeight")
        print(new_height, last_height)
        if new_height == last_height:
            break
        last_height = new_height

    # select all card of products
    card_el = nav.find_elements_by_class_name('shopee-search-item-result__item')

    for card in card_el:
        # get the html attribute from previous selected cards
        card = card.get_attribute('outerHTML')

        # parse the html with beautifulsoap
        soup = BeautifulSoup(card, 'html.parser')

        # find div with name description of the product
        nome = soup.find('div', attrs={'class': 'yQmmFK _1POlWt _36CEnF'}).getText()
        image = soup.find('img')['src']
        links = 'https://shopee.com.br' + soup.find('a', attrs={'data-sqe': 'link'})['href']
        preco = soup.find('span', attrs={'class': '_24JoLh'}).getText()

        if(nome):
            my_list.append({
                "name": nome,
                "img": image,
                "link": links, 
                "price": preco,
            })

    nav.quit()

    return my_list