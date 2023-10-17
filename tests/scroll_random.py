from webdriver_helper import get_webdriver
import time
from selenium.webdriver.common.by import By
import random


driver = get_webdriver('edge')
driver.maximize_window()
emailNum = "650516npu@gmail.com"
password = "123456"

'''/html/body/div[6]/div/div/div/div[2]/div[1]/div/div 上方左侧
/html/body/div[5]/div/div/div/div[2]/div[1]/div/div 上方右侧
/html/body/div[4]/div/div/div/div[2]/div[1]/div/div 下方左侧'''

# 点击上方左侧显示下拉箭头
driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/span').click()
# 选择下拉选框中的元素
box = driver.find_element(
    By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div')
# 前端每次显示5个div,依靠transform: translateY(56 * （0 ～192）px)实现选框切换
num = 56 * random.randint(0, 192)
js = 'transform: translateY(' + str(num) + ')px'
# 改变translateY
driver.execute_script(js, box)
# 随机选取选框列
selectNum = random.randint(0, 4)
xpath = '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[' + \
    str(selectNum) + ']'
# 点击选框列表
driver.find_element(By.XPATH, xpath).click()
