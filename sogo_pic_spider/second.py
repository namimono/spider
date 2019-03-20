import urllib.request
from fake_useragent import UserAgent
import re
import time
import  urllib.error

ua=UserAgent()
start='0'
for x in range(3):
    urltest0="http://pic.sogou.com/pics?query=%CE%D2%B5%C4%C7%E0%B4%BA%C1%B5%B0%AE%CE%EF%D3%EF&policyType=1&mode=1&start="+start+"&reqType=ajax&reqFrom=result&tn=0"
    urltest='http://pic.sogou.com/pics?query=%D3%C9%B1%C8%B1%F5%BD%E1%D2%C2&policyType=1&mode=1&start='+start+'&reqType=ajax&reqFrom=result&tn=0'
    # urltest2='http://www.baidu.com'
    #设置代理ip
    handlers=urllib.request.ProxyHandler({'http':'140.143.105.246:80'})
    #设置头信息，伪装为浏览器
    headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
    #创建request
    req=urllib.request.Request(urltest0)
    #创建opener，并给opener添加信息
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    #加载opener
    urllib.request.install_opener(opener)

    data=urllib.request.urlopen(req).read()
    data=str(data)
    result=re.compile('\"pic_url\":\"http://.+?\"').findall(data)

    index = re.search('\"startIndex\":\d*,\"', data)
    index = re.search("[0-9]+", index[0])
    start = str(int(index[0]) + 48)
    print(start)
    # 以上操作爬取搜狗图片网页的所有图片url
    for i in range(len(result)):

        pic_name=str(i)+"_"+str(x)+".jpeg"
        pic_name='chunwu\\'+pic_name
        result2=re.search('http://.*?jpg|http://.*?jpeg|http://.*?png',result[i])

        try:
            print("%d:%s"%(i,result2[0]))
            urllib.request.urlretrieve(result2[0],filename=pic_name)
            time.sleep(1)
        except urllib.error.URLError as e:
            print(e)
            i+=1
        except Exception as e:
            print(e)
            i+=1
# file=open('1.html','wb')
# file.write(data)
# file.close()
