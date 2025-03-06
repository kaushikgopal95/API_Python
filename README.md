# API Automation using BDD(Behave)

[Automation Report](
behave-python-api-automation.netlify.app)

[Reference Link](https://requests.readthedocs.io/en/latest/)

## Libraries Used:

    requests
    json
    configparser

## How to use

### Import necessary libraries

```
import requests
import json
import configparser
```

### Use requests.get and requests.post methods

```
response = requests.get(URL)
response = requests.post(URL, data=payload)
```

### Parse response

```
response.text
json.load
json.loads(response.text)
response.json()
response.status_code
response.headers
response.cookies
```
### Use .ini file for configurations
```
config = configparser.ConfigParser()
config.read('config.ini')
endpoint = config['API']['endpoint']
```

### Override SSL certifications

`response = requests.get(URL, verify=False)`


`pip install git+https://github.com/behave/behave`

### Run feature files

`behave ./features`

### Use tags and format plain

`behave --no-capture --tags=between-time --format plain`

### Install Allure reporting

`pip install allure-behave`

### Generate Allure report

`behave --no-capture -f allure_behave.formatter:AllureFormatter -o filepath`

### Install Allure command line on Ubuntu
```
# Download the tar file
wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

# Unzip the folder
tar -xvf allure-commandline

# Copy the bin folder path
cp -r allure-commandline/bin /path/to/allure

# Navigate to home folder
cd ~

# Open .bashrc file
nano .bashrc

# At the bottom of the file, add
export PATH=$PATH:/path/to/allure

# Save and exit

# Reload bashrc
source .bashrc
```

### Upload the Allure report online

```
# Navigate to the allure json folder
cd allure-results

# Make sure the folder name is allure-results

# Open terminal outside the allure-results folder

# Generate html files
allure generate

# A folder named allure-report will be created

# Login to netlify app and upload the allure-report folder
```



