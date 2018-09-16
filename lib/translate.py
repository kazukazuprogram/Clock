#!/usr/bin/env python3
#coding: utf-8

from requests import Session
from json import loads, dump
from pprint import pprint
from os import name
from os.path import dirname, exists

#OSの種類によって文字コードを変える
if name == 'nt':
    enc = 'utf-8'
else:
    enc = 'cp932'

def translate(session, string, lang):
    url = "https://script.google.com/macros/s/AKfycbw5E8Fm0y1kdXCJ8zOcd6dKDeX4r1hmcg-x1P0aAq_q8VXVaVU/exec?text="+string+"&source=en&target="+lang.split('_')[0]
    g = session.get(url)
    return g.content.decode()

def get_element(path):
    with open(path, encoding=enc) as f:
        d = loads(f.read())
    return d

def run(lang='', p='lang/en.js', enc='utf8'):
    s = Session()
    d = get_element(path=p)
    # print(translate(s, 'AlwaysOnTop', 'ja'))
    da = dict()
    d = list(d)
    for x in range(len(d)):
        print('\rTranslation completed %s / %s'%(x, len(d)), end='')
        da[d[x]] = translate(s, d[x], lang)
    print('\rTranslation completed %s / %s' % (len(d), len(d)), end='')
    print('\nCompleted.')
    pprint(da)
    # save
    d = dirname(p)
    if len(d)==0:
        path = lang+'.js'
    else:
        path=d+'/'+lang+'.js'
    with open(p, encoding=enc) as f:
        caution = loads(f.read())['DelteFileCaution']
    if exists(path):
        if input(caution).lower() in ['yes', 'y']:
            with open(path+'', 'w', encoding='utf8') as f:
                dump(obj=da, fp=f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    run(lang='ja', p='..\\lang\\ja.js')
