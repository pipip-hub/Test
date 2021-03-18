import requests
def gettext(url):
    r = requests.get(url,timeout=30)
    r.encoding = 'apparent_encoding'
    return r.text

url = 'https://www.baidu.com'
name = 'test1.txt'

print(gettext(url),file=open(name,'x',encoding='utf-8'))
