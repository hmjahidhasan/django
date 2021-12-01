
from django.contrib import admin
from django.urls import path,include
from langdingApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('feature/', views.feature, name='feature'),
    path('screenshot/', views.screenshot, name='screenshot'),
    path('review/', views.review, name='review'),
    path('plan/', views.plan, name='plan'),
    path('download/', views.download, name='download'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
