from django.shortcuts import render, redirect
from .models import Curation, Post
from .forms import CurationForm, PostForm
from django.contrib import messages
# Create your views here.

def detail(request, pk):
    #This part direct the users into the detail page of the post
    curation = Curation.objects.get(pk = pk)
    return render(request, 'leader/detail.html', {'curation': curation})

def curation(request):
    #This try statement assigns the current currator to its post
    try:
        user = request.user
        post = Post.objects.get(user=user)
    except:
    #The excapt code is to create a new post for the User if it he doesn't have an instance yet
    #Then, in his dashboard, if the user did a POST request, the logic to validate the code goes on
        user = request.user
        Post.objects.create(user = user)
        post = Post.objects.get(user=user)
    # Here, we verify if the users status is member
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
    #This else statement is for chief curators, since if they aren't member, they must be chief curators, and the only thing they will need is the list of curations 
    else:
        curations = Curation.objects.filter(accepted = False).order_by("-created_at")
        return render(request, "leader/dashboard.html", {"curations":curations})
    
def remove_curation(request, pk):
    #This function removes a curation from the database and redirect the user to his dashboard
    curated = Curation.objects.get(pk = pk)
    if request.method == 'POST':
        curated.delete()
    return redirect("curation")

def edit_curation(request, pk):
    #This is the logic for the chief of curations to be able to edit the curations they need.
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
#This function is to accept a curation, it will change the status of the curation to true for us to be able to add it in the accpet page of curations
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
    #This is the section of the leader board, where every users would ber able to see the different ranks of each users
    users = Post.objects.all().order_by('-points')
    return render(request, "leader/leader.html", {"users":users})

def accepted(request):
    #This section is for every users to be able to view the accepted post whose accepted status is set to true(remember to accept view logic)
    curations = Curation.objects.filter(accepted = True)
    return render(request, "leader/accepted.html", {"curations":curations})

