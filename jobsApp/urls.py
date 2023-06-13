from django.urls import path
from . import views
app_name='jobsApp'
urlpatterns = [
    path('', views.joblist, name ="job-list"),#reverse("jobs:job_list")
    path('job-detail/<str:slug>', views.job_detail, name ="job-detail"),
    path('add-job', views.add_job, name ="add-job"),
]