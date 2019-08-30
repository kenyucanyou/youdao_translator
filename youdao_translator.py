
import re
import sys
import time
import random
import hashlib
import requests

class youdao():
    def __init__(self):
        self.headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                        'Referer': 'http://fanyi.youdao.com/',
                        'Cookie': 'OUTFOX_SEARCH_USER_ID=-481680322@10.169.0.83;'
                    }
        self.data = {
                        'i': None,
                        'from': 'AUTO',
                        'to': 'AUTO',
                        'smartresult': 'dict',
                        'client': 'fanyideskweb',
                        'salt': None,
                        'sign': None,
                        'ts': None,
                        'bv': None,
                        'doctype': 'json',
                        'version': '2.1',
                        'keyfrom': 'fanyi.web',
                        'action': 'FY_BY_REALTlME'
                    }
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    def translate(self, word):
        ts = str(int(time.time()*10000))
        salt = ts + str(int(random.random()*10))
        sign = 'fanyideskweb' + word + salt + '97_3(jkMYg@T[KZQmqjTK'
        sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
        bv = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        bv = hashlib.md5(bv.encode('utf-8')).hexdigest()
        self.data['i'] = word
        self.data['salt'] = salt
        self.data['sign'] = sign
        self.data['ts'] = ts
        self.data['bv'] = bv
        res = requests.post(self.url, headers=self.headers, data=self.data)
        aa = [res.json()['translateResult'][0][0].get('tgt')]
        print(aa)
        
yd = youdao()
word = input("请输入你要翻译的文字：")
yd.translate(word)
