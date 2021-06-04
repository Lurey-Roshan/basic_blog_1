from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
  
from  blog import views

urlpatterns = [
    path('', views.allblog, name ='allblog'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

