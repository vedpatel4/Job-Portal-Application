from django.shortcuts import render,redirect
from .models import Job
from .forms import Create_JobForm
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    form = Create_JobForm()

    if request.method == 'POST':
        form = Create_JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('/')

    context = {'createjobform': form}
    return render(request, 'job/create.html', context=context)

def show(request):
    jobs = Job.objects.all()
    return render(request, "job/show.html", {'jobs': jobs})



