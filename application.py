from config import ProductionConfiguration, TestConfiguration
import boto3
import requests
from bs4 import BeautifulSoup

def initialise(URL):
    '''
    Set URL and config variables
    '''
    cfg = ProductionConfiguration(URL)
    return cfg

def get_page(target):
    '''
    Check if URL returns 200 and then returns HTML; none if otherwise
    '''
    r = requests.get(target)
    if r.status_code == 200:
        # req was successful
        return r.text
    else:
        return None

def get_soup(html):
    '''
    Returns soup object from HTML text
    '''
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def check_image(soup):
    '''
    Checks if image is returning from the same source (which shows the e-flash opening soon sign)
    '''
    image_src = soup.find_all('img')[0]['src']
    if image_src == '//cdn.shopify.com/s/files/1/1994/0655/t/1/assets/password.png?6921477390879209528':
        return True
    else:
        return False
    

if __name__ == "__main__":

    cfg = initialise('https://eflash-sg.doverstreetmarket.com/password')
    html_text = get_page(cfg.target)
    soup = get_soup(html_text)
    print(soup.title)

