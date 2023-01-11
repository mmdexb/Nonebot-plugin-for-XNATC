import json
from nonebot import get_bot
from nonebot import on_command, require, get_driver
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

import urllib.request
import _thread
import requests

online = on_command("online", aliases={'在线','在线管制','在线飞行员','在线人数','在线信息'},priority=5)
@online.handle()
async def online():
    group_id = 1022601472
    #获取json数据
    url = ""
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    pilots = data['pilots']
    atcs = data['atcs']

    online_pilots = len(pilots)
    online_atcs = len(atcs)
    online_count = online_pilots + online_atcs

    message = "在线人数：{}\n在线飞行员：\n".format(online_count)
    for pilot in pilots:
        message += "呼号：{}，出发机场：{}，到达机场：{}\n".format(pilot['call_sign'], pilot['departure_airport'], pilot['arrival_airport'])
    message += "在线管制员:\n"
    for atc in atcs:
        message += "呼号：{}，用户ID：{}\n".format(atc['call_sign'], atc['user_id'])

    bot = get_bot()
    await bot.send_group_msg(group_id=group_id, message=message)

    