from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.




def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        
        return render(request,"account/login.html",{
            "error_for_authentication" : "Kullanıcı adı veya parola hatalı"
        })

    elif request.method == "GET":
        return render(request,"account/login.html")

    else:
        return render(request,"account/login.html",{
            "error" : "Bu metodun kullanımına izin verilmez!"
        })




def register_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():
            return render(request,"acocunt/register.html",{
                "error" : "Bu kullanıcı adına ait başka bir hesap bulunmaktadır !"
            })
        
        user = User.objects.create_user(username = username, password = password)
        user.save()
        return redirect("login")

    elif request.method == "GET":
        return render(request,"account/register.html")

    else:
        return render(request,"account/register.html",{
            "error" : "Bu metodun kullanımına izin verilmez"
        })



@login_required(login_url='account/login')
def logout_request(request):
    logout(request)
    return redirect("login")