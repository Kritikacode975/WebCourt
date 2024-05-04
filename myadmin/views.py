from django.shortcuts import render
from django.http import HttpResponse

def layout(request):
	context = {}
	return render(request,'adminlawyer/layout.html',context)

def header(request):
	context = {}
	return render(request,'adminlawyer/header.html',context)

def sidebar(request):
	context = {}
	return render(request,'adminlawyer/sidebar.html',context)

def footer(request):
	context = {}
	return render(request,'adminlawyer/footer.html',context)

def dashboard(request):
	context = {}
	return render(request,'adminlawyer/dashboard.html',context)

def table(request):
	context = {}
	return render(request,'adminlawyer/table.html',context)

def form(request):
	context = {}
	return render(request,'adminlawyer/form.html',context)

def calendar(request):
	context = {}
	return render(request,'adminlawyer/calendar.html',context)

def add_case(request):
	context = {}
	return render(request,'adminlawyer/add_case.html',context)

def add_client(request):
	context = {}
	return render(request,'adminlawyer/add_client.html',context)

def add_doc(request):
	context = {}
	return render(request,'adminlawyer/add_doc.html',context)

def add_member(request):
	context = {}
	return render(request,'adminlawyer/add_member.html',context)

def view_cases(request):
	context = {}
	return render(request,'adminlawyer/view_cases.html',context)

def view_client(request):
	context = {}
	return render(request,'adminlawyer/view_client.html',context)

def view_doc(request):
	context = {}
	return render(request,'adminlawyer/view_doc.html',context)

def view_member(request):
	context = {}
	return render(request,'adminlawyer/view_member.html',context)

def view_feedback(request):
	context = {}
	return render(request,'adminlawyer/view_feedback.html',context)

def view_appointment(request):
	context = {}
	return render(request,'adminlawyer/view_appointment.html',context)
	
def login(request):
	context = {}
	return render(request,'adminlawyer/login.html',context)