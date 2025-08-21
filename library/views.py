from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BoockSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views heremdhesuf.

# class BookListApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BoockSerializer


class BookListApiView(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer_date = BoockSerializer(books, many=True).data
        info = {
            'status':'all books have been shown',
            'books list':serializer_date
        }
        return Response(info, status=status.HTTP_200_OK)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BoockSerializer
#     lookup_field = 'id'

class BookDetailApiView(APIView):
    def get(self, request, pk):
        book = Books.objects.get(id=pk)
        serializer_data = BoockSerializer(book).data
        info = {
            'status':'Book taken sucsessfully',
            'book':serializer_data
        }
        return Response(info)

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BoockSerializer

class BookUpdateApiViwe(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BoockSerializer

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BoockSerializer

class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BoockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            info = {
                'static': 'This book is saved to database',
                'book info':data
            }
            return Response(info)

class BookMixedApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BoockSerializer

