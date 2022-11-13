# 模型字段的基本类
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 模型字段的字符类型
class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')

# 模型字段的整数类型
class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')

# 定义元类ModelMetaclass，控制Model对象的创建
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        for k, v in attrs.items():
            # 保存类属性和列的映射关系到mappings字典
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            # 将类属性移除，使定义的类字段不污染User类属性
            attrs.pop(k)
        # 假设表名和为类名的小写,创建类时添加一个__table__类属性
        attrs['__table__'] = name.lower()
        # 保存属性和列的映射关系，创建类时添加一个__mappings__类属性
        attrs['__mappings__'] = mappings
        return super().__new__(cls, name, bases, attrs)

# 定义Model类
class Model(metaclass=ModelMetaclass):
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        super().__init__()

    def save(self):
        fields, params = [], []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append(str(self.kwargs[k]))
        sql = 'insert into %s (%s) values (%s)'
        sql = sql % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)


# 定义模型User
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建实例对象
u = User(id=123, name='Dj', email='Dj@dd.gg', password='111')
# 调用save()方法
u.save()