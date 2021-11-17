from django.shortcuts import render
from .models import Parameter
from .filters import DataFilter
from django.db import connection

def get_parameters(request):
    db_name = connection.settings_dict['NAME']
    parameters = Parameter.objects.all()
    myFilter = DataFilter(request.GET, queryset=parameters)
    parameters = myFilter.qs
    context = {'parameters':parameters,'myFilter':myFilter,'dbName':db_name}
    return render(request,'parameters/dashboard.html',context)
