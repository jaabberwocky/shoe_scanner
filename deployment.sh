#!/bin/bash

# note if you're running this in WSL Linux you have to use dos2unix before running to ensure compatibility...

echo "Removing dist folder..."
rm -rf dist
echo "Creating dist folder"
mkdir -p dist
echo "Copying site-packages libraries..."
cp -rf venv/Lib/site-packages/* dist
echo "Copying application code..."
cp application.py dist
cp config.py dist
cp ARN.py dist

cd dist

echo "Zipping file..."
zip -r9 ../function.zip .

cd ..

aws lambda update-function-code --function-name shoe_scanner --zip-file fileb://function.zip
