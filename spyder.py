#encoding:UTF-8

import urllib.request

print(urllib.request)

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
#data = data.decode("utf-8")
print(type(data))

file = open("trial.html", "wb")
file.write(data)
file.close()

print(data)
