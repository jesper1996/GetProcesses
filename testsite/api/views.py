from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Processes
from .serializers import processesSerializer
from .services import deleteData, createProcesses

# API endpoint to empty database and get new processes
@api_view(['GET'])
def refreshData(request):
    deleteData()
    createProcesses()
    allProcesses = Processes.objects.all()
    serializer = processesSerializer(allProcesses, many = True)

    return Response(serializer.data)

# API endpoint to get the processes from the database
@api_view(['GET'])
def getData(request):
    allProcesses = Processes.objects.all()
    serializer = processesSerializer(allProcesses, many = True)
    
    return Response(serializer.data)