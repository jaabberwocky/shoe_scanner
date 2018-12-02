# Shoe Scanner!

Uses a simple requests/BS4 combination, along with AWS Lambda and SNS topic, to automatically scan a website to see if it changed. Website is here: (URL)[https://eflash-sg.doverstreetmarket.com/password]

If it **indeed** has changed, a SMS is sent to subscribed users to alert them.

## Packages
- BeautifulSoup4
- requests
- boto3