from django.http import HttpResponse

def index(request):
    return HttpResponse("www.picsum.photos/1080/620/?random")