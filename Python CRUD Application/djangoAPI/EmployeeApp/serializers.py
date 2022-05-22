# USed to convert django models into json format 

from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from EmployeeApp.models import Departments , Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId' , 'DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeId' , 'EmployeeName' , 'Department' , 'DateOfJoining' , 'PhotoFile')