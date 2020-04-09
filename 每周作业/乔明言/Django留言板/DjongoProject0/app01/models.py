from django.db import models

# Create your models here.

# 基础模型
class CommonInfo(models.Model):
    gmt_update = models.DateTimeField(auto_now=True, null=True, blank=True)
    gmt_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # 声明为抽象表
    class Meta:
        abstract = True

# 消息模型
class Message(CommonInfo):
    username = models.CharField(max_length=64)
    content = models.TextField(max_length=65535)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # 重写__str__方法，用于格式化输出
    def __str__(self):
        return f'{self.username}: {self.content} at{self.create_time}'