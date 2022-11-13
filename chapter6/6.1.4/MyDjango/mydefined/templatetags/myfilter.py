from django import template
# 创建模版对象
register = template.Library()
# 声明并定义过滤器
@register.filter(name='replace')
def do_replace(value, agrs):
    oldValue = agrs.split(':')[0]
    newValue = agrs.split(':')[1]
    return value.replace(oldValue, newValue)
