from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://search.jd.com/Search?keyword=%E5%A5%B6%E7%B2%89&enc=utf-8&suggest=2.def.0.V19&wq=naifen&pvid=c470db8c19d14abbb93c76c10686da9d')
browser.execute_script("window.scrollBy(0,3000)")
time.sleep(1)
browser.execute_script("window.scrollBy(0,5000)")
time.sleep(1)
browser.execute_script("window.scrollBy(0,8000)")
time.sleep(1)
a=browser.page_source
print(a)