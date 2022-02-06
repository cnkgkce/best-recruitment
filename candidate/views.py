import profile
from django.shortcuts import redirect, render
import requests
from .models import Candidate
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='account/login')
def index(request):
    return render(request,"candidate/index.html")

@login_required(redirect_field_name="login")
def about(request):
    return render(request,"candidate/about.html")


@login_required(login_url='account/login')
def search_for_candidate(request):
    if request.method == "POST":
        username = request.POST['username']
        BASE_URL = "https://api.github.com/users/"
        avatar_url = ''
        profile_url = ''
        email =''
        followers = 0
        following = 0
        repos =''
        
    
        response = requests.get(BASE_URL+str(username))
       

        if response.status_code == 200:
            json_data = response.json()  #json_data is a dictionary
        
            avatar_url = json_data['avatar_url']
            profile_url = json_data['html_url']
            email = json_data['email']
            followers = json_data['followers']
            following = json_data['following']
            
            req = requests.get(profile_url)
            soup = BeautifulSoup(req.text,'html.parser')
            
            repos = soup.find("span",{"class" : "Counter"}).text
            candidate = Candidate(username = username, avatar_url = avatar_url, profile_url = profile_url, email = email , followers = followers , following = following,repos = repos)
            return render(request,"candidate/details.html",{"candidate" : candidate})

        #Buradan devam.. Elimdeki url'lere tekrardan bir request atıp ilgili yerleri html sayfasına gönderebiliriz. Candidate objesi oluşturmaya gerek olmayabilir

        else:
            return render(request,"candidate/index.html",{
                "error_for_status" : "Arattığınız kullanıcı bulunamamıştır :("
            })

    elif request.method == "GET":
        return redirect("index")

    else:
        return render(request,"candidate/index.html",{
            "error_for_method" : "Bu metodun kullanılmasına izin verilmez!"
        })
 



@login_required(login_url='account/login')
def favorites(request):

    candidates = Candidate.objects.all()

    return render(request,"candidate/favorites.html",{"candidates" : candidates})


@login_required(login_url='account/login')
def add_favorite(request,username):
    BASE_URL = "https://api.github.com/users/"
    avatar_url = ''
    profile_url = ''
    email =''
    followers = 0
    following = 0
    repos =''


    response = requests.get(BASE_URL+username)

    if response.status_code == 200:
        json_data = response.json()  #json_data is a dictionary
        
        avatar_url = json_data['avatar_url']
        profile_url = json_data['html_url']
        email = json_data['email']
        followers = json_data['followers']
        following = json_data['following']
            
        req = requests.get(profile_url)
        soup = BeautifulSoup(req.text,'html.parser')
            
        repos = soup.find("span",{"class" : "Counter"}).text
        candidate = Candidate(username = username, avatar_url = avatar_url, profile_url = profile_url, email = email , followers = followers , following = following,repos = repos)
        
        candidate.save()

        return redirect("favorites")