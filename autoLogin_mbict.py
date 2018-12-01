'''import webbrowser as wb
import requests as rq
import bs4

wb.open('http://10.0.0.1:8090/')
res = rq.get('http://10.0.0.1:8090/httpclient.html')
soup = bs4.BeautifulSoup(res.text,'html.parser')
containers = soup.findAll('div',{'class':'tablecss'})
containers[0].input['readonly'] = 'U6007053'
'''


from selenium import webdriver
br = webdriver.Chrome()
br.get('http://10.0.0.1:8090/httpclient.html')
br.find_element_by_name('username').send_keys('U6007053')
br.find_element_by_name('password').send_keys('qazdisha')
br.find_element_by_name('btnSubmit').click()

def main():
    if 
 

