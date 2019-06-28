from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url('^$',views.index, name = 'index'),
  url(r'^new_restaurant/$', views.new_restaurant, name='new_restaurant'),
  url(r'^profile/$',views.profile,name='profile'),
  url(r'^restaurant/$',views.restaurant,name='restaurant'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)