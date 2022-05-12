from main.models import Processes
import subprocess

def createProcesses():
    # Getting the processes
    process_List = subprocess.check_output('powershell.exe Get-Process', shell=True)
    a = str(process_List)
    # splitting the string for each line
    list = a.split("\\r\\n")
    
    counter = 0
    # for each element/row in our list, create a new processes object 
    for x in list:
        # removing some unnecessary elements/rows
        if counter > 2 and x != "" and counter+1 != len(list):
            y = stringToJson(x)
            Processes.objects.create(processData = y)
            
        counter += 1


# Deletes the data in the database
def deleteData():
    Processes.objects.all().delete()


# converts each line into JSON format  
def stringToJson(x):
    temp = {}

    data = x.split()
    temp["Handles"] = data[0]
    temp["NPM(K)"] = data[1]
    temp["PM(K)"] = data[2]
    temp["WS(K)"] = data[3]
    if len(data) < 8:
        temp["CPU"] = ""
        temp["ID"] = data[4]
        temp["SI"] = data[5]
        temp["ProcessName"] = data[6]
    else:
        temp["CPU"] = data[4]
        temp["ID"] = data[5]
        temp["SI"] = data[6]
        if len(data) > 8:
            tempstring = ""
            for i in range(7, len(data)):
                tempstring += data[i] + " " 
            temp["ProcessName"] = tempstring
        else:
            temp["ProcessName"] = data[7]

    return temp