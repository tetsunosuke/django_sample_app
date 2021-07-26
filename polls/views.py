from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from django.shortcuts import redirect
from django.db import transaction
import time




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)



def add(request, question_id, x):
    q = Question.objects.get(id=question_id)
    q.amount += int(x)
    q.save()
    return redirect("/polls")
def buy(request, question_id, x):
    # TODO: wait for seconds
    time.sleep(3)
    with transaction.atomic():
        q = Question.objects.select_for_update().get(id=question_id)
        q.amount -= int(x)
        if q.amount < 0:
            # マイナスに減算せず戻す
            return redirect("/polls/" + str(question_id))
        q.save()
    return redirect("/polls")
