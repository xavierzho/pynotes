import logging

# 设置日志的格式
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(filename)s:%(lineno)d line] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='myapp.log',  # 设置日志文件的路径
                    filemode='a')

# logging.basicConfig(level=logging.INFO,
#                     format='levelName:%(levelname)s fileName:%(filename)s'
#                            'outputNumber:[%(lineno)d] thread:%(threadName)s '
#                            'output msg:- %(asctime)s',
#                     datefmt='[%d/%b/%Y %H:%M:%S]',
#                     # filename='loggmsg.log',
#                     # filemode='a'
#                     )

# 实例化logger对象
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info('this is a info log')
    logger.info('this is a info log 1')

# 在任何py文件中调用logger即可

