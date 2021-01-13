"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/13
"""
class_name = 'Poeple'
class_bases = ('Object',)
class_body = """
def __init__(self,name,age):
    self.name = name
    self.age = age
"""
class_dict = {}
call_class = type(class_name, bases=class_bases, dict=class_dict)
