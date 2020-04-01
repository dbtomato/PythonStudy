from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse
from django.contrib import messages as django_messages

from .forms import MessageForm
from .models import Message

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")

    message_form = MessageForm()
    # 判断是否 POST 请求，是的话发送数据
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        # 检查表单是否合法
        if message_form.is_valid():
            # 如果合法，则保存数据
            message_form.save()
            # 调用 django.contrib.messages 的方法，返回留言状态
            # django.contrib.messages 模块自动生成一个`messages`变量，禁止在 context中定义同名变量，会覆盖当前默认变量
            django_messages.success(request, '留言成功')
            return redirect(reverse('index'))

    # 拿到所有留言
    messages = Message.objects.all()
    # 留言赋值给 message_list
    context = {
        # 'title': '乔明言',
        'message_list': messages,
        'form': message_form
    }
    # rander()渲染，将context渲染到 index.html
    return render(request, 'index.html', context)
