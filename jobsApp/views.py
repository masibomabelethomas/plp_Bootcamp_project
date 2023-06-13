from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Job
from .forms import JobForm, ApplyForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

from django.core.paginator import Paginator #django docs forsetails



# Create your views here.
def joblist(request):
    jobs = Job.objects.all()
   
    # Filters
    myfilter = JobFilter(request.GET, queryset=jobs)
    jobs = myfilter.qs # qs == queryset
   
    # Pagination
    paginator = Paginator(jobs, 5) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    context = {'jobs': page_obj, 
            'myfilter' : myfilter} # templates name
    return render(request, "joblist.html", context) # template not working.

# Job detail + Apply view
def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug) # will retrieve on job
    # job_detail = Job.object.filter() # will retrieve on job from a list according to some filtration


    # Django bootstrap:  https://django-bootstrap4.readthedocs.io/en/latest/quickstart.html
    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
                    myform = form.save(commit=False)
                    myform.job = job_detail
                    myform.save()
                    print('Done')

    else:
        form = ApplyForm()

    context = {'job' : job_detail , 'form' : form}
    return render(request,'jobdetail.html', context)