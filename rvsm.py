
from nonebot import get_bot
from nonebot import on_command, require, get_driver
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message, MessageSegment
import urllib.request
import _thread
import requests
import json

rvsm = on_command("rvsm", priority=5, aliases={"rvsm","RVSM"})
@rvsm.handle()
async def handle_first_receive():
    info="RVSM是什么？\nRVSM（Reduced Vertical Separation Minimum）是指降低垂直分离最小值，是一种在高空飞行中，为了提高飞行效率，减少飞行时间，降低燃油消耗，降低噪声，降低污染物排放，提高飞机性能，提高飞行安全的一种飞行模式。"
    image_path="file:///C:/Users/Administrator/Desktop/rvsm.jpg"
    msg2 = MessageSegment.image(image_path)
    msg = msg2 + info
    bot = get_bot()
    #发送图片

    await bot.send_group_msg(group_id=1022601472, message=msg)
