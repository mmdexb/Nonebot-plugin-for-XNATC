from nonebot import get_bot
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
import random
import time
import _thread
import requests
import json

qixiang = on_command("qixiang", priority=5, aliases={'气象', '天气', '天气预报', '气象预报', '天气预报查询', '气象预报查询', '天气查询', '气象查询'})


@qixiang.handle()
# 获取参数
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        #转为大写字符串
        plain_text = plain_text.upper()

        from metar import Metar

        #构建json url
        url = ""

        #获取json数据
        response = requests.get(url)
        data = response.json()

        metar1 = data['metar']

        obs = Metar.Metar(metar1)
        #获取元数据
        time = str(obs.time)
        wind = str(obs.wind())
        vis = str(obs.visibility())
        temp = str(obs.temp)
        pres = str(obs.press)
        dewp = str(obs.dewpt)

        #构造消息
        msg =  plain_text + '的气象报文为: ' + metar1 + '\n' +'解析如下：'+ '\n' + '时间：' + time + '\n' + '风向：' + wind + '\n' + '能见度：' + vis + '\n' + '温度：' + temp + '\n' + '气压：' + pres + '\n' + '露点：' + dewp






        bot=get_bot()
        await bot.send_group_msg(group_id=1022601472, message=msg)




    else: #发送消息说出现错误
        await qixiang.finish('请输入正确的ICAO代码')
