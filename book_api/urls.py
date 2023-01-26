from django.contrib import admin
from django.urls import path
from book_api.views import *

urlpatterns = [
    # 1ere method
    # path('list/', book_list),  # get
    # path('', book_create),  # post
    # path('<int:pk>', book)  # get with id

    # 2eme method
    path('list/', BookList.as_view()),  # get
    path('', BookCreate.as_view()),  # post
    path('<int:pk>', BookDetail.as_view())  # get with id
]
