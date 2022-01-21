from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes

@csrf_exempt
def signup(request):
	return render(request,'signup.html')	

@csrf_exempt
def index(request):
	a=Product.objects.all()
	return render(request,'index.html',{"Product":a})	

@csrf_exempt
def select(request):
	a=Product.objects.all()
	return render(request,'select.html')
	
@csrf_exempt
def savesignup(request):
		a=request.POST.get("customerid")
		b=request.POST.get("customername")
		c=request.POST.get("apassword")

		obj=Customer(customer_id=a,customer_name=b,password=c)
		obj.save()
		msg="Customer Detail Saved"
		return HttpResponse(msg)	

@csrf_exempt
def login(request):
	return  render(request,'login.html')

@csrf_exempt
def main(request):
	return  render(request,'main.html')	

@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def savelogin(request):
	a=request.POST.get('customerid')
	b=request.POST.get('apassword')

	obj = Customer.objects.filter(customer_id=a,password=b)
	#obj=auth.authenticate(username=a,password=b)
	if obj:
		return render(request,'main.html')
	else:
		return HttpResponse('Fail')	

@csrf_exempt
def showproduct(request):	
	if request.method=="POST":
		a=request.POST.get('productid')
		b=request.POST.get('cat')
		result=Product.objects.raw('select * from Product where product_id="'+a+'"')
		#result=Product.objects.raw('select * from Product where product_id="'+a+'" OR product_cat="'+b+'"')
		return render(request,'select.html',{"Product":result})			
	else:
		res=Product.objects.raw('select * from Product')
		return HttpResponse(request,'select.html',{"Product":res})

@csrf_exempt
def showcat(request):
	if request.method=="POST":
		b=request.POST.get('cat')
		res=Product.objects.filter(product_cat=b)
		if res:
			return render(request,'select.html',{"Product":res})	
		else:
			return HttpResponse('Select valid category or product id')		

def showdata(request):
	obj=Product.objects.all()
	msg="<table width='100%' border='1'>"
	msg=msg+'<tr>'
	msg=msg+'<td> Product Cat</td>'
	msg=msg+'<td> Product ID </td>'
	msg=msg+'<td> Product Name </td>'
	msg=msg+'<td> Product Prize </td>'
	msg=msg+'<td> Product Discription</td>'
	msg=msg+'</tr>'
	for x in obj:
		msg=msg+'<tr>'
		msg=msg+'<td>'+x.product_cat+'</td>'
		msg=msg+'<td>'+ x.product_id +'</td>'
		msg=msg+'<td>' +x.product_name+'</td>'
		msg=msg+'<td>' +x.product_prize+'</td>'
		msg=msg+'<td>'+x.product_discription+'</td>'
		msg=msg+'</tr>'
	msg=msg+'<table>'
	return HttpResponse(msg)			

