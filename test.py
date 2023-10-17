from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.browser_version = 'latest'
options.platform_name = 'Windows 11'
sauce_options = {}
sauce_options['username'] = 'ZYP'
sauce_options['accessKey'] = '92a1c3b7-cc8b-429f-9d25-e7b8d3ad976c'
sauce_options['build'] = 'selenium-build-7VYG5'
sauce_options['name'] = '<your test name>'
options.set_capability('sauce:options', sauce_options)

url = "https://bstackdemo.com/"
driver = webdriver.Remote(command_executor=url, options=options)