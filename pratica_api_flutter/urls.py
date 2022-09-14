
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from app.viewset import ProdutosViewSet

router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/', include(router.urls)),

    path('', include('app.urls')),
]

