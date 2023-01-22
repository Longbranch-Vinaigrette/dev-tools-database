import json
import os

from django.http import HttpResponse
print("CWD: ", os.getcwd())


def index(request):
    print("Request body: ")
    print(request.body)
    data = {
        "debug": {
            "message": "Success"
        }
    }
    res = HttpResponse(json.dumps(data))
    res.headers["Content-Type"] = "application/json"

    return res


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

