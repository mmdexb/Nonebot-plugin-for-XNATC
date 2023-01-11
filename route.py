import hashlib
import time
import requests
from nonebot import get_bot
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
from nonebot.params import CommandArg


from nonebot import get_bot
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot import on_command


hanglu = on_command("hanglu", aliases={'航路', '航路查询', '查航路', }, priority=5)





@hanglu.handle()
async def handle_first_receive( matcher: Matcher,event: GroupMessageEvent, args: Message = CommandArg()):
    args = str(args.extract_plain_text()).strip()
    dep = args.split(' ')[0]
    arr = args.split(' ')[1]
    



    # 获取当前的 Unix 时间戳
    current_time = str(int(time.time()))

    # 取前七个字符
    abi = current_time[:7]

    # 生成字符串的 MD5 哈希值
    pwd = 


    url = ''

# 发起请求
    response = requests.get(url)
    
# 读取响应内容
    data = response.json()

# 在data里那些有用的
    route = data['route']
    distance = data['distance']

    # 构造消息
    msg = '您查询的' + dep + '到' + arr + '的' +'航路为：' + '\n'+ route + '\n' + '距离：' + distance + '\n' + '导航数据版本：2213'
   
    bot = get_bot()
    await bot.send_group_msg(group_id=1022601472, message=msg)
