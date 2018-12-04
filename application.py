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
    Returns none if nothing is found
    '''
    image_list = soup.find_all('img')
    if len(image_list) == 0:
        return None
    else:
        image_src = soup.find_all('img')[0]['src']
        if image_src == '//cdn.shopify.com/s/files/1/1994/0655/t/1/assets/password.png?6921477390879209528':
            return True
        else:
            return False


def check_title(soup, title='Dover Street Market SG – Opening Soon'):
    '''
    Checks if title is still the same
    '''
    if soup.title.text.strip(" ").rstrip("\n").lstrip("\n").lstrip(" ") == title:
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


def lambda_handler(request, context):
    '''
    lambda handler for AWS, note that request and context is asked, but not used
    '''
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
    if check_title(soup):
        print("Website scanned, nothing to report")
    else:
        print("Website scanned, site changed!")
        send_sns_message(
            client, ARN, "Website has changed! Quickly go to website now!")
    return None

if __name__ == "__main__":
    request, context = None, None
    lambda_handler(request,context)
