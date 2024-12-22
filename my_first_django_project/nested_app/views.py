from django.http import HttpResponse

def nested_view_1(request):
    return HttpResponse('<h1>Nested View 1</h1>')

def nested_view_2(request):
    return HttpResponse('<h1>Nested View 2</h1>')