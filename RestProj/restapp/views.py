from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
import io

# Create your views here.
@api_view(['GET'])
def get_book(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many=True)
    response = {'status':200, 'payload':serializer.data}
    return Response(response)

"""
@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    if student_obj:
        serializer = StudentSerializer(student_obj, many=True)    
        response = {
            'status': 200,
            'payload': serializer.data
        }
        return Response(response)
    return Response({'status':500, 'message': 'No any record'})


@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        # body = request.body
        # stream = io.BytesIO(body)
        # parsed_data = JSONParser().parse(stream)
        # print(parsed_data)
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            response = {'status':200, 'message':'data saved successfully..'}
        else:
            response = {'status':403, 'error':serializer.errors, "message":"Something went wrong"}
        return Response(response)
  
@api_view(['PUT', 'PATCH'])
def update_student(request, id):
    if request.method == 'PUT':
        try:
            student_obj = Student.objects.get(id = id)
            serializer = StudentSerializer(student_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = {"status":200, 'message': "Data Updated Successfully"}
                return Response(response)
            else:
                return Response({'error': serializer.errors})
        except Exception as e:
            return Response({'status':403, 'message': 'Invalid id'})
    
    if request.method == 'PATCH':
        try:
            student_obj = Student.objects.get(id = id)
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response = {"status":200, 'message': "Data Updated Successfully"}
                return Response(response)
            else:
                return Response({'error': serializer.errors})
        except Exception as e:
            return Response({'status':403, 'message': 'Invalid id'})
    
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id = id)
        student_obj.delete()
        response = {"status":200, 'message': "Record Deleted Successfully"}
        return Response(response)
    except Exception as e:
        return Response({'status':403, 'message': 'Invalid id'})
"""


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'error':serializer.errors})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)

        return Response({'status':200, 'payload':serializer.data, 'token':str(token_obj), 'message':'user successfully registered'})
            
        
    

class StudentAPI(APIView):
    """Authentication validators"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        print(request.user)
        student_obj = Student.objects.all()
        if student_obj:
            serializer = StudentSerializer(student_obj, many=True)    
            response = {
                'status': 200,
                'payload': serializer.data
            }
            return Response(response)
        return Response({'status':500, 'message': 'No any record'})


    def post(self, request):
        data = request.data
        print(data)
        # body = request.body
        # stream = io.BytesIO(body)
        # parsed_data = JSONParser().parse(stream)
        # print(parsed_data)
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            response = {'status':200, 'message':'data saved successfully..'}
        else:
            response = {'status':403, 'error':serializer.errors, "message":"Something went wrong"}
        return Response(response)

    def put(self, request):
        try:
            id = request.data['id']
            student_obj = Student.objects.get(id = id)
            serializer = StudentSerializer(student_obj, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                response = {"status":200, 'message': "Data Updated Successfully"}
                return Response(response)
            else:
                return Response({'error': serializer.errors})
        except Exception as e:
            return Response({'status':403, 'message': 'Invalid id'})


    def patch(self, request):
        try:
            id = request.data['id']
            student_obj = Student.objects.get(id = id)
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response = {"status":200, 'message': "Data Updated Successfully"}
                return Response(response)
            else:
                return Response({'error': serializer.errors})
            
        except Exception as e:
            return Response({'status':403, 'message': 'Invalid id'})

    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.get(id = id)
            student_obj.delete()
            response = {"status":200, 'message': "Record Deleted Successfully"}
            return Response(response)
        except Exception as e:
            return Response({'status':403, 'message': 'Invalid id'})
        
