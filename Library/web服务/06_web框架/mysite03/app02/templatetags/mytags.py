from django import template
register = template.Library()


# 自定义过滤器(参数最多2个)
@register.filter(name='baby')
def my_sum(v1, v2):
    return v1 + v2


# 自定义标签（参数可以有多个）
@register.simple_tag(name='plus')
def index(a, b, c, d):
    return '%s-%s-%s-%s' % (a, b, c, d)


# 自定义inclusion_tag
@register.inclusion_tag(filename='left_menu.html')
def left_menu(n):
    data = ['第{}项'.format(i) for i in range(n)]
    # 第一种
    # return {'data':data}
    # 第二种
    return locals()  # 将data传递给left_menu.html

