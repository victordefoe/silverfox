

# 引入path
from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'researches'

urlpatterns = [
    path('home/', views.research, name='home'),
    path('login/', views.get_login, name='research_login')
     
]