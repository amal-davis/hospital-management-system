import select
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from .models import *
import random
import string




# Create your views here.

def index(request):
    return render(request, 'index.html')


def signuppage(request):
    return render(request,'signup.html')


def loginpage(request):
    return render (request,'login.html')


def user_create(request):
    if request.method == "POST":
        first_name =  request.POST['fname']
        last_name = request.POST['lname']

        email = request.POST['email']
        phonenumber = request.POST['phnum']
        G_endr = request.POST['gender']
        age = request.POST['A_ge']
        address = request.POST['adres']
        photo = request.FILES.get('files')
        username = request.POST['uname']
        password = request.POST['password']
        if len (password) < 8:
            messages.error(request, 'Password must be alt least 8 characters long.')
            return redirect('signuppage')
        if not any(char.isupper() for char in password):
            messages.error(request, 'Password must contain atleast one Uppercase letter')
            return redirect('signuppage')
        if not any(char.isdigit() for char in password):
            messages.error(request,'Password must contain at least one numeric digit.')
            return redirect('signuppage')
        if not any(char in string.punctuation for char in password):
            messages.error(request,'Password must contain atleast one special character.')
            return redirect('signuppage')
        if User.objects.filter(username=username).exists():
            messages.info(request,'This username already exisists!!')
            return redirect('signuppage')
        elif User.objects.filter(email=email).exists():
             messages.info(request,'This email is already exisists!!')
             return redirect('signuppage')
        else:
            user =  User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.save()
            data = User.objects.get(id=user.id)
            patient_data = Patient_model.objects.create(pt_age=age,pt_gender=G_endr,pt_phone=phonenumber,pt_addres=address,image=photo,patient=data)
            patient_data.save()
            send_mail('Your Account Details',f'Username: {username}\nPassword: {password}', 'amald416@gmail.com', recipient_list=[email],fail_silently=False)
            messages.success(request,'Your Account Has Been Created Sucessfully')
            return redirect('loginpage')
    else:
      return redirect('loginpage')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('adminpage')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('show_profile')
        else:
            return redirect('loginpage')
    return redirect('loginpage')


@login_required(login_url='loginpage')
def show_profile(request):
    puser = request.user
    user_id = puser.id
    user = User.objects.get(id=user_id)
    patient = Patient_model.objects.get(patient=user_id)
    appointments = Bookings_model.objects.all()
    return render(request, 'profile.html', {'patient': patient, 'user': user, 'appointments': appointments})


def logout(request):
	auth.logout(request)
	return redirect('index')


def adminpage(request):
    return render(request,'admin.html')


def pa_edit(request,pk):
    patient = Patient_model.objects.get(id=pk)
    return render(request,'edit.html',{'patient':patient})


def pa_edit_details(request,pk):
    if request.method == 'POST':
        patient = Patient_model.objects.get(id=pk)
        user_id = patient.patient.id
        print(user_id)
        user = User.objects.get(id=user_id)
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.username = request.POST.get('uname')
        user.email = request.POST.get('email')
        patient.pt_phone = request.POST.get('phnum')
        patient.pt_gender = request.POST.get('gender')
        patient.pt_age = request.POST.get('A_ge')
        patient.pt_addres = request.POST.get('adres')
        old = patient.image
        new = request.FILES.get('files')
        if old != None and new == None:
            patient.image=old
        else:
            patient.image=new
        user.save()
        patient.save()
        patient = Patient_model.objects.get(id=pk)
        return redirect('show_profile')
    return render(request,'edit.html',{'patient':patient})


def adddep(request):
    return render(request,'adddepart.html')


def dep_details(request):
    if request.method == 'POST':
        depname = request.POST['dname']
        data = Category(department_name=depname)
        data.save()
        return redirect('adminpage')


def addxray(request):
    return render(request,'addxray.html')


def add_xray_detais(request):
    if request.method == 'POST':
        x_name = request.POST['xname']
        data = Xray_category(X_ray_types=x_name)
        data.save()
        return redirect('adminpage')


def add_lab(request):
    return render(request,'addlab.html')


def add_lab_details(request):
    if request.method == 'POST':
        lab_name = request.POST['lname']
        data = Lab_category(Lab_type=lab_name)
        data.save()
        return redirect('adminpage')


def add_blood(request):
    return render(request,'addblood.html')


def add_blood_details(request):
    if request.method == 'POST':
        b_name = request.POST['bgroup']
        data = Blood_category(blood_type=b_name)
        data.save()
        return redirect('adminpage')


def add_docto(request):
    dept = Category.objects.all()
    context = {'dept':dept}
    return render(request,'adddoctor.html',context)


def add_doctor(request):
    if request.method == 'POST':
        docname = request.POST['name']
        docadres = request.POST['adres']
        docage = request.POST['age']
        docgender = request.POST['gender']
        docphn = request.POST['phnum']
        select = request.POST['select']
        photo = request.FILES.get('files')
        dept = Category.objects.get(id=select)
        data = add_doctor_details(name=docname,adres=docadres,age=docage,gender=docgender,phoneno=docphn,dept=dept,image=photo)
        data.save()
        return redirect('adminpage')


def search(request):
    return render(request,'searched.html')


def searched_detail(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        doctors = add_doctor_details.objects.filter(name=searched)
        context = {'searched':searched,'doctors':doctors,}

        return render(request,'searched.html',context)
    else:
        return redirect('search')
            


def add_nurse(request):
    return render(request,'addnurse.html')


def add_nurse_details(request):
    if request.method == 'POST':
        nursname = request.POST['name']
        nursadres = request.POST['adres']
        nursgender = request.POST['gender']
        nursage = request.POST['age']
        nursphn = request.POST['phnum']
        data = nurse_model(name=nursname,adres=nursadres,gender=nursgender,age=nursage,phoneno=nursphn)
        data.save()
        return redirect('adminpage')

def book_dep(request):
    dept = Category.objects.all()
    context = {'dept':dept}
    return render(request,'bookapoint.html',context)


def book_form(request):
    if request.method == 'POST':
       pt_name = request.POST['name']
       pt_adres = request.POST['adres']
       pt_email = request.POST['email']
       pt_age = request.POST['age']
       pt_phnnum = request.POST['phnnum']
       select = request.POST['select']
       cat = Category.objects.get(id=select)
       data = Bookings_model(name=pt_name,adres=pt_adres,email=pt_email,age=pt_age,phoneno=pt_phnnum,dept=cat)
       messages.success(request,'Your Registeration has completed .Please wait for the confirmation email for more details')
       data.save()
       
       return redirect('show_profile')
    else:
        return render(request,'bookapoint.html')
    





def book_lab(request):
    lab = Lab_category.objects.all()
    context = {'lab':lab}
    return render(request,'booklab.html',context)


def book_lab_details(request):
    if request.method == 'POST':
       pt_name = request.POST['name']
       pt_adres = request.POST['adres']
       pt_email = request.POST['email']
       pt_age = request.POST['age']
       pt_phnnum = request.POST['phnnum']
       select = request.POST['select']
       cat = Lab_category.objects.get(id=select)
       data = Booking_labs(name=pt_name,adres=pt_adres,email=pt_email,age=pt_age,phoneno=pt_phnnum,lab=cat)
       data.save()
       subject = 'Booking Confirmation'
    message = 'Dear Consultant,\nWe are pleased to inform that your booking for Lab check is schedulsd for tommorow morning 9.00am'
    recipient =request.POST["email"]
    send_mail(subject, 
        message, settings.EMAIL_HOST_USER, [recipient])
    return redirect('show_profile')


def book_xray(request):
    xray = Xray_category.objects.all()
    context = {'xray':xray}
    return render(request,'bookxray.html',context)

        
def book_xray_details(request):
     if request.method == 'POST':
       pt_name = request.POST['name']
       pt_adres = request.POST['adres']
       pt_email = request.POST['email']
       pt_age = request.POST['age']
       pt_phnnum = request.POST['phnnum']
       select = request.POST['select']
       cat = Xray_category.objects.get(id=select)
       data = Booking_xray(name=pt_name,adres=pt_adres,email=pt_email,age=pt_age,phoneno=pt_phnnum,xray=cat)
       data.save()
       subject = 'Booking Confirmation'
       message = 'Dear Consultant,\nWe are pleased to inform that your booking for xray checkup is schedulsd for tommorow morning 9.00am'
       recipient =request.POST["email"]
       send_mail(subject, 
                 message, settings.EMAIL_HOST_USER, [recipient])
       return redirect('show_profile')


def book_blood(request):
    bld = Blood_category.objects.all()
    context = {'bld':bld}
    return render(request,'bookblood.html',context)


def book_blood_details(request):
     if request.method == 'POST':
       pt_name = request.POST['name']
       pt_adres = request.POST['adres']
       pt_email = request.POST['email']
       pt_age = request.POST['age']
       pt_phnnum = request.POST['phnnum']
       select = request.POST['select']
       cat = Blood_category.objects.get(id=select)
       data = Book_blood(name=pt_name,adres=pt_adres,email=pt_email,age=pt_age,phoneno=pt_phnnum,bld=cat)
       data.save()
       subject = 'Booking Confirmation'
       message = 'Dear Consultant,\nWe are pleased to inform that your booking for blood Donation is schedulsd for tommorow morning 9.00am'
       recipient =request.POST["email"]
       send_mail(subject, 
                 message, settings.EMAIL_HOST_USER, [recipient])
       return redirect('show_profile')
     
       
def patient_view(request):
    patient = Patient_model.objects.all()
    return render(request,'patientview.html',{'patient':patient})
       

def delete_data(request,pk):
    d = Patient_model.objects.filter(id=pk)
    d.delete()
    return redirect('patient_view')


def enroled_data(request):
    return render(request,'enroled.html')


def booked_data(request):
    booked = Bookings_model.objects.all()
    return render (request,'apoviews.html',{'booked':booked})


def booked_lab(request):
    book = Booking_labs.objects.all()
    return render(request,'labviews.html',{'book':book})

def booked_xray(request):
    xbook = Booking_xray.objects.all()
    return render(request,'xrayview.html',{'xbook':xbook})


def booked_blood(request):
    blood = Book_blood.objects.all()
    return render(request,'bloodview.html',{'blood':blood})


def booked_data_edit(request,pk):
    cat = Category.objects.all()
    booked = Bookings_model.get(id=pk)
    return render(request,'datasend.html',{'cat':cat,'booked':booked})


def delete_views(request,pk):
      d = Bookings_model.objects.filter(id=pk)
      d.delete()
      return redirect('booked_data')


'''def dataform(request):
    form = model_form()
    if request.method == 'POST':
        form = model_form(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Booking Confirmation'
            message = 'Dear Candidate,\n We are pleased to inform that your booking has been sechuduled for tomorrow morning 9.00am'
            recipient = form.cleaned_data.get('email')     #  recipient =request.POST["inputTagName"]
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient])
            return redirect('adminpage')
    return render(request, 'datasend.html', {'form': form})'''


def Contact(request):
    return render(request,'contact.html')


def contact_details(request):
    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_adres = request.POST['message_adres']
        messaage_email = request.POST['messaage_email']
        message = request.POST['message']
        message_phnnum = request.POST['message_phnnum']

        send_mail(
         'message from'+ message_name, # Subject
         message, # Message
         messaage_email, # From email
         ['amald416@gmail.com']   # To email
        )
        mail = Contact_details(name=message_name,phoneno=message_phnnum,addres=message_adres,email=messaage_email,remarks=message)
        mail.save()
        return render(request,'contact.html',{'message_name':message_name})
    else:
       return redirect('Contact')


def about(request):
    return render(request,'about.html')


def send_email(request, pk):
    try:
        obj = Bookings_model.objects.get(pk=pk)
        customer_email = obj.email  # Assuming the email field is named 'email' in your CustomModel

        # Send the email
        send_mail(
            'Booking Confirmation',
            'This is to inform you that the booking for your appointment has been scheduled for tommorow morning',
           settings.EMAIL_HOST_USER,  # Sender's email address
            [customer_email],  # List of recipient email addresses
            fail_silently=False,
        )
# Optionally, you can perform other actions or display a success message
        messages.success(request, 'Email sent successfully!')
    except Bookings_model.DoesNotExist:
        messages.error(request, 'Invalid data entry.')

    return redirect('booked_data')  # Redirect back to the change list view


def rejection_mail(request, pk):
    try:
        obj = Bookings_model.objects.get(pk=pk)
        customer_email = obj.email  # Assuming the email field is named 'email' in your CustomModel

        # Send the email
        send_mail(
            'Booking Status',
            'This is to inform you that the booking for your appointment has been cancelled due to unavailable of staff',
           settings.EMAIL_HOST_USER,  # Sender's email address
            [customer_email],  # List of recipient email addresses
            fail_silently=False,
        )
# Optionally, you can perform other actions or display a success message
        messages.success(request, 'Email sent successfully!')
    except Bookings_model.DoesNotExist:
        messages.error(request, 'Invalid data entry.')

    return redirect('booked_data')  # Redirect back to the change list view


def confirm_appointment(request, appointment_id):
    appointments = Bookings_model.objects.get(pk=appointment_id)
    appointments.status = 'Confirmed'
    appointments.save()
    send_email(request,appointment_id)
    return redirect('admin:hospitalapp_bookings_model_changelist')


def reject_appointment(request, appointment_id):
    appointments = Bookings_model.objects.get(pk=appointment_id)
    appointments.status = 'Rejected'
    appointments.save()

    rejection_mail(request,appointment_id)
    return redirect('admin:hospitalapp_bookings_model_changelist')


def status(request):
    return render(request,'status.html')
