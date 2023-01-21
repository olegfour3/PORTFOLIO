from django.contrib import admin
from django.urls import path, include, re_path
from .views import (
    homePage,
    projectsPage,
    projectDetail,
    search,
    handler404,
)

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.static import serve


handler404 = handler404

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', homePage, name='homePage'),
    path('projects/', projectsPage, name='projectsPage'),
    path('projects/<str:slug>/', projectDetail, name='projectDetail'),
    path('search/', search, name='search'),

    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
