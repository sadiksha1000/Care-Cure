from django.urls import path
from  django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index),
    path('home/',views.home),
    path('about/',views.about),
    path('postServiceMF/',views.post_service_mf),
    path('getServiceMF/',views.get_service_mf),
    path('updateServiceMF/<int:service_id>',views.update_service_mf),
    path('deleteServiceMF/<int:service_id>',views.delete_service_mf),
    path('postDoctorMF/',views.post_doctor_mf),
    path('getDoctorMF/',views.get_doctor_mf),
    path('viewDoctorMF/<str:doctor_id>',views.view_doctor_mf, name="view_doctor"),
    path('editDoctorMF/',views.edit_doctor_mf),
    path('updateDoctorMF/<int:doctor_id>',views.update_doctor_mf),
    path('deleteDoctorMF/<int:doctor_id>',views.delete_doctor_mf),


]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_URL)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
