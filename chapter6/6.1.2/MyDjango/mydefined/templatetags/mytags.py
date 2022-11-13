from django import template
# 创建模版对象
register = template.Library()

# 定义模版节点类
class ReversalNode(template.Node):
    def __init__(self, value):
        self.value = str(value)

    # 数据反转处理
    def render(self, context):
        return self.value[::-1]

# 声明并定义标签
@register.tag(name='reversal')
# parse是解析器对象，token是被解析的对象
def do_reversal(parse, token):
    try:
        # tag_name是代表标签名，即reversal
        # value是由标签传递的数据
        tag_name, value = token.split_contents()
    except:
        raise template.TemplateSyntaxError('syntax')
    # 调用自定义的模板节点类
    return ReversalNode(value)
