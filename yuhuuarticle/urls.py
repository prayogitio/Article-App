from django.contrib import admin
from django.urls import path, include #include enables us to get the template from another app
from . import views #this enables us to interact with views.py
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #this is for static assets folder where we put css
from django.conf.urls.static import static #this is for media purposes
from django.conf import settings #this is also for media purposes
from articles import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', home_views.article_list, name="home"),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls'))
]

#THIS IS FOR ASSETS AND MEDIA
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#virtualenv env --no-site-packages
#then search for Scripts folder run activate