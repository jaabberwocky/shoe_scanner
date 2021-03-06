# Shoe Scanner!

Uses a simple requests/BS4 combination, along with AWS Lambda and SNS topic, to automatically scan a website to see if it changed and then alert if so. Website is here: [URL](https://eflash-sg.doverstreetmarket.com/password).

![architecture](https://s3-ap-southeast-1.amazonaws.com/tobiasleong/lambda_architecture.PNG)

If it **indeed** has changed, a SMS is sent through SNS to subscribed users to alert them. Monitoring is also done through Cloudwatch Logs.

## How to use
1. `git clone` 
2. Make sure you have an `ARN.py` file containing a variable named `ARN` which points to your topic ARN
3. Create your virtual environment using `virtualenv venv` and activate it. Then, run `pip install -r requirements.txt`. 
4. Ensure that aws-cli tools are [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
5. Build using `deployment.sh`

Note: the path to `site-packages` will differ based on the machine you are using. Include python's version if you are running MacOS/Linux, e.g. `path=venv/Lib/python3.6/site-packages`.

## Packages
- BeautifulSoup4
- requests
- boto3

*full list of packages can be found in requirements.txt*
