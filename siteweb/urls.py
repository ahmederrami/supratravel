# test new branch in github
# it works
from django.urls import path
from django.views.generic import TemplateView
#from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html'), name='home'),
    #path('aos', views.aolistview, name='aolistview'),
    #path('recrutements', views.recrutementlistview, name='recrutementlistview'),
]
