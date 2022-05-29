import logging
from msilib.schema import Class
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Member,Fund
from .serializers import MemberSerializer,FundSerializer

@csrf_exempt
def fundservice(request,fund_id=0):
    if request.method == 'GET':
        Fund_data = Fund.objects.all()
        Fund_serialized = FundSerializer(Fund_data, many=True)
        return JsonResponse(Fund_serialized.data, safe=False)

    elif request.method == 'POST':
        Fund_data = JSONParser().parse(request)
        logging.info(Fund_data)
        Fund_serialized = FundSerializer(data=Fund_data)
        logging.info(Fund_serialized)
        if Fund_serialized.is_valid():
            Fund_serialized.save()
            return JsonResponse("Success Adding", safe=False)
        return JsonResponse("Failed Adding data", safe=False)  
    
    elif request.method == "PUT":
        Fund_data = JSONParser().parse(request)
        Funds = Fund.objects.get(Fund_id=Fund_data["Fund_id"])
        Fund_serialized = FundSerializer(Funds,data=Fund_data)
        if Fund_serialized.is_valid():
            Fund_serialized.save()
            return JsonResponse("Success updateting", safe=False)
        return JsonResponse("Failed updateting data", safe=False) 

    elif request.method == "DELETE":
        Fund_data = Fund.objects.get(Fund_id=fund_id)
        Fund_data.delete()
        return JsonResponse("Success Deletion", safe=False)

@csrf_exempt
def memberservice(request,member_id=0):
    if request.method == 'GET':
        Member_data = Member.objects.all()
        Member_serialized = MemberSerializer(Member_data, many=True)
        return JsonResponse(Member_serialized.data, safe=False)

    elif request.method == 'POST':
        Member_data = JSONParser().parse(request)
        logging.info(Member_data)
        Member_serialized = MemberSerializer(data=Member_data)
        logging.info(Member_serialized)
        if Member_serialized.is_valid():
            Member_serialized.save()
            return JsonResponse("Success Adding", safe=False)
        return JsonResponse("Failed Adding data", safe=False)  
    
    elif request.method == "PUT":
        Member_data = JSONParser().parse(request)
        Members = Member.objects.get(Member_id=Member_data["Member_id"])
        Member_serialized = MemberSerializer(Members,data=Member_data)
        if Member_serialized.is_valid():
            Member_serialized.save()
            return JsonResponse("Success updateting", safe=False)
        return JsonResponse("Failed updateting data", safe=False) 

    elif request.method == "DELETE":
        Member_data = Member.objects.get(Member_id=member_id)
        Member_data.delete()
        return JsonResponse("Success Deletion", safe=False)
 