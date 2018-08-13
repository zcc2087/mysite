from django.contrib import admin
from .models import BlogType, Blog

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    #list_display设置要显示在列表中的字段，id是Django模型的默认主键
    list_display = ('id', "type_name")

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'author', 'created_time', 'last_updated_time')
    #list_per_page设置每页显示记录的条数，默认是100
    list_per_page = 10

'''
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'blog')
'''
admin.site.site_header = '后台登陆'
admin.site.site_title = '博客后台'