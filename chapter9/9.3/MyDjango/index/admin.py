from django.contrib import admin
from .models import *

# 修改title和header
admin.site.site_title = 'MyDjango后台管理'
admin.site.site_header = 'MyDjango'

# 方法一：
# 将模型直接注册到admin后台
# admin.site.register(PersonInfo)

# 方法二：
# 自定义PersonInfoAdmin类并继承ModelAdmin
# 注册方法一，使用装饰器将PersonInfoAdmin和Product绑定
@admin.register(PersonInfo)
class PersonInfoAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'name', 'age']


# 注册方法二
# admin.site.register(PersonInfo, PersonInfoAdmin)


@admin.register(Vocation)
class VocationAdmin(admin.ModelAdmin):
    # 在数据新增或修改的页面设置可编辑的字段
    # fields = ['job','title','payment','person']

    # 在数据新增或修改的页面设置不可编辑的字段
    # exclude = []

    # 改变新增或修改页面的网页布局
    fieldsets = (
        ('职业信息', {
            'fields': ('job', 'title', 'payment')
        }),
        ('人员信息', {
            # 设置隐藏与显示
            'classes': ('collapse',),
            'fields': ('person',),
        }),
    )

    # 将下拉框改为单选按钮
    # admin.HORIZONTAL是水平排列
    # admin.VERTICAL是垂直排列
    radio_fields = {'person': admin.HORIZONTAL}

    # 在数据新增或修改的页面设置可读的字段，不可编辑
    # readonly_fields = ['job',]

    # 设置排序方式，['id']为升序，降序为['-id']
    ordering = ['id']

    # 设置数据列表页的每列数据是否可排序显示
    sortable_by = ['job', 'title']

    # 在数据列表页设置显示的模型字段
    list_display = ['id', 'job', 'title', 'payment', 'person']

    # 为数据列表页的字段id和job设置路由地址，该路由地址可进入数据修改页
    # list_display_links = ['id', 'job']

    # 设置过滤器，如有外键，应使用双下画线连接两个模型的字段
    list_filter = ['job', 'title', 'person__name']

    # 在数据列表页设置每一页显示的数据量
    list_per_page = 100

    # 在数据列表页设置每一页显示最大上限的数据量
    list_max_show_all = 200

    # 为数据列表页的字段id和job设置编辑状态
    list_editable = ['job', 'title']

    # 设置可搜索的字段
    search_fields = ['job', 'title']

    # 在数据列表页设置日期选择器
    date_hierarchy = 'recordTime'

    # 在数据修改页添加“另存为”功能
    save_as = True

    # 设置“动作”栏的位置
    actions_on_top = False
    actions_on_bottom = True
