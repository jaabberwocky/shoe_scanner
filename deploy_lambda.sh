cd venv/Lib/site-packages
zip -r9 ../../../function.zip .

cd ../../..
zip -g function.zip application.py
zip -g function.zip ARN.py
zip -g function.zip config.py

aws lambda update-function-code --function-name shoe_scanner --zip-file fileb://function.zip