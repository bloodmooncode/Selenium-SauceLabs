import time
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
import pytest

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