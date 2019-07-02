
import requests
from bs4 import BeautifulSoup
import json
import time
import datetime
from config import *
import re


def get_html(url,data):
    '''
    :param url:请求的url地址
    :param data: 请求的参数
    :return: 返回网页的源码html
    '''
    response = requests.get(url,data)
    return response.text


def parse_html(html):
    '''
    :param html: 传入html源码
    :return: 通过yield生成一个生成器，存储爬取的每行信息
    '''
    soup = BeautifulSoup(html, 'html.parser')

    uls = soup.find_all("ul", attrs={"class": "easyui-tree"})
    for ul in uls:
        lis=ul.find_all('li')
        for li in lis:
            print(li)



def write_to_file(content):
    '''
    :param content:要写入文件的内容
    '''
    with open("result.txt",'a',encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")

def get_page_nums():
    '''
    :return:返回的是需要爬取的总页数
    '''
    base_url = "http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp?"
    date_time = datetime.date.fromtimestamp(time.time())
    data = {
        "pktrqks": date_time,
        "ktrqjs": date_time,
    }
    while True:
        html = get_html(base_url,data)
        soup = BeautifulSoup(html, 'lxml')
        if soup.body.text.strip() == "系统繁忙":
            print("系统繁忙，登录太频繁，ip被封锁")
            time.sleep(ERROR_SLEEP_TIME)
            continue
        else:
            break
    res = soup.find("div",attrs={"class":"meneame"})

    page_nums = res.find('strong').text
    #这里获得page_nums是一个爬取的总条数，每页是15条数据，通过下面方法获取总页数
    page_nums = int(page_nums)
    if page_nums %15 == 0:
        page_nums = page_nums//15
    else:
        page_nums = page_nums//15 + 1
    print("总页数：",page_nums)
    return page_nums

def autoLogin():
    base_url = "url"
    headers  = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Cookie":"account=admin; userId=dac0c8cd-26a0-4c3c-bc6e-5770ef5d8e87; userName=%e6%af%9b%e9%93%b6%e4%b8%9c; roleId=2b2d93cd-f3e5-4b18-9e16-4986369b846f; roleName=%e7%ae%a1%e7%90%86%e5%91%98; url=http%3a%2f%2f10.60.4.103%3a4001%2f; isAutoLogin=false",
            "Host":"10.60.4.103:8080",
            "Referer":"url",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    res = parse_html(response.text)
    for i in res:
        write_to_file(i)


def main():
    autoLogin()
    
if __name__ == '__main__':
    main()








