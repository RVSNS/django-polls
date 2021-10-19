from django.db.models import F
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question

"""
def index(request:HttpRequest)->HttpResponse:
    latest_question_list = Question.objects.order_by('-publish_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html',context=context)

def detail(request:HttpRequest,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html',{"question":question})

def results(request:HttpRequest,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request:HttpRequest,question_id:int):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(
            request,'polls/detail.html',
            {
                'question':question,
                'error_message':"you didn't select a choice.",
            }
        )
    else:
        selected_choice.votes=F('votes')+1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results',args=(question.id,))
        )
"""
class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name = 'polls/question_detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request:HttpRequest,question_id:int):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(
            request,'polls/detail.html',
            {
                'question':question,
                'error_message':"you didn't select a choice.",
            }
        )
    else:
        selected_choice.votes=F('votes')+1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results',args=(question.id,))
        )
