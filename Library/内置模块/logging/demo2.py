import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(filename)s:%(lineno)d line] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='myapp.log',  # 设置日志文件的路径
                    filemode='a')

logger = logging.getLogger(__name__)

try:
    int('123asd')
except Exception as e:
    logger.warning(f'error:{e} error_type:{e.__class__} file_path:{e.__traceback__.tb_frame.f_locals["__file__"]} line:{e.__traceback__.tb_lineno}  ')
    print(e)  # 错误信息
    print(e.args)  # 错误元组
    print(e.__traceback__.tb_frame.f_locals['__file__'])  # 哪个文件出错了
    print(e.__traceback__.tb_lineno)  # 文件的哪一行出错
    print(e.__class__)  # 错误类型


