from django.db import models
from django.contrib.auth.models import User
from datetime import date

# State Table
class State(models.Model):
	state_name = models.CharField(max_length=50)

	class Meta:
		db_table='state'

	def __str__(self):
		return self.state_name



# City Table
class City(models.Model):
	city_name = models.CharField(max_length=50)
	state     = models.ForeignKey(State,on_delete=models.DO_NOTHING)

	class Meta:
		db_table='city'

	def __str__(self):
		return self.city_name



# Lawyer Table
class Lawyer(models.Model):
	lawyer_name 	   = models.CharField(max_length=50)
	username           = models.CharField(max_length=20)
	email		       = models.CharField(max_length=50)
	password           = models.CharField(max_length=20)
	dob			       = models.DateField()
	age			       = models.IntegerField()
	gender			   = models.CharField(max_length=10)
	contact		       = models.BigIntegerField()
	qualification      = models.CharField(max_length=20)
	experience	       = models.IntegerField()
	registration_date  = models.DateField()
	address			   = models.CharField(max_length=255)
	photo			   = models.CharField(max_length=255)
	city 			   = models.ForeignKey(City,on_delete=models.DO_NOTHING)
	state 			   = models.ForeignKey(State,on_delete=models.DO_NOTHING)
	zipcode 		   = zipcode=models.IntegerField()
	user    = models.OneToOneField(User,on_delete=models.CASCADE)

	class Meta:
		db_table='lawyer'

	def __str__(self):
		return self.lawyer_name



# Client Table
class Client(models.Model):
	client_name 	   = models.CharField(max_length=50)
	username           = models.CharField(max_length=20)
	email		       = models.CharField(max_length=50)
	password           = models.CharField(max_length=20)
	dob			       = models.DateField()
	age			       = models.IntegerField()
	gender			   = models.CharField(max_length=10)
	contact		       = models.BigIntegerField()
	address			   = models.CharField(max_length=255)
	photo			   = models.CharField(max_length=255)
	city 			   = models.ForeignKey(City,on_delete=models.DO_NOTHING)
	state 			   = models.ForeignKey(State,on_delete=models.DO_NOTHING)
	zipcode 		   = zipcode=models.IntegerField()
	user    = models.OneToOneField(User,on_delete=models.CASCADE,default="")

	class Meta:
		db_table='client'

	def __str__(self):
		return self.client_name


# Cases Table
class Cases(models.Model):
	title          = models.CharField(max_length=30)
	description    = models.TextField()
	fir_copy       = models.CharField(max_length=255)
	police_station = models.CharField(max_length=255)
	case_type      = models.CharField(max_length=50)
	case_reg_date  = models.DateField()
	court          = models.CharField(max_length=50)
	judge          = models.CharField(max_length=50)
	status         = models.CharField(max_length=10)
	client         = models.ForeignKey(Client,on_delete=models.DO_NOTHING)
	lawyer         = models.ForeignKey(Lawyer,on_delete=models.DO_NOTHING)
	city 		   = models.ForeignKey(City,on_delete=models.DO_NOTHING)
	state 		   = models.ForeignKey(State,on_delete=models.DO_NOTHING)
	result		   = models.CharField(max_length=5, default="")
	remarks		   = models.TextField(default="")

	class Meta:
		db_table='cases'

	def __str__(self):
		return self.title



# Case Schedule Table
class Schedule(models.Model):
	next_hearing_date = models.DateField()
	remarks           = models.TextField()
	cases             = models.ForeignKey(Cases,on_delete=models.DO_NOTHING)
	status			  = models.TextField(default="")
	description       = models.TextField(default="")
	
	class Meta:
		db_table='schedule'

	def __str__(self):
		return self.next_hearing_date



# Case Document Table
class Documents(models.Model):
	title          = models.CharField(max_length=30)
	document       = models.CharField(max_length=255)
	description    = models.TextField()
	client         = models.ForeignKey(Client,on_delete=models.DO_NOTHING)
	cases          = models.ForeignKey(Cases,on_delete=models.DO_NOTHING)

	class Meta:
		db_table='documents'

	def __str__(self):
		return self.title



# Appointment Table
class Appointment(models.Model):
	date    = models.DateField()
	time    = models.TimeField()
	status  = models.CharField(max_length=10)
	subject = models.CharField(max_length=50)
	message = models.TextField()
	client  = models.ForeignKey(Client,on_delete=models.DO_NOTHING)
	cases   = models.ForeignKey(Cases,on_delete=models.DO_NOTHING)
	
	class Meta:
		db_table='appointment'

	def __str__(self):
		return self.date



# Feedback Table
class Feedback(models.Model):
	date    = models.DateField()
	time    = models.TimeField()
	message = models.TextField()
	rating  = models.IntegerField()
	cases   = models.ForeignKey(Cases,on_delete=models.DO_NOTHING)
	client  = models.ForeignKey(Client,on_delete=models.DO_NOTHING)

	class Meta:
		db_table='feedback'

	def __str__(self):
		return self.message


class Contact_Client(models.Model):
	name    = models.CharField(max_length=30)
	email   = models.CharField(max_length=50)
	phone   = models.BigIntegerField()
	message = models.TextField()
	# cases   = models.ForeignKey(Cases,on_delete=models.DO_NOTHING)

	class Meta:
		db_table='contact_client'

	def _str_(self):
		return self.message