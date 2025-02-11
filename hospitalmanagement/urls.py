"""
Developed By : KENNEDY MAINIMO TATAH

"""




from django.contrib import admin
from django.urls import path
from hospital import views
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),



    path('adminclick', views.adminclick_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),

    path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),
    
    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='hospital/patientlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),


    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'),
    
    path('admin-discharge-doctor', views.admin_discharge_doctor_view,name='admin-discharge-doctor'),
    
    path('discharge-doctor/<int:pk>', views.discharge_doctor_view,name='discharge-doctor'),
    
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    
    path('download-doctor-pdf/<int:pk>', views.download_doctor_pdf_view,name='download-doctor-pdf'),
    
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),


    path('admin-revenue-view', views.admin_revenu,name='admin-revenue-view'),   
    path('admin-view-revenu-view', views.admin_view_revenu_view,name='admin-view-revenu-view'),   
    
    
    path('admin-expense',views.admin_expense,name='admin-expense'),
    path('admin-expense-view',views.admin_expense12,name='admin-expense-view'),
    
    #path('admin_view_expense',views.admin_view_expense,name='admin-view-expense'),
    
    path('search-doctor',views.search_doctor,name='search-doctor'),
    
    
    path('admin-add-expense',views.admin_add_expense,name='admin-add-expense'),
    path('admin-expense-generate-report',views.admin_expense_generate_report,name='admin-expense-generate-report'),
    path('admin-revenu-generate-report',views.admin_revenu_generate_report,name='admin-revenu-generate-report'),
    path('download-expense-pdf', views.download_pdf_expense_report,name='download-expense-pdf'),
    path('download-revenu-pdf', views.download_pdf_revenu_report,name='download-revenu-pdf'),
    path('admin-approve-expense', views.admin_approve_expense_view,name='admin-approve-expense'),
    path('approve-expense/<int:pk>', views.approve_expense_view,name='approve-expense'),
    path('reject-expense/<int:pk>', views.reject_expense_view,name='reject-expense'),
    path('delete-expense/<int:pk>', views.delete_expense_view,name='delete-expense'),
    path('update-expense/<int:pk>', views.update_expense_view,name='update-expense'),
    
    
    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
]


#---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('search', views.search_view,name='search'),
    path('search-patient', views.search_view1,name='search-patient'),
    #path('search-doctor', views.search_view2,name='search-doctor'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-add-patient', views.doctor_add_add_patient,name='doctor-add-patient'),
    
    path('doctor-expense',views.doctor_expense,name='doctor-expense'),
    path('doctor-view-expense',views.doctor_view_expense,name='doctor-view-expense'),
    path('doctor-add-expense',views.doctor_add_expense,name='doctor-add-expense'),
    
    
    path('doctor-view-patient', views.doctoginr_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),
    path('doctor-update-patient/<int:pk>', views.doctor_update_patient_view,name='doctor-update-patient'),
    
    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
]




#---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns +=[

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-view-doctor', views.patient_view_doctor_view,name='patient-view-doctor'),
    path('searchdoctor', views.search_doctor_view,name='searchdoctor'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),

]

#Developed By : KENNEDY MAINIMO TATAH
