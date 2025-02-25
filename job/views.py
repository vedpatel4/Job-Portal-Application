from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import Create_JobForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required  # Only logged-in users can access this view
def create(request):
    form = Create_JobForm()

    if request.method == 'POST':
        form = Create_JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user  # Associate the job with the logged-in user
            job.save()
            return redirect('show')

    context = {'createjobform': form}
    return render(request, 'job/create.html', context=context)

def show(request):
    jobs = Job.objects.all()
    return render(request, "job/show.html", {'jobs': jobs})

@login_required  # Only logged-in users can access this view
def update(request, id):
    job = get_object_or_404(Job, id=id)
    if job.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this job.")
    
    form = Create_JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect("show")
    
    context = {'updatejobform': form}
    return render(request, 'job/update.html', context=context)

@login_required  # Only logged-in users can access this view
def delete(request, id):
    job = get_object_or_404(Job, id=id)
    if job.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this job.")
    
    job.delete()
    return redirect("show")