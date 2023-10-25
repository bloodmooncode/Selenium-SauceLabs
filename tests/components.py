import json
import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
    # 点击空白部分
    button_click(driver, '//*[@id="root"]/div/div[1]/div/div[1]')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, path))).click()
    pass


def input_box(driver,input_path, input_content):
    driver.find_element(
        By.XPATH, input_path).clear()
    time.sleep(1)
    # print(platform.system())
    while driver.find_element(
            By.XPATH, input_path).get_attribute("value"):
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


# 判断当前使用的是什么浏览器
def get_browser_name(driver):
    if isinstance(driver, webdriver.Chrome):
        return "Chrome"
    elif isinstance(driver, webdriver.Firefox):
        return "Firefox"
    elif isinstance(driver, webdriver.Edge):
        return "Edge"
    elif isinstance(driver, webdriver.Safari):
        return "Safari"
    elif isinstance(driver, webdriver.Ie):
        return "Internet Explorer"
    else:
        return "Unknown"


def download_file(driver, browser_option, url) :
    # 获取当前文件上两级绝对路径
    up_path = os.path.dirname(os.path.realpath(__file__))
    up_up_path= os.path.dirname(up_path)
    # 指定下载的默认文件夹, 区分Mac，win，linux系统
    if platform.system() == "Darwin" :
        prefs = {
            "download.default_directory": up_up_path + '/assets',  # 下载存放目标文件夹
            "download.prompt_for_download": False,  # 不提示下载对话框
        }
    elif platform.system() == "Windows":
        prefs = {
            "download.default_directory": up_up_path + "\\assets",  # 下载存放目标文件夹
            "download.prompt_for_download": False,  # 不提示下载对话框
        }
    else :
        pass
    browser_option.add_experimental_option("prefs", prefs)
    driver.get(url)
    time.sleep(10)  # 等待下载完成


def upload_file(driver, input_path, file_path, verify_path):
    # Ant Design是一个复杂组合组件，需要找到隐藏的基础组件
    try:
        file_input = driver.find_element(By.XPATH, input_path)
        file_input.send_keys(file_path)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, verify_path)))
    except Exception as e:
        # 点击空白部分
        print('upload fail')
        button_click(driver, '//*[@id="root"]/div/div[1]/div/div[1]')