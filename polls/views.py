from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from django.shortcuts import redirect




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def update(request, question_id):
    # TODO: wait for seconds
    return redirect("/polls")
def update_lock(request, question_id):
    # TODO: wait for seconds
    return redirect("/polls")
