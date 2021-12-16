"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import rest_framework_simplejwt.views as rest_framework_simplejwt_views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

import article.views as article_views
import accounts.views as accounts_views

router = DefaultRouter()
router.register(r'^article', article_views.ArticleViewSet)
router.register(r'^board', article_views.BoardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/kakao/login/', accounts_views.kakao_login),
    path('accounts/kakao/login/callback/', accounts_views.kakao_login_callback),
    path('api/', include(router.urls)),
    path('api/token/', rest_framework_simplejwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', rest_framework_simplejwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
