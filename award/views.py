from django.shortcuts import render
from django.http  import HttpResponse, Http404,HttpResponseRedirect
from .forms import NewProfileForm,NewProjectForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def welcome(request):
  return render(request, 'index.html')


def search(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-awards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-awards/search.html',{"message":message})

def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-awards/project.html", {"project":project}) 


def profile(request):
  current_user = request.user
  profile=Profile.objects.filter(user_id=current_user.id)
  projects = Project.objects.filter(user_id=current_user.id)

  return render(request,'profile.html',{"profile":profile,"projects":projects})

@login_required(login_url='/accounts/login')
def new_profile(request):
  current_user=request.user
  if request.method == 'POST':
    form=NewProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      prof_pic=form.cleaned_data['prof_pic']
      bio=form.cleaned_data['bio']
      contact = form.cleaned_data['contact']
      Profile.objects.filter(user=current_user).update(bio=bio,prof_pic=prof_pic,contact=contact)
      profile.save()

    return redirect('profile') 
  else:
    form = NewProfileForm()
    return render(request,'new-profile.html',{"form":form})

@login_required(login_url='/accounts/login')
def project_add(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewProjectForm(request.POST,request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.user = current_user
      project.save()
    return redirect('home')

  else:
    form=NewProjectForm()
    return render(request,'project.html',{'form':form})



