from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from newapp.models import Employee

def Signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        if pass1 != pass2:
            return HttpResponse("<h1>Password doesn't match</h1>")
        else:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.save()
            return redirect('login')
    return render(request,"SignUp.html")

def Login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass")
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("<h1>UserID and Pass Not Valid</h1>")
    return render(request,"Login.html")

# def Welcome(request):
#     return render(request,"Welcome.html")

def LogoutPage(request):
    logout(request)
    return redirect('login')


def Index(request):
    emp = Employee.objects.all()
    context = {
        "Emp": emp
    }
    return render(request, "index.html", context)



def Add(request):
    n = ''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            Name=name,
            Email=email,
            Address=address,
            Phone=phone
        )
        emp.save()
        n = 'Data Inserted'
        return redirect('home')

    return render(request, "index.html", {'n': n})


def Edit(request):
    emp = Employee.objects.all()
    context = {
        "Emp": emp
    }
    return render(request, "index.html", context)


def Update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            id=id,
            Name=name,
            Email=email,
            Address=address,
            Phone=phone
        )
        emp.save()
        return redirect('home')

    return render(request, "index.html")


'''
def Delete(request,id):

    if request.method == "POST":
        emp = Employee(
            id=id
        )
        emp.delete()
        # emp.save()
        return redirect('home')
    return render(request,"index.html")
    '''


def Delete(request, id):
    emp = Employee.objects.filter(id=id)
    emp.delete()
    context = {
        'Emp': emp
    }
    return redirect('home')


