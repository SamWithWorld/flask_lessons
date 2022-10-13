# !/usr/local/bin python3
# coding: utf-8
# @FileName  :translate.py.py
# @Time      :2022-10-12 21:03
# @Author    :Sam

import json, random, hashlib, http.client
from flask_babel import _
from app import app
from urllib import parse
import config


def translate(q, fromLang, toLang):
    if not config.Config.BD_TRANSLATOR_APPID:
        return _('Error:the translation service is not configured.')
    if not config.Config.BD_TRANSLATOR_KEY:
        return _('Error:the translation service is not configured.')
    appid = config.Config.BD_TRANSLATOR_APPID
    secretKey = config.Config.BD_TRANSLATOR_KEY

    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)

    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        print("myurl:",myurl)

        response = httpClient.getresponse()  # response是HTTPResponse对象
        r = response.read().decode('utf-8')
        d = json.loads(r)
        print('翻译结果:', d)

        l = d['trans_result']
        l1 = l[0]['dst']

        return (l1)
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
