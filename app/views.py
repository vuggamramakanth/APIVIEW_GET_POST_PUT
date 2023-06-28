from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework import status

class ProductCrud(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)
    

    def post(self,request):
        pmsd=ProductSerializer(data=request.data)
        if pmsd.is_valid():
            spo=pmsd.save()
            return Response({'message':'product is created'})
        else:
            return Response({'faild':'product is not created'})
      
    def put(self,request,pid):
        productobject=product.objects.get(pid=pid)
        PMSD=ProductSerializer(productobject,data=request)     
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message':'product is updated'})
        else:
            return Response({'failed':'product update is failed'})










    