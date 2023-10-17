import random
import time
from webdriver_helper import get_webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.keys import Keys
# from define_value import driver, emailNum, password


driver = get_webdriver('edge')
driver.maximize_window()
emailNum = "moonfunjohn@gmail.com"
password = "123456"


def click_to_login():
    driver.get('https://test-console.mnd.infothinker.com/login')
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/input').send_keys(emailNum)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/button').click()
    time.sleep(5)


def click_to_transferPage():
    # 点击进入转账界面
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/section/aside/div/div[2]/ul/li[6]/span/a').click()
    time.sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/section/div[2]/main/div/div[1]/button').click()
    time.sleep(2)


def box_select(arrow_path, select_path, num):

    driver.find_element(
        By.XPATH, arrow_path).click()
    time.sleep(5)

    selectNum = num
    # print(selectNum)
    xpath = select_path + '/div[' + str(selectNum) + ']'
    # 点击选框列表
    try:
        # print(xpath)
        driver.find_element(
            By.XPATH, xpath).click()
    except NoSuchElementException or ElementNotInteractableException or InvalidSelectorException as e:
        # 点击空白部分
        single_select('/html/body/div[2]/div/div[2]/div/div[2]')

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


def choose_Asset(num):
    # 选择虚拟币种
    box_select('/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div',
               '/html/body/div[3]/div/div/div/div[2]/div/div', num)


def input_Value(value):
    # 输入转账金额
    input_box(
        '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div[1]/div/input', value)
    # 判断转账金额是否超过账户所有值
    ValueString = driver.find_element(
        By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[4]/h2[1]').text
    # print(ValueString)
    return ValueString


def transfer_Page():
    choose_Asset(1)

    whitelistString = driver.find_element(
        By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[6]/div/div/h1').text
    if whitelistString == '白名单为空 - 将您的地址添加到白名单':
        choose_Asset(4)
    ans = input_Value(0.26)
    # print(ans)
    # 如果白名单为空，切换币种

    # 如果有这个币种存款不够，会报出Insufficient balance错误，点击Max按钮
    if ans == '余额不足.':
        single_select('/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/h1')
    # ValueMax = ans.split(' ')[1]
    # print(float(ValueMax))

    time.sleep(10)
    # 转账速度选择
    num = random.randint(1, 4)
    print('num = ', num)
    box_select(
        '/html/body/div[2]/div/div[2]/div/div[2]/div/div[5]/div/div[2]',
        '/html/body/div[5]/div/div/div/div[2]/div/div', num)
    # 输入remark
    input_box(
        '/html/body/div[2]/div/div[2]/div/div[2]/div/div[7]/div/input', 'Something')
    # 如果有这个币种存款足够，点击转账
    single_select('/html/body/div[2]/div/div[2]/div/div[2]/div/button')
    # 页面跳转时间
    single_select('/html/body/div[2]/div/div[2]/div/div[2]/div/button[1]')


def Transfer_Process_Control():
    click_to_login()
    click_to_transferPage()
    transfer_Page()

    time.sleep(5)
    # 关闭驱动，回收资源
    driver.quit()


# 主函数
if __name__ == "__main__":
    Transfer_Process_Control()
