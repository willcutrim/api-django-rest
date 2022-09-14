from django.urls.conf import path

from . import views

from .viewset import ProdutosViewSet

urlpatterns = [
   
    path('listar/', ProdutosViewSet.as_view),
]