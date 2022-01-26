from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('signup', views.signup, name='signup'),
    
    path('loading', views.loading, name='loading'),
    
    path('forgot-password', views.forgotPassword, name='forgot-password'),
    
    path('set-password', views.setPassword, name='set-password'),
   
#    dashboard
    path('boot/', include([
        
        path('', views.boot, name='boot'),
        
        path('home', views.home, name='home'),
        
        path('team', views.team, name='team'),
        
        path('chat', views.chat, name='chat'),
        
        path('analyse', views.analyse, name='analyse'),
        
        path('settings', views.settings, name='settings'),
        
        path('profile/', include([
            path('', views.profile, name='profile'),
            path('edit', views.edit, name='edit'),
        ])),
        
    ]))
]
