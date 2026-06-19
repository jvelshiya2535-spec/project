from django.shortcuts import render
from rest_framework .decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import book
from .serializer import Bookserializer,BookAuthor
from author .models import author
from django.db.models import Count

# Create your views here.
@api_view(['POST'])
def create_book(request):
    serializer=Bookserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data created','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_book(request):
    value=book.objects.all()
    serializer=BookAuthor(value,many=True)
    return Response({"message":"data fetched succesffully","data":serializer.data},status=status.HTTP_200_OK)


@api_view(['GET'])
def get_book(request):
    book_author=request.query_params.get('author')
    value=book.objects.all()
    if book_author:
        value=value.filter(author__name__exact=book_author)
    serializer=BookAuthor(value,many=True)
    return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_bookbyyear(request):
    value=book.objects.all()
    value=value.filter(published_date__year=2008)
    serializer=BookAuthor(value,many=True)
    return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_bookbytitle(request):
    value=book.objects.filter(title__exact="Clean Code")
    serializer=Bookserializer(value,many=True)
    return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_bookbyprice(request):
    value=book.objects.all()
    value=value.filter(price__gt=750)
    serializer=Bookserializer(value,many=True)
    return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_bookbyrange(request):
    value=book.objects.all()
    value=value.filter(price__range=(800,950))
    serializer=Bookserializer(value,many=True)
    return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_bookbyauthor(request):
    value=author.objects.annotate(book_count=Count('book')).filter(book_count__gt=1)
    data=[
        {
            "author_name": hello.name,
            "book_count": hello.book_count
        }
        for hello in value
    ]
    return Response({'message':'data fetched successfully','data':data},status=status.HTTP_200_OK)




@api_view(['PUT'])    
def updatebook(request,pk):
    book=book.objects.all()
    serializer=Bookserializer(book,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data updated successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_book(request,pk):
    serializer=book.objects.get(pk=pk)
    serializer.save()
    return Response({'message':'deleted successfully'},ststus=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_book_id(request,pk):
    book=book.objects.get(pk=pk)
    serializer=Bookserializer(book)
    return Response({'message':'datas fetched successfully','data':serializer.data},status=status.HTTP_200_OK)

