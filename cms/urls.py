from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('add/', views.add_user, name='add_user'),

]
