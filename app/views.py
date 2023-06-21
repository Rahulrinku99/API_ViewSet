from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# Create your views here.

class ProductMVS(ViewSet):
    def list(self,request):
        PQS=Product.objects.all()
        PSD=ProductMS(PQS,many=True)
        return Response(PSD.data)
    
    def create(self,request):
        PSD=ProductMS(data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({"success":"Product is created"})
        return Response({"Failed":"Product is not created"})
    
    def retrieve(self,request,pk):
        PQS=Product.objects.get(pk=pk)
        PSD=ProductMS(PQS)
        return Response(PSD.data)

    def update(self,request,pk):
        PQS=Product.objects.get(pk=pk)
        PSD=ProductMS(PQS,data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({"success":"Product is updated"})
        return Response({"Failed":"Product is not updated"})
    
    def partial_update(self,request,pk):
        PQS=Product.objects.get(pk=pk)
        PSD=ProductMS(PQS,data=request.data,partial=True)
        if PSD.is_valid():
            PSD.save()
            return Response({"success":"Product is updated"})
        return Response({"Failed":"Product is not updated"})
    
    def destroy(self,request,pk):
        PQS=Product.objects.get(pk=pk).delete()
        return Response({"Delete":"Product is Delete"})
        
