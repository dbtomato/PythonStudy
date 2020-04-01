from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    # 元信息
    class Meta:
        model = Message
        fields = ['username', 'content']
        # createtime 时间不需要用户填写，所以此处只有两个字段