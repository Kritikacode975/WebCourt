"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from client import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('login_check', views.login_check, name='login_check'),
    path('hello', views.hello, name='hello'),
    path('layout', views.layout, name='layout'),
    path('feedback', views.feedback, name='feedback'),
    path('appointment', views.appointment, name='appointment'),
    path('appointment_store', views.appointment_store, name='appointment_store'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio1', views.portfolio1, name='portfolio1'),
    path('portfolio2', views.portfolio2, name='portfolio2'),
    path('portfolio3', views.portfolio3, name='portfolio3'),
    path('read_more1', views.read_more1, name='read_more1'),
    path('read_more2', views.read_more2, name='read_more2'),
    path('read_more3', views.read_more3, name='read_more3'),
    path('read_more4', views.read_more4, name='read_more4'),
    path('read_more5', views.read_more5, name='read_more5'),
    path('read_more6', views.read_more6, name='read_more6'),
    path('payment', views.payment, name='payment'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('cases', views.cases, name='cases'),
    path('contact', views.contact, name='contact'),
    path('contact_store', views.contact_store, name='contact_store'),
    path('feedback_store', views.feedback_store, name='feedback_store'),
    path('view_details/<int:id>', views.view_details, name='view_details'),
    path('profile/<int:id>', views.profile, name='profile'),
    # path('layout', views.layout, name='layout'),
    # path('sidebar', views.sidebar, name='sidebar'),
    # path('header', views.header, name='header'),
    # path('footer', views.footer, name='footer'),
    # path('dashboard', views.dashboard, name='dashboard'),
    # path('table', views.table, name='table'),
    # path('form', views.form, name='form'),
    # path('calendar', views.calendar, name='calendar'),
    # path('add_doc', views.add_doc, name='add_doc'),
    # path('add_member', views.add_member, name='add_member'),
    # path('add_case', views.add_case, name='add_case'),
    # path('add_client', views.add_client, name='add_client'),
    # path('view', views.view, name='view'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('edit/<int:id>', views.edit, name='edit'),
    # path('update/<int:id>', views.update, name='update'),
    # path('view_cases', views.view_cases, name='view_cases'),
    # path('view_doc', views.view_doc, name='view_doc'),
    # path('view_feedback', views.view_feedback, name='view_feedback'),
    # path('view_appointment', views.view_appointment, name='view_appointment'),
    # path('view_member', views.view_member, name='view_member'),
    # path('view_client', views.view_client, name='view_client'),
    # path('login', views.login, name='login'),
    # path('store', views.store, name='store'),
]
