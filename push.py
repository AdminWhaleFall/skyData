#! /usr/bin/python3
# 酷推推送模块 支持传入参数
import requests
import sys
# 酷推token
token = "92f83d0596c7b553ea1df9f242e4fc46"

status = sys.argv[1]
time = sys.argv[2]
log = sys.argv[3]

# print(status,time,log)
# sys.exit()

url = "https://push.xuthus.cc/send/%s" % (token)

if status == "True":
    content = "[SkyData] \n%s 自动提交skyCSV成功!\nGit信息:%s" % (time,log)
elif status == "False":
    content = "[SkyData] \n%s 自动提交skyCSV失败!错误信息:\n%s" % (time, log)
else:
    raise TypeError("参数有误")

data = "%s" % (content)
res = requests.post(url=url, data=data.encode('utf-8'))
print(res.text)
