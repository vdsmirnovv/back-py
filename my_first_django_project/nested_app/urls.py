from django.urls import path
from .views import nested_view_1, nested_view_2

urlpatterns = [
    path('view1/', nested_view_1),
    path('view2/', nested_view_2),
]