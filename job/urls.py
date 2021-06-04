from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
  
from  job import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('jobs',views.d_job, name='jobdetail')
    
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)