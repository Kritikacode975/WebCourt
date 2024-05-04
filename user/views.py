from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from adminlawyer.models import *

def layout(request):
	context = {}
	return render(request,'user/layout.html',context)

def contact(request):
    result = Cases.objects.all()
    context = {'result':result}
    return render(request,'user/contact.html',context)

def about(request):
	context = {}
	return render(request,'user/about.html',context)



def contactus(request):
	context = {}
	return render(request,'user/contactus.html',context)

def cases(request):
	context = {}
	return render(request,'user/cases.html',context)


def appointment(request):
	context = {}
	return render(request,'user/appointment.html',context)


def header(request):
	context = {}
	return render(request,'user/header.html',context)

def sidebar(request):
	context = {}
	return render(request,'sidebar.html',context)

def footer(request):
	context = {}
	return render(request,'user/footer.html',context)

def home(request):
	context = {}
	return render(request,'user/home.html',context)

def table(request):
	context = {}
	return render(request,'staff/table.html',context)

def form(request):
	context = {}
	return render(request,'staff/form.html',context)

# def calendar(request):
# 	context = {}
# 	return render(request,'staff/calendar.html',context)

def add_case(request):
	context = {}
	return render(request,'staff/add_case.html',context)

def add_client(request):
	context = {}
	return render(request,'staff/add_client.html',context)

def add_doc(request):
	context = {}
	return render(request,'staff/add_doc.html',context)

def add_member(request):
	context = {}
	return render(request,'staff/add_member.html',context)

def view_cases(request):
	context = {}
	return render(request,'staff/view_cases.html',context)

def view_client(request):
	result = Client.objects.all()
	context = {'result':result}
	return render(request, 'staff/view_client.html',context)

def view_doc(request):
	context = {}
	return render(request,'staff/view_doc.html',context)

def view_member(request):
	context = {}
	return render(request,'staff/view_member.html',context)

def view_feedback(request):
	context = {}
	return render(request,'staff/view_feedback.html',context)

def view_appointment(request):
	context = {}
	return render(request,'staff/view_appointment.html',context)
	
def login(request):
	context = {}
	return render(request,'staff/login.html',context)
	
def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    result = auth.authenticate(request, username=username, password=password)

    if result is None:
        print('Invalid Username Or Password')
        return redirect('/client/login')
    else:
        auth.login(request, result)
        return redirect('/client/home')


def logout(request):
    auth.logout(request)
    return redirect('/client/login')

def store(request):
	case_title = request.POST['title']
	description = request.POST['description']
	case_type = request.POST['type']
	fir_copy = request.POST['fircopy']
	lname = request.POST['lname']
	cname = request.POST['cname']
	
	city = request.POST['city']
	state = request.POST['state']
	zipcode = request.POST['zipcode']

	police_station = request.POST['policestation']
	case_status = request.POST['status']
	rdate = request.POST['rdate']

	Case.objects.create(casetitle = case_title, description = description, casetype = case_type, 
	fircopy = fir_copy, lawyername = lname, clientname = cname, 
	 zipcode = zipcode,police_station = police_station, case_status = case_status)
	return redirect('/staff/add_case')

def view(request):
	pass

# def read(request):
#     result = Case.objects.all()
#     context = {'result':result}
#     return render(request, '/staff/view_case.html',context)


def delete(request,id):
	result = Case.objects.get(pk=id)
	result.delete()
	return redirect('/staff/view_case')


def edit(request,id):
	result  = Case.objects.get(pk=id)
	city = City.objects.all()
	state = State.objects.all()
	context = {'result':result,'city':city,'state':state}
	return render(request, 'staff/update_case.html',context)


def update(request,id):
	data = {
				'case_title'  : request.POST['title'],
				'description' : request.POST['description'],
				'case_type'   : request.POST['type'],
				'fir_copy' 	  : request.POST['fircopy'],
				'lname'       : request.POST['lname'],
				'cname' 	  : request.POST['cname'],
	
				'city' 	      : request.POST['city'],
				'state'       : request.POST['state'],
				'zipcode'     : request.POST['zipcode'],

				'police_station' : request.POST['policestation'],
				'case_status '   : request.POST['status'],
				'rdate'          : request.POST['rdate'],
		   }
	Case.objects.update_or_create(pk=id, defaults=data)
	return redirect('/staff/view_case')