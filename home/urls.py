from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("category/<slug:slug>/", views.category, name="category"),
    path('<int:pk>/<slug:slug>/', views.VideoDetail, name='detail'),
    path('videolist/', views.VideoList, name='video_all'),
    path('search/', views.Search, name='search'),
    path('like/<int:pk>/<slug:slug>/', views.likeDetail, name='like'),
    path('notification/<int:pk>', views.NotificationView.as_view(), name='notification'),
]