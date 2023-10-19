import json
import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import pyperclip
import os
import platform


def button_click(driver, path):
  # path 代表需等待出现的元素路径
  try :
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, path))).click()
  except Exception as e:
      pass


def input_box(driver,input_path, input_content):
    driver.find_element(
        By.XPATH, input_path).clear()
    time.sleep(1)
    # print(platform.system())
    if platform.system() == "Darwin" :
        driver.find_element(
            By.XPATH, input_path).send_keys(Keys.CONTROL, 'a')
        driver.find_element(
            By.XPATH, input_path).send_keys(Keys.BACKSPACE)
    else :
        driver.find_element(
        By.XPATH, input_path).send_keys(Keys.COMMAND, 'a')
        driver.find_element(
            By.XPATH, input_path).send_keys(Keys.BACKSPACE)
    driver.find_element(
        By.XPATH, input_path).send_keys(input_content)


def box_select(driver, arrow_path, select_path, RangeNum):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, arrow_path))).click()
    except Exception as e:
        # 点击空白部分
        button_click(driver, '//*[@id="root"]/div/div[1]/div/div[1]')
    # 选择下拉选框中的元素
    selectNum = random.randint(1, RangeNum)
    # print(selectNum)
    xpath = select_path + '/div[' + str(selectNum) + ']'
    
    # 点击选框列表
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, xpath))).click()
    except Exception as e:
        # 点击空白部分
        button_click(driver, '//*[@id="root"]/div/div[1]/div/div[1]')


def date_picker(driver,date_path, param):

    driver.find_element(By.XPATH, date_path).send_keys(param)


def upload_file(driver, input_path, file_path):
    # Ant Design是一个复杂组合组件，需要找到隐藏的基础组件
    try:
        file_input = driver.find_element(By.XPATH, input_path)
        file_input.send_keys(file_path)
    except Exception as e:
        # 点击空白部分
        button_click(driver, '//*[@id="root"]/div/div[1]/div/div[1]')
