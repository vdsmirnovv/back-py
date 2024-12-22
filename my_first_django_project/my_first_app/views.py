from django.http import HttpResponse
from django.http import QueryDict
from django.shortcuts import redirect
from django.http import JsonResponse

'''
def hello_world(request, name):
    age = request.GET.get('age', 'unknown')
    return HttpResponse(f'<h1>Hello, {name}! You are {age} years old.</h1>')
    '''

def redirect_example(request):
    return redirect('/hello/test/?age=3')

def json_example(request):
    data = {'name': 'John', 'age': 30}
    return JsonResponse(data)

def hello_world(request, name):
    response = HttpResponse(f'<h1>Hello, {name}!</h1>')
    response.set_cookie('username', name)
    return response

def show_cookies(request):
    cookies = request.COOKIES
    return HttpResponse(f'<h1>Cookies: {cookies}</h1>')