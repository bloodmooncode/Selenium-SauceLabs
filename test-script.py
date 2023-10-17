import json
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_helper import get_webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.keys import Keys

driver = get_webdriver('edge')

executor_object = {
    'action': 'setSessionName',
    'arguments': {
        'name': "<test-name>"
    }
}
browserstack_executor = 'browserstack_executor: {}'.format(
    json.dumps(executor_object))
driver.execute_script(browserstack_executor)
