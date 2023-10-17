import time
from selenium import webdriver

# 启动浏览器
driver = webdriver.Edge()

# 访问被测试网页
driver.get('https://test-console.mnd.infothinker.com/vault')

# 强制等待
time.sleep(5)
# 关闭驱动，回收资源
driver.quit()

# 关闭界面
driver.close()