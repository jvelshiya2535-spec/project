from rest_framework.decorators import api_view
from .serializer import Fileserializers
from rest_framework.response import Response
from rest_framework import status
from .models import file


@api_view(['POST'])
def create_file(request):
    email=request.data.get('email')
    number=request.data.get('phone_number')
    a=len(number)
    password=request.data.get('password')
    confirm=request.data.get('confirm')
    if file.objects.filter(email=email).exists():
        return Response({'message':'email already exists'},status=status.HTTP_400_BAD_REQUEST)
    if a!=10:
       return Response({'message':'please enter valid phone number'},status=status.HTTP_400_BAD_REQUEST)
    if file.objects.filter(phone_number=number).exists():
        return Response({'message':'number already exists'},status=status.HTTP_400_BAD_REQUEST)
    if password!=confirm:
        return Response({'message':'password does not match'},status=status.HTTP_400_BAD_REQUEST)
    serializer=Fileserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
def login_user(request):
    email=request.data.get('email')
    password=request.data.get('password')
    if file.objects.filter(email=email).exists():
        a=file.objects.filter(email=email).first()
        s=Fileserializers(a)
        if password==a.password:
            return Response({'message':'login successfully','data':s.data},status=status.HTTP_200_OK)
        else:
            return Response({'message':'password does not match'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'email not exists'},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_file(request):
    value=file.objects.all()
    serializer=Fileserializers(value,many=True)
    return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['PUT'])
def updatefile(request,pk):
    value=file.objects.get(pk=pk)
    serializer=Fileserializers(value,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data updated successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_file(request,pk):
    a=file.objects.get(pk=pk)
    a.delete()
    return Response({'message':'deleted successfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_file_id(request,pk):
    user=file.objects.get(pk=pk)
    serializer=Fileserializers(file)
    return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)




 

