from django.shortcuts import render
from subjects import models as subject_models


def homeRender(request):

    subjectList = subject_models.Subject.objects.all()

    return render(request, "screens/home.html", context={
        "subjectList": subjectList
    })