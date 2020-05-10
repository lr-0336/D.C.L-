import pypinyin #汉语转拼音模块
import urllib.request 
import urllib.parse
import json
import re

def spider(word):#网上爬取

    try:

        url = 'https://fanyi.baidu.com/sug' #资源地址
        data = {} #得到的数据的容器
        data['kw'] = word

        data = urllib.parse.urlencode(data).encode('utf-8') #获取数据并转码
        req = urllib.request.Request(url,data,headers) 

        response = urllib.request.urlopen(req) #提取出需要的字符串并做成表格
        html = response.read().decode('utf-8')
        terget = json.loads(html)['data'][0]['v']
        terget = terget.replace('[','').split(']')[0]

        return terget
    except Exception:
        return word

def modular(word):#模块转换
    
    target = ''.join((pypinyin.pinyin(word))[0])#将结果转换为字符串

    return target

def trans(word):

    try:

        word = modular(word)

        return word

    except Exception:#如果模块出错，就网上爬取

        word = spider(word)

        return word


if __name__ == '__main__': #测试
    while True:
        word = input('输入：')
        print (trans(word))
