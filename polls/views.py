from django.template import loader
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Chioce, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request)) 아래 render 사용하면 똑같다.
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_chioce = question.chioce_set.get(pk=request.POST['chioce'])
    except(KeyError, Chioce.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        select_chioce.vote +=1
        select_chioce.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
