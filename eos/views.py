from django.http import HttpResponse

def index(request):
    return HttpResponse("https://picsum.photos/1080/620/?random")