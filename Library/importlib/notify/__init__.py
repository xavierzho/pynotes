from .settings import NOTIFY_LIST
import importlib


def send_all(content):
    for path_str in NOTIFY_LIST:
        module_path, class_name = path_str.rsplit('.', maxsplit=1)
        # 1.利用字符串导入模块
        module = importlib.import_module(module_path)
        # 2.利用反射获取类名
        cls = getattr(module, class_name)
        # 3.生成类的对象
        obj = cls()
        # 4.利用鸭子类型直接调用send()方法
        obj.send(content)
