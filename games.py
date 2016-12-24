from selenium import webdriver
from urllib.request import urlopen

url = 'http://www.nashuanorthathletics.com/main/teamschedule/id/3695990/seasonid/4115615'
file_name = './test.txt'

conn = urlopen(url)
data = conn.read()
conn.close()

file = open(file_name, 'wb')
file.write(data)
file.close()

browser = webdriver.Firefox()
browser.get('file:///'+file_name)
html = browser.page_source
browser.quit()