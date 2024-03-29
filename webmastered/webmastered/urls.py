from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from wagtail.contrib.sitemaps.views import sitemap

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("engine/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("__reload__/", include("django_browser_reload.urls")),
    path('portal/', include('portal.urls')),
    path('sitemap.xml', sitemap),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    from django.views.defaults import page_not_found, server_error
    def wm_page_not_found(request):
        return page_not_found(request, None)

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Django Debug Toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
        path("404/", wm_page_not_found),
        path("500/", server_error),
    ] + urlpatterns

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
