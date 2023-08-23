from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('', views.home, name='home'),
    # path('add-student/', views.add_student, name='add_student'),
    # path('update_student/<id>', views.update_student, name='update_student'),
    # path('delete_student/<id>', views.delete_student, name='delete_student'),
    path('register-user/', RegisterUser.as_view(), name='RegisterUser'),
    path('student/', StudentAPI.as_view(), name='StudentAPI'),
    path('get-book/', views.get_book, name='get_book')
]
