from django.contrib import admin
from django.urls import path, include

from mytube import views

urlpatterns = [
    path('video/upload/', views.upload_video),
    path('video/stream/', views.stream_video),
    path('login/', views.login),
    path('signup/', views.signup_view),
    path('comment/upload/', views.comment_upload),
    path('comment/view/all', views.comment_view_all),
    path('comment/view/<str:videoid>/', views.comment_view),
    path('comment/delete/', views.comment_delete),
    path('admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
