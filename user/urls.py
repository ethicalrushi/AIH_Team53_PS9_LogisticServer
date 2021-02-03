from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),  
    path('getUserDetails/', views.getUserDetails),
    
]