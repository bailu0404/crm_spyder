#encoding:UTF-8

import urllib.request

#print(urllib.request)

url = "http://home.nanjing.fang.com/zhuangxiu/DealerList_192_0_0_0_0_3_0_1_/"
httpHandler = urllib.request.HTTPHandler(debuglevel=1)
httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httpHandler, httpsHandler)
urllib.request.install_opener(opener)

try:
    data = urllib.request.urlopen(url, timeout=5).read()
    #data = data.decode("utf-8")
    print(data)
except urllib.error.HTTPError as e:
    print("Caught YOU")
    print(e.reason)
except urllib.error.URLError as e:
    print("Caught YOU TOO")
    print(e.reason)
    
'''
file = open("trial.html", "wb")
file.write(data)
file.close()
'''
