from django.http import request
from django.shortcuts import render

# Create your views here.

from Admin.models import Customer,Query,Employee
from Admin.serializers import CustomerSerializer,QuerySerializer,EmployeeSerializer
from rest_framework import status
import requests 
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json



#*********** Employee Management *********

def employeehome(request):
    return render(request,'homeemploye.html')

def search_view(request):
    return render(request,'searchemploye.html')

@csrf_exempt
def searchapi(request):
    try:
        getEmpCode=request.POST.get("empcode")
        getEmployee=Employee.objects.filter(empcode=getEmpCode)
        employee_serializer=EmployeeSerializer(getEmployee,many=True)
        return render(request,"searchemploye.html",{"data":employee_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")
########################
@csrf_exempt
def employee_details(request,fetchid):
    try:
        employees=Employee.objects.get(id=fetchid)
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

############################
def add_employe(request):
    return render(request,'addemploye.html')

@csrf_exempt
def employeeaddpage(request):
    if(request.method =="POST"):
        employee_serialize=EmployeeSerializer(data=request.POST)
        if (employee_serialize.is_valid()):
            employee_serialize.save()
            return redirect(view_employe)
            # return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialisation",status=status.HTTP_400_BAD_REQUEST)
            
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)


def view_employe(request):
    fetchdata=requests.get("http://localhost:8000/Admin/viewall/").json()
    return render(request,'viewemploye.html',{"data":fetchdata})



############################

def upd_view(request):
    return render(request,'updateemploye.html')
@csrf_exempt
def updatesearchapi(request):
    try:
        getEmpCode=request.POST.get("empcode")
        getEmployee=Employee.objects.filter(empcode=getEmpCode)
        employee_serializer=EmployeeSerializer(getEmployee,many=True)
        return render(request,"updateemploye.html",{"data":employee_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def update_data_read(request):
    getid=request.POST.get("newid")

    getname=request.POST.get("newname")
    getsalary=request.POST.get("newsalary")
    getaddress=request.POST.get("newaddress")
    getcode=request.POST.get("newempcode")
    getemailid=request.POST.get("newemailid")
    getphonenumber=request.POST.get("newphonenumber")
    getaadhaarno=request.POST.get("newaadhaarno")
    getgender=request.POST.get("newgender")
    getdoj=request.POST.get("newdoj")
    getdob=request.POST.get("newdob")
    getpincode=request.POST.get("newpincode")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword")
    mydata={'name':getname,'salary':getsalary,'id':getid,'address':getaddress,'empcode':getcode,'emailid':getemailid,'phonenumber':getphonenumber,'aadhaarno':getaadhaarno,
    'pincode':getpincode,'dateofjoining':getdoj,'dateofbirth':getdob,'gender':getgender,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://localhost:8000/Admin/viewemployee/"+getcode
    requests.put(Apilink,data=jsondata)
    return redirect(view_employe)
    # return HttpResponse("data updated successfully")

###################

def del_view(request):
    return render(request,'deleteemploye.html')

@csrf_exempt
def delete_data_read(request):

    getnewid=request.POST.get("newid")
    Apilink="http://localhost:8000/Admin/viewemployee/" + getnewid
    requests.delete(Apilink)
    return redirect(view_employe)
    # return HttpResponse("data deleted successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getEmpCode=request.POST.get("empcode")
        getEmployee=Employee.objects.filter(empcode=getEmpCode)
        employee_serializer=EmployeeSerializer(getEmployee,many=True)
        return render(request,"deleteemploye.html",{"data":employee_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")








#*********** Customer Management***********

@csrf_exempt
def addcustomer(request):
    if(request.method=="POST"):
        print(request.POST)
        # mydata=JSONParser().parse(request)
        customer_serial=CustomerSerializer(data=request.POST)
        if(customer_serial.is_valid()):
            customer_serial.save()
            return redirect(viewall)
            # return JsonResponse(customer_serial.data)
        else:
            return HttpResponse("error in serialization")

    else:
        return HttpResponse("sucess")

@csrf_exempt
def view_all(request):
    if(request.method=="GET"):
        c1=Customer.objects.all()
        customer_serial=CustomerSerializer(c1,many=True)
        return JsonResponse(customer_serial.data,safe=False)

@csrf_exempt
def viewcustomer(request,fetchid):
    try:
        c1=Customer.objects.get(id=fetchid)
        if(request.method=="GET"):
            customer_serial=CustomerSerializer(c1)
            return JsonResponse(customer_serial.data,safe=False)

        if(request.method=="DELETE"):
            c1.delete()
            return HttpResponse("Deleted",status=status)

        if(request.method=="PUT"):
            cdata=JSONParser().parse(request)
            customer_serial=CustomerSerializer(c1,data=cdata)
            if (customer_serial.is_valid()):
                customer_serial.save()
                return JsonResponse(customer_serial.data)
            else:
                return JsonResponse(customer_serial.errors)
    except Customer.DoesNotExist:
        return HttpResponse("invalid syntax")


def homecustomer(request):
    return render(request,'homecustomer.html')

def header(request):
    return render(request,"headercustomer.html")

def add_c(request):
    return render(request,"addcustomer.html")


def viewall(request):
    fetchdata=requests.get("http://127.0.0.1:8000/Admin/viewallcustomer/").json()
    return render(request,"viewcustomer.html",{"data":fetchdata})


def search(request):
    return render(request,"searchcustomer.html")

@csrf_exempt
def search_api(request):
    try:
        getno=request.POST.get("mobileno")
        getmobileno=Customer.objects.filter(mobileno=getno)
        customer_serial=CustomerSerializer(getmobileno,many=True)
        return render(request,"searchcustomer.html",{"data":customer_serial.data})
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


def update(request):
    return render(request,"updatecustomer.html")

@csrf_exempt
def update_api(request):
    try:
        getno=request.POST.get("mobileno")
        getmobileno=Customer.objects.filter(mobileno=getno)
        customer_serial=CustomerSerializer(getmobileno,many=True)
        return render(request,"updatecustomer.html",{"data":customer_serial.data})
        # return JsonResponse(event_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_data(request):
    getnewid=request.POST.get("newid")

    getnewname=request.POST.get("newname")
    getnewDOB=request.POST.get("newDOB")
    getnewusername=request.POST.get("newusername")
    getnewpassword=request.POST.get("newpassword")
    getnewpurchase_date=request.POST.get("newpurchase_date")
    getnewproduct_type=request.POST.get("newproduct_type")
    getnewgender=request.POST.get("newgender")
    getnewaddress=request.POST.get("newaddress")
    getnewpincode=request.POST.get("newpincode")
    getnewmobileno=request.POST.get("newmobileno")
    getnewemail=request.POST.get("newemail")
    getnewadharno=request.POST.get("newadharno")
    
    mydata={'purchase_date':getnewpurchase_date,'DOB':getnewDOB,'password':getnewpassword,'username':getnewusername,'product_type': getnewproduct_type,
    'id':getnewid,'name':getnewname,'gender':getnewgender,'address':getnewaddress,'pincode':getnewpincode,'mobileno':getnewmobileno,'email':getnewemail,'adharno':getnewadharno}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/Admin/viewcustomer/"+ getnewid
    requests.put(Apilink,data=jsondata)
    return redirect(viewall)
    # return HttpResponse("data has updated sucessfully")

def delete(request):
    return render(request,"deletecustomer.html")

@csrf_exempt
def delete_api(request):
    try:
        getno=request.POST.get("mobileno")
        getmobileno=Customer.objects.filter(mobileno=getno)
        customer_serial=CustomerSerializer(getmobileno,many=True)
        return render(request,"deletecustomer.html",{"data":customer_serial.data})
        # return JsonResponse(event_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def delete_data(request):
    getnewid=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/Admin/viewcustomer/"+ getnewid
    requests.delete(Apilink)
    return redirect(viewall)
    # return HttpResponse("data has deleted sucessfully")

def view_connection(request):
    return render(request,"viewconnection.html")

@csrf_exempt
def view_api(request):
    try:
        getno=request.POST.get("purchase_date")
        getdateno=Customer.objects.filter(purchase_date=getno)
        customer_serial=CustomerSerializer(getdateno,many=True)
        return render(request,"viewconnection.html",{"data":customer_serial.data})
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


def view_today(request):
    return render(request,"viewdate.html")

@csrf_exempt
def view_todayapi(request):
    try:
        getno=request.POST.get("purchase_date")
        getdateno=Customer.objects.filter(purchase_date=getno)
        customer_serial=CustomerSerializer(getdateno,many=True)
        return render(request,"viewdate.html",{"data":customer_serial.data})
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")



def product(request):
    return render(request,"viewproduct.html")

@csrf_exempt
def product_api(request):
    try:
        getno=request.POST.get("product_type")
        getmobileno=Customer.objects.filter(product_type=getno)
        customer_serial=CustomerSerializer(getmobileno,many=True)
        return render(request,"viewproduct.html",{"data":customer_serial.data})
        # return JsonResponse(flat_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")










#**************Admin main**********


def home(request):
    return render(request,'home.html')

def login_page(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')





#************** Customer Query**********

@csrf_exempt
def addQuery(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        query_serialize=QuerySerializer(data=request.POST)
        if(query_serialize.is_valid()):
            query_serialize.save()
            return redirect(viewQuerys)
            #return JsonResponse(query_serialize.data,status=status.HTTP_200_OK)

        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewQuery(request):
    if(request.method=="GET"):
        quries=Query.objects.all()
        query_serialize=QuerySerializer(quries,many=True)
        return JsonResponse(query_serialize.data,safe=False)

def homeQuery(request):
    return render(request,'homequery.html')

def QueryAdd(request):
    return render(request,'queryregister.html')

def viewQuerys(request):
    fetchdata=requests.get("http://127.0.0.1:8000/Admin/viewall/").json()
    return render(request,'queryview.html',{"data":fetchdata})

def searchQuerys(request):
    return render(request,'querysearch.html')

def Feedbacksearch(request):
    return render(request,'searchfeedback.html')

def Questionssearch(request):
    return render(request,'searchquestion.html')

def Complaintssearch(request):
    return render(request,'searchcomplaint.html')

def updateToCustomer(request):
    return render(request,'querysolution.html')


@csrf_exempt
def searchapi(request):
    try:
        getdate=request.POST.get("date")
        getQuery=Query.objects.filter(date=getdate)
        query_serialize=QuerySerializer(getQuery,many=True)
        return render(request,"querysearch.html",{"data":query_serialize.data})
        #return JsonResponse(query_serialize.data,safe=False)
    except Query.DoesNotExist:
        return HttpResponse("Invalid Date")

    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def searchFeedback(request):
    try:
        getFeedback=request.POST.get("selectquery")
        getQuery=Query.objects.filter(selectquery=getFeedback)
        query_serialize=QuerySerializer(getQuery,many=True)
        return render(request,"searchfeedback.html",{"data":query_serialize.data})
        #return JsonResponse(query_serialize.data,safe=False)
    except Query.DoesNotExist:
        return HttpResponse("Invalid input")

    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def searchQuestions(request):
    try:
        getQuestions=request.POST.get("selectquery")
        getQuery=Query.objects.filter(selectquery=getQuestions)
        query_serialize=QuerySerializer(getQuery,many=True)
        return render(request,"searchquestion.html",{"data":query_serialize.data})
        #return JsonResponse(query_serialize.data,safe=False)
    except Query.DoesNotExist:
        return HttpResponse("Invalid input")

    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def searchComplaints(request):
    try:
        getComplaints=request.POST.get("selectquery")
        getQuery=Query.objects.filter(selectquery=getComplaints)
        query_serialize=QuerySerializer(getQuery,many=True)
        return render(request,"searchcomplaint.html",{"data":query_serialize.data})
        #return JsonResponse(query_serialize.data,safe=False)
    except Query.DoesNotExist:
        return HttpResponse("Invalid input")

    except:
        return HttpResponse("something went wrong")


