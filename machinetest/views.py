from django.shortcuts import render

# Create your views here.


def cv(request):
     return render(request, 'bio/cv.html')


def bio(request):
     return render(request, 'bio/bio.html')