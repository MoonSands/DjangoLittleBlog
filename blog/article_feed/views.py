from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from .serializers import *


def index(request):
    pass

#Posts
class PostAPIView(generics.ListAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer

#class PostCreateAPIView(generics.CreateAPIView):
#   permission_classes = [IsAdminUser]
#
#   queryset = post.objects.all()
#    serializer_class = PostSerializer

class PostCreateAPIView(APIView):
    #   permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostUPdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    queryset = post.objects.all()
    serializer_class = PostSerializer

#Docs

class DocsAPIView(generics.ListAPIView):
    queryset = docs.objects.all()
    serializer_class = DocsSerializer

class DocsCreateAPIView(APIView):
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):
        print(request.data)
        serializer = DocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocsUPdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


    queryset = docs.objects.all()
    serializer_class = DocsSerializer

#FAQ

class FAQAPIView(generics.ListAPIView):
    queryset = faq.objects.all()
    serializer_class = FAQSerializer

class FAQCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]

    queryset = faq.objects.all()
    serializer_class = FAQSerializer


class FAQUPdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    queryset = faq.objects.all()
    serializer_class = FAQSerializer

#Product

class ProductAPIView(generics.ListAPIView):
    queryset = products.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    #permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUPdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    queryset = products.objects.all()
    serializer_class = ProductSerializer

#Messages from form

class DataFromFormsAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]

    queryset = dataFromForms.objects.all()
    serializer_class = FormsSerializer


class DataFromFormsSingleAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]

    queryset = dataFromForms.objects.all()
    serializer_class = FormsSerializer




