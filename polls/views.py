from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Question, Choice
from django.views import generic

# def index(request):
#     last_question_list = Question.objects.all().order_by('-pub_date')[:5]  # order_by -сортировка по pub_date? c - Это вначале новые
#     context = {
#         'questions': last_question_list
#     }
#     return render(request, 'index.html', context)

class Index(generic.ListView):
    model = Question
    template_name = 'index.html'
    context_object_name = 'questions' # Also can use {% if object_list %} in index.html. object_list is reserved method. #}

    def get_queryset(self):
        return self.model.objects.all().order_by('-pub_date')[:5] #выдает 5 вопросов в обратном направлении ('-pub_date' - последний добавленный вверху)

# def detail(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     # question = Question.objects.get(id=question_id)
#     return render(request, 'detail.html', {'question': question})
#     # return HttpResponse(f'Вы находитесь на странице вопроса №{question_id}')

class QuestionDetail(generic.DetailView):
    model = Question    # тут в html Он указывается как object.question_text

# def result(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, 'result.html', {'question': question})

class Result(QuestionDetail):
    context_object_name = 'question' # тут контекст в Html будет искать как question
    template_name = 'result.html'   # тут говорим не надо испол. стандрарный, а result.html темплейт
    pk_url_kwarg = 'question_id' #делаем так чтобы в urls.py не менять <int:question_id> в pk

# def vote(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     choice_id = int(request.POST.get('choice'))
#       # choice = Choice.objects.get(id=choice_id) # it uses without question variable
#     choice = question.choices.get(id=choice_id)
#     choice.votes += 1
#     choice.save()
#     return redirect(reverse('result', kwargs={'question_id':question_id}))

class Vote(generic.View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        choice_id = int(request.POST.get('choice'))
        choice = question.choices.get(id=choice_id)
        choice.votes += 1
        choice.save()
        return redirect(reverse('result', kwargs={'question_id':question_id}))
