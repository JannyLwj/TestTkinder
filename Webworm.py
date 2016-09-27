#encoding:UTF-8
import urllib
import urllib.request
import urllib.parse
import http.cookiejar

def open_url():
    values = {}
    values['username'] = "cjkx38"
    values['password'] = "Newpassword48"
    data = urllib.parse.urlencode(values)
    binary_data = data.encode(encoding='UTF8')
    url = "http://sds12.comm.mot.com/LicensingTools/llt/index.cfm?operator=CreateEntitlement"
    request = urllib.request.Request(url,binary_data)
    try:
        response = urllib.request.urlopen(request)
    except urllib.request.URLError as e:
        print(e.reason)
    print(response.read())

def test():
    req = urllib.request.Request('http://blog.csdn.net/cqcre')
    try:
        urllib.request.urlopen(req)
    except urllib.request.HTTPError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        else:
            print('OK')

def test_cookie():
       # 声明一个CookieJar对象实例来保存cookie
    cookie = http.cookiejar.CookieJar()
    # 利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib.request.build_opener(handler)
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print('Name = ' + item.name)
        print('Value = ' + item.value)

    filename = "D:\cookie.txt"
    cookie1=http.cookiejar.MozillaCookieJar(filename)
    handler1=urllib.request.HTTPCookieProcessor(cookie1)
    opener=urllib.request.build_opener(handler1)
    response= opener.open('http://www.baidu.com')
    cookie1.save(ignore_discard=True, ignore_expires=True)  # 创建MozillaCookieJar实例对象

def test_readfromcookie():
    cookie = http.cookiejar.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load("D:\cookie.txt", ignore_discard=True, ignore_expires=True)
    # 创建请求的request
    req = urllib.request.Request("http://www.baidu.com")
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print(response.read())

if __name__=='__main__':
    test_readfromcookie()

