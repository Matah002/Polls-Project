from django.shortcuts import render,HttpResponse
# from django.http import HttpResponse
from .models import Question
# from django.template import loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):             # %s This is a question holder
    return HttpResponse("<h2>You're looking at question %s.</h2>" % question_id)


def results(request, question_id):
    response = "<h2>You're looking at the results of question %s.</h2>"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("<h2>You're voting on question %s.</h2>" % question_id)
#https://www.perplexity.ai/search/Humane-AI-explores-AU.wpBWXSVubdfyZry8GVQ
# https://gamma.app/create/generate/62mhkoj8fq5eh1c





