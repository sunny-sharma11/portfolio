from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('resume', views.resume, name='resume'),
    path('work', views.work, name='work'),
    path('contact', views.contact, name='contact')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
