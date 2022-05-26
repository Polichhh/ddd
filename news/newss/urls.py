from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostDetail

# urlpatterns = [
#     path('default', default)
# ]

urlpatterns = [

    path('news/', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]

