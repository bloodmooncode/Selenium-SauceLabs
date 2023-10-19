# SourceLab + Selenium

- [SourceLab + Selenium](#sourcelab--selenium)
  - [Set up the dependencies](#set-up-the-dependencies)
  - [Add config in Selenium script](#add-config-in-selenium-script)
  - [Move the test from Local to Remote](#move-the-test-from-local-to-remote)
  - [Code Example](#code-example)

## Set up the dependencies

Run the following command on your terminal/command-prompt to install the required dependencies.

For macOS or Linux

```bash
# create virtual environment
python3 -m venv env
source env/bin/activate
# install the required packages
pip3 install -r requirements.txt
```

For Windows

```bash
python3 -m venv env
env\Scripts\activate
pip3 install -r requirements.txt
```

## Add config in Selenium script

```python
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.browser_version = 'latest'
options.platform_name = 'Windows 11'
sauce_options = {}
sauce_options['username'] = '<User-name>'
sauce_options['accessKey'] = '<accessKey>'
sauce_options['build'] = '<Build ID>'
sauce_options['name'] = '<your test name>'
options.set_capability('sauce:options', sauce_options)
```

## Move the test from Local to Remote

```python
url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=url, options=options)
```

## Code Example

```python
import time
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver

options = EdgeOptions()
sauce_options = {}
sauce_options['username'] = 'AUV'
sauce_options['accessKey'] = '853569bb-0b61-4b91-b1f2-0a82a1c7274e'
sauce_options['build'] = 'selenium-build-7VYG5'
sauce_options['name'] = 'bstackdemo-test'
options.set_capability('sauce:options', sauce_options)

url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=url, options=options)
driver.get('https://bstackdemo.com/')

time.sleep(5)
driver.quit()
```
