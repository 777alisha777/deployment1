from django.urls import path
from appFour import views

#for template tagging
app_name = 'appFour'

urlpatterns = [
    path('relative/', views.relative, name='relative'), #grab views from relative
    path('other/', views.other, name='other')

]
