#爬获校花网
# 请求库：requests, selenium（可以驱动浏览器解析渲染CSS和JS，但有性能劣势（有用没用的网页都会加载）；）
# 解析库：正则，beautifulsoup，pyquery
# 存储库：文件，MySQL，Mongodb，Redis


import re
import requests

respose=requests.get('http://www.xiaohuar.com/v/')
# print(respose.status_code)# 响应的状态码
# print(respose.content)  #返回字节信息
# print(respose.text)  #返回文本内容
urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
url=urls[5]
result=requests.get(url)
mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]

video=requests.get(mp4_url)

with open('/Users/admin/Desktop/test/m.mp4','wb') as f:
    f.write(video.content)