from config import ProductionConfiguration, TestConfiguration
import boto3
import requests
from ARN import ARN
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

def get_sns_client():
    '''
    Returns SNS client obj
    '''
    return boto3.client('sns')

def send_sns_message(client, ARN, msg):
    '''
    Sends SNS message to topic
    '''
    r = client.publish(
        TopicArn=ARN,
        Message=msg
    )
    return None

def lambda_handler(request,context):
    # init and get html/soup
    cfg = initialise('https://eflash-sg.doverstreetmarket.com/password')
    html_text = get_page(cfg.target)
    if html_text is None:
        print("page is not found")
        return None
    soup = get_soup(html_text)
    
    # open sns client
    client = get_sns_client()

    # is img inside?
    if check_image(soup):
        print("Website scanned, nothing to report")
    else:
        send_sns_message(client, ARN, "Website has changed! Quickly go to website now!")
    
    return None

    

