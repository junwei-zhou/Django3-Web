from django.db import models
from django.db import connection
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

def create_table(sql):
    # 创建数据表必须使用try……except，因为数据表已存在的时候会提示异常
    try:
        with BaseDatabaseSchemaEditor(connection) as editor:
            editor.execute(sql=sql)
    except:
        pass

# 创建分表
tb_list = []
for i in range(3):
    create_table(f'''
        create table  if not exists person{i}(
        id int primary key auto_increment ,
        name varchar(20),
        sex tinyint not null default '0'
        )ENGINE=MyISAM DEFAULT CHARSET=utf8
        AUTO_INCREMENT=1 ;
    ''')
    tb_list.append(f'person{i}')

# 创建总表
# tb_str是将所有分表联合到总表
tb_str = ','.join(tb_list)
create_table(f'''
    create table  if not exists allperson(
    id int primary key auto_increment ,
    name varchar(20),
    sex tinyint not null default '0'
    )ENGINE=MERGE UNION=({tb_str}) INSERT_METHOD=LAST 
    CHARSET=utf8 AUTO_INCREMENT=1 ;
''')


class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    sex = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人员信息'
        # 参数managed代表不会在数据迁移中创建数据表
        managed = False
        # 模型映射数据库中特定的数据表
        db_table = 'allperson'




