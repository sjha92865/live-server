from django.urls import path, re_path

from . import views
#from .views import GeneratePDF

urlpatterns = [
    
    path('preview/',views.newproject,name='newproject'),
    path('mend2/',views.mend2,name='mend2'),

    

    
    
]