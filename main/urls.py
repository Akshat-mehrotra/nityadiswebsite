from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
                    buy,
                    home,
                    upload_art,
                    art,
                    about,
                    getit,)

app_name = 'main'

urlpatterns = [
    path('', home, name="home"),
    path('purchase/<int:pk>', buy, name="buy"),
    path('artwork', art, name="art"),
    path('getit/<int:pk>', getit, name='getit'),
    path('upload_art', upload_art, name="upload_art"),
    path('about', about, name='about')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
