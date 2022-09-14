from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Produtos
from .serializers import ProdutosSerializer
from django.views import View
from django.http import Http404

class CadastroProdutos(APIView):
    def get(self, request):
        produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(produtos)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EmpresaDetalhe(APIView):

    """
        PUT and DELETE
    """

    def get_produto(self, pk):
        try:
            return Produtos.objects.get(pk=pk)
        except Produtos.DoesNotExist:
            raise Http404



    def get(self, request, pk):
        produto_id = self.get_empresa(pk)
        serializer = ProdutosSerializer(produto_id)
        return Response(serializer)

    def put(self, request, pk):
        produto_id = self.get_produto(pk)
        serializer = ProdutosSerializer(produto_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        produto = self.get_produto(pk)
        produto.delete()
        return Response(status=status.HTTP_200_OK)