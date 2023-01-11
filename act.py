
from nonebot import get_bot
from nonebot import on_command, require, get_driver
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import datetime
import time
import urllib.request
import _thread
import requests
import json


atc= on_command("actvive" ,aliases={'最近活动' ,'活动' ,'近期活动'} ,priority=5)

@atc.handle()
async def activity():
# 获取群号

 group_id = 1022601472



    # 获取远程 JSON 数据
 url = ""
 response = urllib.request.urlopen(url)
 data = json.loads(response.read())

    # 解析 JSON 数据


 info = data['info'][0][0]
 airport_list = info['airport_list']
 dep = airport_list[0]
 arr = airport_list[1]
 name = info['name']
 start_time = info['start_time']
 #转化为中文时间格式
 start_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(int(start_time)))
 end_time = info['end_time']
 #转化为中文时间格式
 end_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(int(end_time)))
 route = info['route']
 detail = info['detail']

 activity_id = info['id']

 msg= f"活动名称: {name}\n开始时间: {start_time}\n结束时间: {end_time}\n起飞机场：{dep}\n到达机场：{arr}\n路线: {route}\n详情: {detail}\n活动 ID: {activity_id}"

# 构造消息

 bot = get_bot()

    # 将解析后的内容发送回群聊中
 await bot.send_group_msg(group_id= group_id, message=msg)