from nonebot import get_bot
from nonebot import on_command, require, get_driver
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

help = on_command("help", priority=5, aliases={"help","帮助"})
@help.handle()
async def handle_first_receive():
    
    msg = 'Hi,我是XNATC BOT您可以尝试下列指令来使用我♡' + '\n' + '/气象 机场四字码 =>获取最新气象报文以及解析' + '\n' + '/在线 =>查看在线人数' + ' \n' + '/活动 =>查看最近活动' + '\n' + '/rvsm =>查看rvsm相关信息' + '\n' + '\n' + '/查航路 起飞机场 到达机场 =>查询航路' +'\n'+'/帮助 => 获取指令列表 '
    bot = get_bot()
    await bot.send_group_msg(group_id=1022601472, message=msg)
