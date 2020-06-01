from django.contrib import admin

# Register your models here.
from App.models import Goods, student, Grade, News


class GoodsAdmin(admin.ModelAdmin):
    # 显示的字段，展示数据字段的时候
    list_display = ['name','price']
    # 过滤 类似于excel的筛选字段
    list_filter = ['name','price']
    # 可搜素字段
    search_fields = ['name']
    # 每页显示的数目
    list_per_page = 5

    # 添加、修改、删除页面的显示字段以及顺序
    fields = ['name','price']


class StudentInfo(admin.TabularInline):
    # 创建新数据的时候， 顺便添加下面模型的数据
    model = student
    extra = 2

class GradeAdmin(admin.ModelAdmin):
    # 应该该admin时候，自动关联下面类对应的模型数据
    inlines = [StudentInfo]



admin.site.register(Goods,GoodsAdmin)
admin.site.register(student)
admin.site.register(Grade,GradeAdmin)
admin.site.register(News)



