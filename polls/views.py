
from django.http import HttpResponse


def index(request):
    return render(request, 'polls/main.html')