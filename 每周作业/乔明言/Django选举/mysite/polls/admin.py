from django.contrib import admin
from django.contrib.admin import StackedInline

from .models import Choice, Question

# Register your models here.

# 用于 Question 类中的inlines
# class ChoiceInline(StackedInline):    # 继承StackedInline 类时，每个字段单独显示为一行
class ChoiceInline(admin.TabularInline):
    """
    继承 admin.TabularInline，同一个model class 中的数据显示为一行
    """
    model = Choice
    extra = 3      # 额外显示的空行，用于添加choice

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']  # 调整字段显示顺序

    # 区分字段集合
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline] # 用于在Question 管理页面编辑Choice
    # 定制实力的列表页面
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加过滤属性,在页面右侧添加FILTER过滤侧栏
    list_filter = ['pub_date']
    # 添加搜索框
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


