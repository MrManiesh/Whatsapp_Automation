from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\\Users\\admin\\Desktop\\chromedriver.exe"   #path to chromedriver in your computer 
bot = webdriver.Chrome(PATH)
Name = "Second Number"  #Name of Chat or Group
bot.get('https://web.whatsapp.com/')

time.sleep(10)  

person = bot.find_element_by_xpath("//span[@title = '{}']".format(Name))

person.click()

msg_box = bot.find_element_by_class_name('_3uMse')

time.sleep(5)
for i in range(100):  #number of msg
    a="msg {} of 100".format(i+1) #message
    msg_box.send_keys(a)
    time.sleep(1)
    msg_box.send_keys(Keys.RETURN)
    time.sleep(1)
