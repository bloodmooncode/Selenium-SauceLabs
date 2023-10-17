from webdriver_helper import get_webdriver
import time

driver = get_webdriver('edge')

# 访问被测试网页
driver.get('https://test-console.mnd.infothinker.com/vault')

# 强制等待
time.sleep(5)
# 关闭驱动，回收资源
driver.quit()
