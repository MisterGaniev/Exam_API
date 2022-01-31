from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from app_1.views import TodoViewSet

router = DefaultRouter()

router.register('todo', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

