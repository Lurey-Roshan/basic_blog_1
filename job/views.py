from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from job.models import Job

def index(request):
	jobs=Job.objects.order_by('summary')
	return render(request, 'job/index.html', {'jobs':jobs})

def d_job(request, job_id):
	detailjob=get_object_or_404(Blog, pk=job_id)
	return render(request, 'job/job.html', {'jobs': detailjob})