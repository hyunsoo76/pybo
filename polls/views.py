from django.template import loader
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request)) 아래 render 사용하면 똑같다.
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/index.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)