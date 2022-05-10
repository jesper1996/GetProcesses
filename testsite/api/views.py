from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Processes
from .serializers import processesSerializer
import subprocess


# API endpoint to get processes and empty database
@api_view(['GET'])
def getData(request):
    #Processes.objects.filter(id > 0).delete()
    Processes.objects.filter(for_delete= "test").delete()
    process_List = subprocess.check_output('powershell.exe Get-Process', shell=True)
    Processes.objects.create(name = process_List, for_delete = "test")
    allProcesses = Processes.objects.all()
    serializer = processesSerializer(allProcesses, many = True)
    

    return Response(serializer.data)

