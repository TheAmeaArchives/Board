from django.shortcuts import render, redirect
from .models import Curation, Post
from .forms import CurationForm, PostForm
from django.contrib import messages
# Create your views here.

def detail(request, pk):
    curation = Curation.objects.get(pk = pk)
    return render(request, 'leader/detail.html', {'curation': curation})

def curation(request):
    try:
        user = request.user
        post = Post.objects.get(user=user)
    except:
        user = request.user
        Post.objects.create(user = user)
        post = Post.objects.get(user=user)
    if  post.title == "member":
        if request.method == "POST":
            form = CurationForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = user
                obj.save()
                messages.success(request, "Congratulation You have submitted a curation")
                return redirect("curation")
            else:
                return render(request, 'leader/curation.html', {'form': form})
        else:
            form = CurationForm()
        return render(request, 'leader/curation.html', {'form': form})
    else:
        curations = Curation.objects.filter(accepted = False).order_by("-created_at")
        return render(request, "leader/dashboard.html", {"curations":curations})
    
def remove_curation(request, pk):
    curated = Curation.objects.get(pk = pk)
    if request.method == 'POST':
        curated.delete()
    return redirect("curation")

def edit_curation(request, pk):
    curated = Curation.objects.get(pk=pk)
    curations = Curation.objects.all()
    if request.method == "POST":
        form = CurationForm(request.POST, instance = curated)
        if form.is_valid():
            obj= form.save(commit=False)
            obj.user = curated.user
            obj.save()
            return redirect("curation")
    else:
        form = CurationForm(instance = curated)
    return render(request, "leader/edit.html",{'curated':curated ,'form': form})

def accept(request, pk):
    curation = Curation.objects.get(pk = pk)
    curated = Post.objects.get(user = curation.user)
    print("not post")
    if request.method == 'POST':
        print("here")
        curated.points+=1
        curation.accepted = True
        curation.save()
        curated.save()
    return redirect('curation')

def leader_board(request):
    users = Post.objects.all().order_by('-points')
    return render(request, "leader/leader.html", {"users":users})

def accepted(request):
    curations = Curation.objects.filter(accepted = True)
    return render(request, "leader/accepted.html", {"curations":curations})

