
from .models import Category, Product
from .documents import ProductDocument
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE', 'UPDATE']:
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().select_related('category')
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE', 'UPDATE']:
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()


class ProductSearchAPIView(APIView):
    serializer_class = ProductSerializer
    document_class = ProductDocument
    
    def get(self, request, query):
        search = self.document_class.search().query('query_string', query=query, fields=['title', 'description'])
        response = search.to_queryset()
        data = self.serializer_class(response, many=True).data
        return Response(data)
