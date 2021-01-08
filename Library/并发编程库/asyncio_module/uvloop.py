# 是asyncio 是时间循环的替代方案，事件循环>默认asyncio事件循环
# uvloop 暂不支持win32

import uvloop
import asyncio
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
