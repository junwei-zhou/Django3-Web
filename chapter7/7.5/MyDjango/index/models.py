from django.db import models

def createModel(name, fields, app_label, options=None):
    """
    动态定义模型对象
    :param name: 模型的命名
    :param fields: 模型字段
    :param app_label: 模型所属的项目应用
    :param options: 模型Meta类的属性设置
    :return: 返回模型对象
    """
    class Meta:
        pass

    setattr(Meta, 'app_label', app_label)

    # 设置模型Meta类的属性
    if options is not None:
        for key, value in options.items():
            setattr(Meta, key, value)

    # 添加模型属性和模型字段
    attrs = {'__module__': f'{app_label}.models', 'Meta': Meta}
    attrs.update(fields)
    # 使用type动态创建类
    return type(name, (models.Model,), attrs)


def createDb(model):
    """
    使用ORM的数据迁移创建数据表
    :param model: 模型对象
    """
    from django.db import connection
    from django.db.backends.base.schema import BaseDatabaseSchemaEditor
    # 创建数据表必须使用try……except，因为数据表已存在的时候会提示异常
    try:
        with BaseDatabaseSchemaEditor(connection) as editor:
            editor.create_model(model=model)
    except: pass


def createNewTab(model_name):
    """
    定义模型对象和创建相应数据表
    :param model_name: 模型名称（数据表名称）
    :return: 返回模型对象，便于视图执行增删改查
    """
    fields = {
        'id': models.AutoField(primary_key=True),
        'product': models.CharField(max_length=20),
        'sales': models.IntegerField(),
        '__str__': lambda self: str(self.id), }
    options = {
        'verbose_name': model_name,
        'db_table': model_name,
    }
    m = createModel(name=model_name, fields=fields,
                    app_label='index', options=options)
    createDb(m)
    return m