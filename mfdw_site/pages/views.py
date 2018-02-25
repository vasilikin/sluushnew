from django.shortcuts import render
from django.shortcuts import HttpResponse


# return HttpResponse("<h1>The Meandco Homepage</h1>")


def index(request):
        return render(request, 'pages/page.html')

# Create your views here.
