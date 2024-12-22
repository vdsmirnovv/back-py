from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>/', views.hello_world),
    path('redirect/', views.redirect_example),
    path('json/', views.json_example),
    path('cookies/', views.show_cookies),
]


