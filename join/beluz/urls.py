"""beluz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from home.views import page_view, home_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('home', home_view, name='home_view'),
    path('<page_name>.html', page_view, name='page_view'),
    path('admin/', admin.site.urls),
    path('api/token/auth/', obtain_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('comments/', include('django_comments.urls')),
    path('photologue/', include('photologue.urls', namespace='photologue')),
    path('login/', auth_views.login,
         {
             'template_name': 'pages_templates/page-login.html',
         }, name='login'),
    path('logout/', auth_views.logout, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + urlpatterns
