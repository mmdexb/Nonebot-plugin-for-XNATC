



from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Event, GroupIncreaseNoticeEvent, MessageSegment

def _rule(event: Event):
    return isinstance(event, GroupIncreaseNoticeEvent)

join=on_notice(rule=_rule)
@join.handle()
async def group_increase_handle(event: GroupIncreaseNoticeEvent):
    msg = '欢迎' + MessageSegment.at(event.user_id) + '加入XNATC!' + "\n" + "如果您对XNATC还没有了解，不妨访问我们的网站https://www.xnatc.com/"+ "\n" + "当然，您也可以访问https://fly.xnatc.com/ 来了解我们的飞行活动" + '\n' + "群内的BOT也向您开放，您可以通过发送 /帮助 来查看BOT的功能" + '\n' + "最后欢迎加入XNATC的大家庭！Enjoy your flight!"
    await join.finish(msg)
    