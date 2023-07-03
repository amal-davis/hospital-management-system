from django.urls import path
from  hospitalapp import views
from  django.contrib import admin
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.index,name='index'),
    path('signuppage/',views.signuppage,name='signuppage'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('show_profile/',views.show_profile,name='show_profile'),
    path('user_create/',views.user_create,name='user_create'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('pa_edit/<int:pk>',views.pa_edit,name='pa_edit'),
    path('pa_edit_details/<int:pk>',views.pa_edit_details,name='pa_edit_details'),
    path('adddep/',views.adddep,name='adddep'),
    path('dep_details/',views.dep_details,name='dep_details'),
    path('addxray/',views.addxray,name='addxray'),
    path('add_xray_detais/',views.add_xray_detais,name='add_xray_detais'),
    path('add_lab/',views.add_lab,name='add_lab'),
    path('add_lab_details/',views.add_lab_details,name='add_lab_details'),
    path('add_blood/',views.add_blood,name='add_blood'),
    path('add_blood_details/',views.add_blood_details,name='add_blood_details'),
    path('add_docto/',views.add_docto,name='add_docto'),
    path('add_doctor',views.add_doctor,name='add_doctor'),
    path('add_nurse/',views.add_nurse,name='add_nurse'),
    path('add_nurse_details/',views.add_nurse_details,name='add_nurse_details'),
    path('book_dep/',views.book_dep,name='book_dep'),
    path('book_form/',views.book_form,name='book_form'),
    path('book_lab/',views.book_lab,name='book_lab'),
    path('book_lab_details/',views.book_lab_details,name='book_lab_details'),
    path('book_xray/',views.book_xray,name='book_xray'),
    path('book_xray_details/',views.book_xray_details,name='book_xray_details'),
    path('book_blood/',views.book_blood,name='book_blood'),
    path('book_blood_details/',views.book_blood_details,name='book_blood_details'),
    path('patient_view/',views.patient_view,name='patient_view'),
    path('delete_data/<int:pk>',views.delete_data,name='delete_data'),
    path('enroled_data/',views.enroled_data,name='enroled_data'),
    path('booked_data/',views.booked_data,name='booked_data'),
    path('booked_lab/',views.booked_lab,name='booked_lab'),
    path('booked_xray/',views.booked_xray,name='booked_xray'),
    path('booked_blood/',views.booked_blood,name='booked_blood'),
    path('booked_data_edit/<int:pk>',views.booked_data_edit,name='booked_data_edit'),
    path('delete_views/<int:pk>',views.delete_views,name='delete_views'),
    path('search/',views.search,name='search'),
    path('searched_detail/',views.searched_detail,name='searched_detail'),
    path('Contact/',views.Contact,name='Contact'),
    path('contact_details/',views.contact_details,name='contact_details'),
    path('about',views.about,name='about'),
    path('send_email/<int:pk>/', views.send_email, name='send_email'),
    path('rejection_mail/<int:pk>/', views.rejection_mail, name='rejection_mail'),
    path('confirm_appointment/<int:appointment_id>',views.confirm_appointment,name='confirm_appointment'),
    path('reject_appointment/<int:appointment_id>',views.reject_appointment,name='reject_appointment'),
    path('status/',views.status,name='status'),
    


    
   

]