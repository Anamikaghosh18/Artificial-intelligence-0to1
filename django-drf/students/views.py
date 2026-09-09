from django.shortcuts import render
from django.http import HttpResponse
from students.models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def home(request):
    return HttpResponse("<h2> This is web api testing </h2>")

# def student_details(request):
#     students = Students.objects.all()

#     # json thinks we are passing a dict so we need to chnage into list ---> manual serialization
#     # student_list = list(students.values())

   
#     return JsonResponse(student_list, safe=False)


# function based view 
@api_view(['GET', 'POST'])
def studentView(request):
    if request.method == 'GET':
        # get all the data from student table 
        students = Students.objects.all()

        serializer = StudentSerializer(students, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)
     
    elif request.method == 'POST':
        serializer = StudentSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data = request.data) # prepopulate the data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



