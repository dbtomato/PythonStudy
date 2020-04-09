from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from django.views import generic

from .models import Question, Choice



# Create your views here.

# def index(request):
#     lastest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in lastest_question_list])
#     # return HttpResponse(output)
#
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'lastest_question_list': lastest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))
#
#     context = {
#         'lastest_question_list': lastest_question_list,
#     }
#     return render(request, d/index.html', context)

# def detail(request, question_id):
#     # return HttpResponse('this is %s.' % question_id)
#
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


"""
    类视图：使用通用视图，简化以上注释的代码
"""
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # 显示指定上下文变量名，覆盖默认的变量名question_list
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



