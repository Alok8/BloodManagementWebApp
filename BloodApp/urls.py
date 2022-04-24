from django.urls import path

from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('add',add_donor,name='add_donor'),
    path('search',list_all,name='list_all'),
    path('search_result',search_result,name='search_result'),
    path('<int:pk>',edit_donor,name='edit_donor'),
    path('delete/<int:pk>/',delete_donor,name='delete_donor'),
    path('blood_check',blood_check,name='blood_check')
] 