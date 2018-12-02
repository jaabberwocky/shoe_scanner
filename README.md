# Shoe Scanner!

Uses a simple requests/BS4 combination, along with AWS Lambda and SNS topic, to automatically scan a website to see if it changed. Website is here: [URL](https://eflash-sg.doverstreetmarket.com/password).

If it **indeed** has changed, a SMS is sent to subscribed users to alert them.

## How to use
1. `git clone` 
2. Make sure you have an `ARN.py` file containing a variable named `ARN` which points to your topic ARN
3. Ensure that aws-cli tools are configured
4. Build using `deployment.sh`

## Packages
- BeautifulSoup4
- requests
- boto3

*full list of packages can be found in requirements.txt*
