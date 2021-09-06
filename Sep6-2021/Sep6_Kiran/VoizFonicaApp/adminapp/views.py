from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from adminapp.serializers import QuerySerializer
from adminapp.models import Query
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests,json
from django.shortcuts import redirect
# Create your views here.
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


def QueryAdd(request):
    return render(request,'register.html')

def viewQuerys(request):
    fetchdata=requests.get("http://127.0.0.1:8000/adminapp/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})

def searchQuerys(request):
    return render(request,'search.html')

def Feedbacksearch(request):
    return render(request,'searchfeedback.html')

def Questionssearch(request):
    return render(request,'searchquestion.html')

def Complaintssearch(request):
    return render(request,'searchcomplaint.html')


@csrf_exempt
def searchapi(request):
    try:
        getdate=request.POST.get("date")
        getQuery=Query.objects.filter(date=getdate)
        query_serialize=QuerySerializer(getQuery,many=True)
        return render(request,"search.html",{"data":query_serialize.data})
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
