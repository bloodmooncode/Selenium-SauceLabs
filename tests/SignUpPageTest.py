import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from components import button_click, input_box, box_select, date_picker, upload_file
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOption

# driver = get_webdriver('edge')
# driver.maximize_window()

emailNum = "650516npu@gmail.com"
password = "123456"

options = EdgeOption()
# driver = webdriver.Edge(options=options)
sauce_options = {}
sauce_options['username'] = 'AUV-ZYP'
sauce_options['accessKey'] = '093f748f-5860-443a-b183-e9cb1d9d0965'
sauce_options['build'] = 'selenium-build-U43CY'
sauce_options['name'] = 'bstackdemo-test'
options.set_capability('sauce:options', sauce_options)

url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=url, options=options)


def click_to_signup():
    # 虽然链接注册页但是会转入登录页
    driver.get('https://test-console.mnd.infothinker.com/signup/sendEmail')
    # 点击注册按钮跳转
    button_click(driver, '//*[@id="root"]/div/div[2]/h2[1]/span')
    # 如果出现Create your Mainnet Digital account，则跳转成功
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div[2]/h1'), 'Create your Mainnet Digital account')
    )

    # 输入邮箱
    input_box(driver, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/input', emailNum)
    # 输入密码
    input_box(driver, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/span/input',password)
    # 验证密码
    input_box(driver, '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/span/input', password)
    # 点击注册
    button_click(driver, '//*[@id="root"]/div/div[2]/button')

    
def click_to_login():
    driver.get('https://test-console.mnd.infothinker.com/login')
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div[2]/h1'), 'Welcome to Mainnet Digital, Sign in to Continue.')
    )
    # 输入邮箱
    input_box(driver, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/input', emailNum)
    # 输入密码
    input_box(driver, '//*[@id="password"]', password)
    # 点击登录
    button_click(driver, '//*[@id="root"]/div/div[2]/button')
    

def country_info_page():
    # 直到页面加载出来才开始操作
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/h1'), 'Country information')
        )
    except Exception as e:
        pass

    # 上方左侧选框
    box_select(driver, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div',
               '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 5)

    # 上方右侧选框
    box_select(driver, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div',
               '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div', 5)

    # 下方左侧选框
    box_select(driver, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div',
               '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div', 5)

    # 单一点选
    button_click(driver, '/html/body/div[1]/div/div[2]/div[1]/div[3]')

    # next button
    button_click(driver, '/html/body/div[1]/div/div[2]/div[2]/button')


def personal_info_page():
    # 直到页面加载出来才开始操作
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/h1'), 'Personal information')
        )
    except Exception as e:
        pass   
    # 输入框
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/input', 'AUV')
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[3]/div/div[1]/input', 'AUV')
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input', 'AUV')

    # 日期选择
    date_picker(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div/input', '2023-10-06')

    # 性别选择
    box_select(
        driver, '/html/body/div[1]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div', '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div', 3)

    # 工作状态选择
    box_select(
        driver, '/html/body/div[1]/div/div[2]/div[1]/div[3]/div[3]/div/div/div/div', '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 4)
    # next button
    button_click(driver, '//*[@id="root"]/div/div[2]/div[2]/button[2]')


def residential_address_page():
    # 直到页面加载出来才开始操作
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/h1'), 'Residential address')
        )
    except Exception as e:
        pass

    # 输入街道
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div[1]/input', '123456')
    # 输入单元号
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[1]/input', '123456')
    # 输入邮编
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]/input', '123456')
    # 输入城市
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[3]/div/div[1]/input', '123456')
    # 输入洲
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[4]/div[1]/div/div[1]/input', '123456')
    # 输入国家
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[4]/div[3]/div/div[1]/input', '123456')
    # next button
    button_click(driver, '//*[@id="root"]/div/div[2]/div[2]/button[2]')


def contact_info_page():
    # 直到页面加载出来才开始操作
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/h1'), 'Contact information')
        )
    except Exception as e:
        pass

    # 输入国家代码
    box_select(driver, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]',
               '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 5)
    # 输入电话号码
    input_box(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/input', '123456')
    # next button
    button_click(driver, '//*[@id="root"]/div/div[2]/div[2]/button[2]')


def investment_info_page():
    # 直到页面加载出来才开始操作
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/h1'), 'Investment information')
        )
    except Exception as e:
        pass
    # 选择交易种类
    box_select(driver, '//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div',
               '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 4)
    # next button
    button_click(driver, '//*[@id="root"]/div/div[2]/div[2]/button[2]')


def asset_info_page():
    # 直到页面加载出来才开始操作
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/h1'), 'Asset information')
        )
    except Exception as e:
        pass

    # 选择交易总额
    box_select(driver, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div',
               '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 3)
    # 选择年度收益
    box_select(driver, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div',
               '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div', 4)
    # 选择收入来源
    box_select(driver, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div',
               '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div', 4)
    # 选择收入类型
    box_select(driver, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div',
               '/html/body/div[5]/div/div/div/div[2]/div[1]/div/div', 4)
    # next button
    button_click(driver, '//*[@id="root"]/div/div[2]/div[2]/button[2]')


def document_page():
    # 直到页面加载出来才开始操作
    try:
        WebDriverWait(driver, 10).until(  
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/h1'), 'Identification documents')
        )
    except Exception as e:
        pass

    # 左侧上传文件
    upload_file(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div/div/span/div[1]/span/input',
        'https://dropovercl.s3.amazonaws.com/985408bd-2262-490c-bb9d-9b965ba20193/9da2ca69-dcb7-4d94-a3ca-d9a40eba7c74/9708dd27-9215-406f-9a85-9044c9ca2207.png'
    )
    # 右侧上传文件
    upload_file(
        driver, '//*[@id="root"]/div/div[2]/div[1]/div/div[3]/div/div/span/div[1]/span/input',
        'https://dropovercl.s3.amazonaws.com/985408bd-2262-490c-bb9d-9b965ba20193/9da2ca69-dcb7-4d94-a3ca-d9a40eba7c74/9708dd27-9215-406f-9a85-9044c9ca2207.png'
    )    
    # next button
    button_click (driver, '//*[@id="root"]/div/div[2]/div[2]/button[2]')
          

def SignUp_Process_Control():
    
    click_to_signup()
    click_to_login()
    country_info_page()
    personal_info_page()
    residential_address_page()
    contact_info_page()
    investment_info_page()
    asset_info_page()
    document_page()

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    SignUp_Process_Control()



