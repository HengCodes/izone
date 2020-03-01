from django.contrib import admin

from .models import (CourseClauses, CourseTopic)


# Register your models here.

@admin.register(CourseTopic)
class CourseTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'slug', 'category')


@admin.register(CourseClauses)
class CourseClausesAdmin(admin.ModelAdmin):
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    date_hierarchy = 'create_date'

    exclude = ('views',)

    # 在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
    list_display = ('id', 'title', 'author', 'create_date', 'update_date', 'is_top')

    # 设置需要添加<a>标签的字段
    list_display_links = ('title',)

    # 激活过滤器，这个很有用
    list_filter = ('create_date', 'category', 'is_top')

    list_per_page = 50  # 控制每页显示的对象数量，默认是100

    # 限制用户权限，只能看到自己编辑的文章
    def get_queryset(self, request):
        qs = super(CourseClausesAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
