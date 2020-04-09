from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    # 元信息
    class Meta:
        model = Message
        # fields 中的username、content来自于 ORM模型model中的字段名
        fields = ['username', 'content']
        error_messages = {
            'username':{'required':"昵称错误",},
            'content':{'required':"留言错误",},
        }
        # createtime 时间不需要用户填写，所以此处只有两个字段