from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from employeeapp.serializers import EmployeeSerializer
import json
from employeeapp.models import Employee
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


@csrf_exempt
def searchapi(request):
    try:
        getEmpCode=request.POST.get("empcode")
        getEmployee=Employee.objects.filter(empcode=getEmpCode)
        employee_serializer=EmployeeSerializer(getEmployee,many=True)
        return render(request,"search.html",{"data":employee_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def employee_details(request,empcode):
    try:
        employees=Employee.objects.get(empcode=empcode)
        if (request.method=="GET"):
            employee_serializer=EmployeeSerializer(employees)
            return JsonResponse(employee_serializer.data,safe=False)
        if(request.method=="PUT"):
            mydict=JSONParser().parse(request)
            employee_serialize=EmployeeSerializer(employees,data=mydict)
            if (employee_serialize.is_valid()):
                employee_serialize.save()
                return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(employee_serialize.data,status=status.HTTP_400_BAD_REQUEST)

        if(request.method=="DELETE"):
            employees.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except Employee.DoesNotExist:
        return HttpResponse("Invalid employee id",status=status.HTTP_404_NOT_FOUND)




@csrf_exempt
def employee_list(request):
    if (request.method=="GET"):
        employees=Employee.objects.all()
        employee_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employee_serializer.data,safe=False)



@csrf_exempt
def employeeaddpage(request):
    if(request.method =="POST"):
        # getname=request.POST.get("name")
        # getempcode=request.POST.get("empcode")
        # getaddress=request.POST.get("address")
        # getsalary=request.POST.get("salary")
        # getdob=request.POST.get("dateofbirth")
        # getdoj=request.POST.get("dateofjoining")
        # getaadhaarno=request.POST.get("aadhaarno")
        # getgender=request.POST.get("gender")
        # getpincode=request.POST.get("pincode")
        # getusername=request.POST.get("username")
        # getpassword=request.POST.get("password")
        # mydict={"name":getname,"empcode":getempcode,"address":getaddress,"salary":getsalary,"dateofbirth":getdob,"dateofjoining":getdoj,"aadhaarno":getaadhaarno,"gender":getgender,"pincode":getpincode,"username":getusername,"password":getpassword}
        # result=json.dumps(mydict)
        # return HttpResponse(result)
        #mydict=JSONParser().parse(request)
        employee_serialize=EmployeeSerializer(data=request.POST)
        if (employee_serialize.is_valid()):
            employee_serialize.save()
            return redirect(emp_view)
            #return HttpResponse("success")
            # return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialisation",status=status.HTTP_400_BAD_REQUEST)
            
        # return HttpResponse(result)
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)
def employee_view(request):
    return render(request,'index1.html')
def emp_view(request):
    fetchdata=requests.get("http://localhost:8000/employee/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})
    #return render(request,'viewall.html')
def upd_view(request):
    return render(request,'update.html')
def del_view(request):
    return render(request,'delete.html')
def search_view(request):
    return render(request,'search.html')
@csrf_exempt
def updatesearchapi(request):
    try:
        getEmpCode=request.POST.get("empcode")
        getEmployee=Employee.objects.filter(empcode=getEmpCode)
        employee_serializer=EmployeeSerializer(getEmployee,many=True)
        return render(request,"update.html",{"data":employee_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def update_data_read(request):
    getname=request.POST.get("newname")
    getid=request.POST.get("newid")
    getsalary=request.POST.get("newsalary")
    getaddress=request.POST.get("newaddress")
    getcode=request.POST.get("newempcode")
    getemailid=request.POST.get("newemaiid")
    getphonenumber=request.POST.get("newphonenumber")
    getaadhaarno=request.POST.get("newaadhaarno")
    getgender=request.POST.get("newgender")
    getdoj=request.POST.get("newdoj")
    getdob=request.POST.get("newdob")
    getpincode=request.POST.get("newpincode")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword")
    mydata={'name':getname,'salary':getsalary,'id':getid,'address':getaddress,'empcode':getcode,'emailid':getemailid,'phonenumber':getphonenumber,'aadhaarno':getaadhaarno,'pincode':getpincode,'dateofjoining':getdoj,'dateofbirth':getdob,'gender':getgender,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    Apilink="http://localhost:8000/employee/viewemployee/"+getcode
    requests.put(Apilink,data=jsondata)
    return redirect(emp_view)
    # return HttpResponse("data updated successfully")


@csrf_exempt
def delete_data_read(request):

    getnewid=request.POST.get("newid")
    Apilink="http://localhost:8000/employee/viewemployee/" + getnewid
    requests.delete(Apilink)
    return HttpResponse("data deleted successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getEmpCode=request.POST.get("empcode")
        getEmployee=Employee.objects.filter(empcode=getEmpCode)
        employee_serializer=EmployeeSerializer(getEmployee,many=True)
        return render(request,"delete.html",{"data":employee_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")




