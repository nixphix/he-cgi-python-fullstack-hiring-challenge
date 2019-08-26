from django.conf import settings
from django.urls import include, path, re_path
from rest_framework.authtoken import views


urlpatterns = [
    path("api/v1/", include("games.urls")),
    path("token/", views.obtain_auth_token),
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

    if "drf_yasg" in settings.INSTALLED_APPS:
        from drf_yasg import openapi
        from drf_yasg.views import get_schema_view

        schema_view = get_schema_view(
            openapi.Info(
                title="Games",
                default_version='v1',
                description="Games Backend",
            ),
            validators=['flex', 'ssv'],
            public=True,
        )
        urlpatterns.extend(
            [
                re_path(r'docs(?P<format>.json|.yaml)', schema_view.without_ui(cache_timeout=None), name='schema-json'),
                path('docs/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
            ]
        )
