import requests
import random
import time
from webdriver_helper import get_webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import pyperclip
import os
from define_value import driver, emailNum, password

# driver = get_webdriver('edge')
# driver.maximize_window()
# emailNum = "650516npu@gmail.com"
# password = "123456"


def open_SignUpPage():
    # 虽然链接注册页但是会转入注册页
    driver.get('https://test-console.mnd.infothinker.com/signup/sendEmail')
    # 跳转到注册页面
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/h2[1]/span').click()
    time.sleep(5)


def click_to_SignUp():
    # 输入邮箱
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/input').send_keys(emailNum)
    # 输入密码
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/span/input').send_keys(password)
    # 验证密码
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/span/input').send_keys(password)
    # 点击注册
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/button').click()


def click_to_login():
    driver.get('https://test-console.mnd.infothinker.com/login')
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/input').send_keys(emailNum)
    driver.find_element(
        By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/button').click()


def json_Judge():
    # 得到注册邮箱响应体
    URLlink = "https://apitest.mainnetdigital.com/api/users?filters%5Bemail%5D=" + \
        emailNum.replace("@", "%40")
    # print("emailNum" + emailNum.replace("@", "%40"))

    # 解析响应体
    response = requests.get(URLlink)
    data = response.json()
    # print(data[0])

    # 如果是新用户
    if (data[0]["confirmed"] == False):
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div/button').click()
        time.sleep(2)

        # 跳转到登录页继续输入
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/input').clear()
        driver.find_element(By.XPATH, '//*[@id="password"]').clear()

        # 邮箱验证

        # 点击登录
        click_to_login()
        time.sleep(5)

# 如果是老用户
    else:
        click_to_login()
        time.sleep(5)


def box_select(arrow_path, select_path, RangeNum):

    driver.find_element(
        By.XPATH, arrow_path).click()
    time.sleep(5)
    # 选择下拉选框中的元素
    # box = driver.find_element(By.XPATH, select_path)

    # 前端每次显示5个div,依靠transform: translateY(56 * （0 ～192）px)实现选框切换

    # num = 56 * random.randint(0, 192)
    # js = "arguments[0].style = 'transform: translateY(%dpx); position: absolute; left: 0px; right: 0px; top: 0px;';" % (
    #     num)

    # # 改变translateY
    # driver.execute_script(js, box)
    # 随机选取选框列
    num = 0
    selectNum = random.randint(1, RangeNum)
    # print(selectNum)
    xpath = select_path + '/div[' + str(selectNum) + ']'
    # 点击选框列表
    try:
        driver.find_element(
            By.XPATH, xpath).click()
    except NoSuchElementException or ElementNotInteractableException as e:
        # 点击空白部分
        single_select('//*[@id="root"]/div/div[1]/div/div[1]')

    time.sleep(2)


def single_select(single_path):
    # 单一选择器
    driver.find_element(
        By.XPATH, single_path).click()
    time.sleep(2)


def input_box(input_path, input_content):
    # 全选后再输入 Command for mac/Ctrl for win
    driver.find_element(
        By.XPATH, input_path).send_keys(Keys.COMMAND, 'a')
    driver.find_element(
        By.XPATH, input_path).send_keys(input_content)
    time.sleep(2)


def date_picker(date_path, param):
    driver.find_element(By.XPATH, date_path).send_keys(param)


def upload_file(file):
    # 创建鼠标对宴
    k = PyKeyboard()
    # 创建键盘对象
    m = PyMouse()
    filepath = "/"
    # 模拟快捷键Command+Shift+G
    k.press_keys(["Command", "Shift", "G"])
    # 输入文件路径
    x_dim, y_dim = m.screen_size()
    m.click(x_dim // 2, y_dim // 2, 1)
    # 复制文件路径开头的斜杠
    pyperclip.copy(filepath)
    # 粘贴斜杠
    k.press_keys(["Command", "V"])
    time.sleep(2)
    # 获取当前文件上一级绝对路径
    up_path = os.path.dirname(os.path.realpath(__file__))
    # 输入文件全路径进去
    k.type_string(up_path + file)
    k.press_key("Return")
    time.sleep(2)
    k.press_key("Return")
    time.sleep(2)


def CountryInfo_Page():
    # 上方左侧选框
    box_select('/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div',
               '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 5)

    # 上方右侧选框
    box_select('/html/body/div[1]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div',
               '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div', 5)

    # 下方左侧选框
    box_select('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div',
               '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div', 5)

    # 单一点选
    single_select('/html/body/div[1]/div/div[2]/div[1]/div[3]')

    # next button
    single_select('/html/body/div[1]/div/div[2]/div[2]/button')

    time.sleep(5)


def PersonalInfo_Page():
    # 输入框
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/input', 'AUV')
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[3]/div/div[1]/input', 'AUV')
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input', 'AUV')

    # 日期选择
    date_picker(
        '//*[@id="root"]/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div/input', '2023-10-06')

    # 性别选择
    box_select(
        '/html/body/div[1]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div', '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div', 3)

    # 工作状态选择
    box_select(
        '/html/body/div[1]/div/div[2]/div[1]/div[3]/div[3]/div/div/div/div', '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 4)
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')

    time.sleep(5)


def residentialAddress_Page():
    # 输入街道
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div[1]/input', '123456')
    # 输入单元号
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[1]/input', '123456')
    # 输入邮编
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]/input', '123456')
    # 输入城市
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[3]/div/div[1]/input', '123456')
    # 输入洲
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[4]/div[1]/div/div[1]/input', '123456')
    # 输入国家
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[4]/div[3]/div/div[1]/input', '123456')
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(5)


def ContactInfo_Page():
    # 输入国家代码
    box_select('//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]',
               '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 5)
    # 输入电话号码
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/input', '123456')
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(5)


def Investment_Info_Page():
    # 选择交易种类
    box_select('//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div',
               '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 4)
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(5)


def AssetInfo_Page():
    # 选择交易总额
    box_select('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div',
               '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 3)
    # 选择年度收益
    box_select('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div',
               '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div', 4)
    # 选择收入来源
    box_select('//*[@id="root"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div',
               '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div', 4)
    # 选择收入类型
    box_select('//*[@id="root"]/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div',
               '/html/body/div[5]/div/div/div/div[2]/div[1]/div/div', 4)
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(5)


def Document_page():
    # 点击触发上传
    single_select(
        '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div/div/span/div[1]/span/div/div')
    time.sleep(3)
    # 上传文件
    try:
        upload_file("/assets/logo.png")
    except NoSuchElementException or ElementNotInteractableException as e:
        single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(10)
    # 上传右边照片
    single_select(
        '//*[@id="root"]/div/div[2]/div[1]/div/div[3]/div/div/span/div[1]/span/div/div')
    time.sleep(3)
    try:
        upload_file("/assets/logo.png")
    except NoSuchElementException or ElementNotInteractableException as e:
        single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(10)
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(5)


def OtherDoc_Page():
    single_select(
        '//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/span/div[1]/span/div/div')
    time.sleep(3)
    try:
        upload_file("/assets/logo.png")
    except NoSuchElementException or ElementNotInteractableException as e:
        pass
    time.sleep(10)
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(10)


def Account_Page():
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/textarea', '123456')
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(10)


def Disclaim_Page():
    single_select('//*[@id="root"]/div/div[2]/div[1]/div[2]/div')
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(5)


def Agreement_Page():
    single_select('//*[@id="root"]/div/div[2]/div[1]/div[2]/div')
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(5)


def FaceDetect_Page():
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(5)


def Generate_Page():
    # 选择币种
    box_select('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div/div',
               '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div', 6)
    # 输入货币地址
    input_box(
        '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[1]/input', '123456')
    # next button
    single_select('//*[@id="root"]/div/div[2]/div[2]/button[2]')
    time.sleep(5)


baseURL = "https://apitest.mainnetdigital.com/api"


def acquire_permission():
    # 登录管理员权限
    post_url = baseURL + '/auth/local'
    params = {
        "identifier": "xiaoyu@mainnet.digital",
        "password": "123456"
    }

    response = requests.post(post_url, params)
    # 获取jwt_token
    data = response.json()
    token = data["jwt"]
    # print(token)
    return token


def KYC_approve():
    # 修改KYC认证状态
    token = acquire_permission()
    put_url = baseURL + '/users-permissions/status/181 '
    auth = 'Bearer ' + token
    # print(auth)
    headers = {'content-type': 'application/json',
               'Authorization': auth}
    body = {
        "action": "APPROVE"
    }
    result = requests.put(put_url, json=body, headers=headers)
    # print(result.json())
    time.sleep(5)


def KYC_Process_Control():
    open_SignUpPage()
    click_to_SignUp()
    json_Judge()
    CountryInfo_Page()
    PersonalInfo_Page()
    residentialAddress_Page()
    ContactInfo_Page()
    Investment_Info_Page()
    AssetInfo_Page()
    Document_page()
    OtherDoc_Page()
    Account_Page()
    Disclaim_Page()
    Agreement_Page()
    FaceDetect_Page()
    Generate_Page()

    acquire_permission()
    KYC_approve()
    time.sleep(10)
    click_to_login()

    time.sleep(5)
    # 关闭驱动，回收资源
    driver.quit()


# # 主函数
if __name__ == "__main__":
    KYC_Process_Control()
