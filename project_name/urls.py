""" Default urlconf for {{ project_name }} """

from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import index, sitemap
from django.views.generic.base import TemplateView
from django.views.defaults import (permission_denied,
                                   page_not_found,
                                   server_error)


sitemaps = {
    # Fill me with sitemaps
}

urlpatterns = [
    path('', include('apps.base.urls')),

    # Admin
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Sitemap
    path(r'sitemap\.xml', index, {'sitemaps': sitemaps}),
    path(r'^sitemap-<section:section>\.xml', sitemap, {'sitemaps': sitemaps}),

    # robots.txt
    path(r'robots\.txt',
         TemplateView.as_view(
             template_name='robots.txt',
             content_type='text/plain')
         ),
]

if settings.DEBUG:
    # Add debug-toolbar
    import debug_toolbar  # noqa
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

    # Serve media files through Django.
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    # Show error pages during development
    urlpatterns += [
        path('403/', permission_denied),
        path('404/', page_not_found),
        path('500/', server_error)
    ]
