"""demo_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# from rest_framework import routers
from demo_app import views
from demo_app.class_based_views import Crud
from demo_app.generic_class_based_views import CreateListGenerics, DestroyView,RetrieveView
from demo_app.mixins_class_based_views import CreateList




# router = routers.DefaultRouter()
# router.register(r'', views.Entry)
# router.register(r'user/', views.UserViewset)
# router.register(r'group/', views.GroupViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    # path('entry',Crud.as_view()),
    # path('entry/<id>/',Crud.as_view()),
    path('mixin/',CreateList.as_view()),
    # path('mixin/<pk>/',CreateList.as_view())
    path('createlist/',CreateListGenerics.as_view()),
    path('retrieve/<pk>/',RetrieveView.as_view()),
    path('destroy/<pk>/',DestroyView.as_view())

]
