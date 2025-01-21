# 本地Chrome浏览器的静默模式设置：
from selenium import  webdriver #从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行












# 本地Chrome浏览器设置方法
from selenium import webdriver #从selenium库中调用webdriver模块
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器

import time

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('Wufeng')
time.sleep(4)
assistant = driver.find_element_by_id('assistant')
assistant.send_keys('77')
time.sleep(4)
button = driver.find_element_by_class_name('sub')
button.click()

time.sleep(5)
driver.close()










from selenium import  webdriver # 从selenium模块中调用webdriver模块
driver = webdriver.Chrome()
import time

driver = webdriver.Chrome() # 声明浏览器为本地的Chrome
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php') # 访问页面
time.sleep(1) # 暂停两秒，等待浏览器缓冲

username = driver.find_element_by_id('user_login') # 定位到输入用户名的位置
username.send_keys('spiderman') # 输入用户名
password = driver.find_element_by_id('user_pass') # 定位到输入密码的位置
password.send_keys('crawler334566') # 输入密码
login = driver.find_element_by_id('wp-submit') # 定位到登录按钮的位置
login.click() # 点击登录
time.sleep(2) # 等待两秒

article = driver.find_element_by_partial_link_text('三') # 根据链接的部分文字"三"，定位到这个链接
article.click() # 点击链接
time.sleep(1) # 等待一秒
comment = driver.find_element_by_id('comment') # 定位到评论区
comment.send_keys('蜘蛛侠的selenium评论') # 输入评论内容，随意发挥你的创意，记得带上selenium就行
submit = driver.find_element_by_id('submit') # 定位到"发表评论"的按钮
submit.click() # 点击“发表评论”按钮
driver.close()

