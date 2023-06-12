from django.urls import path
from . import views

urlpatterns = [
    path('', views.joblist, name ="joblist"),
    path('job-detail/<str:slug>', views.job_detail, name ="job-detail"),
]