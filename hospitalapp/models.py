from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,PermissionsMixin,BaseUserManager 

# Create your models here.
class Category(models.Model):
    department_name = models.CharField(max_length=100)




class Patient_model(models.Model):
    patient = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pt_age = models.IntegerField()
    pt_gender = models.CharField(max_length=70)
    pt_phone = models.IntegerField()
    pt_addres = models.CharField(max_length=200)
    image = models.ImageField(upload_to="image/", null=True)


class Xray_category(models.Model):
    X_ray_types = models.CharField(max_length=100)


class Lab_category(models.Model):
    Lab_type = models.CharField(max_length=100)


class Blood_category(models.Model):
    blood_type = models.CharField(max_length=100)


#class add_doctor(models.Model):
 #     dept = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
  #    name = models.CharField(max_length=100)
   #   adres = models.CharField(max_length=100)
    #  age = models.IntegerField()
    #  gender = models.CharField(max_length=70)
    #  phoneno = models.IntegerField()
     # image = models.ImageField(upload_to="image/", null=True)

class add_doctor_details(models.Model):
      dept = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
      name = models.CharField(max_length=100)
      adres = models.CharField(max_length=100)
      age = models.IntegerField()
      gender = models.CharField(max_length=70)
      phoneno = models.IntegerField()
      image = models.ImageField(upload_to="image/", null=True)


class nurse_model(models.Model):
      name = models.CharField(max_length=100)
      adres = models.CharField(max_length=100)
      age = models.IntegerField()
      gender = models.CharField(max_length=70)
      phoneno = models.IntegerField()


class Bookings_model(models.Model):
      dept = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
      name = models.CharField(max_length=100)
      adres = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      age = models.IntegerField()
      phoneno = models.IntegerField()
      status = models.CharField(max_length=20, default='No Booking')  # Default status is 'pending'



class Booking_labs(models.Model):
      lab = models.ForeignKey(Lab_category,on_delete=models.CASCADE,null=True)
      name = models.CharField(max_length=100)
      adres = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      age = models.IntegerField()
      phoneno = models.IntegerField()

class Booking_xray(models.Model):
      xray = models.ForeignKey(Xray_category,on_delete=models.CASCADE,null=True)
      name = models.CharField(max_length=100)
      adres = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      age = models.IntegerField()
      phoneno = models.IntegerField()


class Book_blood(models.Model):
      bld = models.ForeignKey(Blood_category,on_delete=models.CASCADE,null=True)
      name = models.CharField(max_length=100)
      adres = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      age = models.IntegerField()
      phoneno = models.IntegerField()


class Contact_details(models.Model):
    name = models.CharField(max_length=100)
    phoneno = models.IntegerField()
    addres = models.CharField(max_length=600)
    email = models.EmailField()
    remarks = models.CharField(max_length=600)


class UserProfile(models.Model):
    # Other fields in the profile model
    status = models.CharField(max_length=20,default='No Bookings')