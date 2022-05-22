from multiprocessing import managers
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from EmployeeApp.models import Departments , Employee
from EmployeeApp.serializers import DepartmentSerializer , EmployeeSerializer
# Create your views here.


@csrf_exempt
def departmentApi(request , id=0):
    # Get Data from database
    if request.method == 'GET':
        department = Departments.objects.all()
        department_Serializer = DepartmentSerializer(department , many = True) # convert into json format using serializer
        return JsonResponse(department_Serializer.data , safe=False) 

    # Add 
    elif request.method == 'POST':
        department_data = JSONParser().parse(request) #parsing request
        department_Serializer = DepartmentSerializer(data=department_data) # convert into  model using serializer
        if department_Serializer.is_valid():
            department_Serializer.save() # save into database 
            return JsonResponse("Added Successfully" , safe= False)

    # Update
    elif request.method == 'PUT': #update a record
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])#capturing existing record
        department_Serializer = DepartmentSerializer(department , data=department_data) #convert into model
        if department_Serializer.is_valid():
            department_Serializer.save() # save into database 
            return JsonResponse("Update Successfully" , safe= False)
        return JsonResponse("Update Failed" )
    
    # Delete
    elif request.method == 'DELETE': #update a record
        department = Departments.objects.get(DepartmentId = id)#Delete the id
        department.delete()
        return JsonResponse("Deleted Successfully" , safe=False)

