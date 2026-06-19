from rest_framework.decorators import api_view
from .serializer import Authorserializers
from rest_framework.response import Response
from rest_framework import status
from .models import author


@api_view(['POST'])
def create_author(request):
    serializer=Authorserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_author(request):
    value=author.objects.all()
    serializer=Authorserializers(value,many=True)
    return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['PUT'])
def updateauthor(request,pk):
    value=author.objects.get(pk=pk)
    serializer=Authorserializers(value,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data updated successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_author(reques,pk):
    a=author.objects.get(pk=pk)
    a.delete()
    return Response({'message':'deleted successfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_author_id(request,pk):
    value=author.objects.get(pk=pk)
    serializer=Authorserializers(author)
    return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)



