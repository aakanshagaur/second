from django.shortcuts import render
from django.views import View
from passlib.hash import pbkdf2_sha256 as sha
from .models import AddUser
from django.http import HttpResponse
from random import randint
from django.core.mail import send_mail


# Create your views here.
def validate_password(password: str):
    if len(password)>=8:
        lower = 0
        upper = 0
        special = 0
        number = 0
        for i in password:
            if i.islower():
                lower += 1
            
            elif i.isupper():
                upper += 1

            elif i.isnumeric():
                number += 1

            elif i in "~!@#$%^&*()_[]()":
                special += 1

        if lower>=1 and upper>=1 and number>=1 and special>=1:
                return True
    return False

def index(request):
    if request.session.get("islogin"):
        return render(request, "afterlogin.html")
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    #if request.session.get("islogin"):
     #   return render(request, "afterlogin.html")
    return render(request, 'login.html')


class Afterlogin(View):
    def get(self, request):
        return render(request, "login.html")
    
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            obj = AddUser.objects.get(email=email)
        except:
            msg = "user not found"
            return render(request, "login.html", {'msg':msg})
        else:
            if sha.verify(password, obj.password):
                request.session['email'] = email
                request.session['islogin'] = "true"
                return render(request, "afterlogin.html")
            else:
                msg = "Incorrect Password"
                return render(request, "login.html", {'msg':msg})


class AfterSignup(View):
    def get(self, request):
        return render(request, "signup.html")   # this method will handle get method request
    
    def post(self, request):          
     # this method will handle post method request   
        name= request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        enc_password = sha.hash(password)
        try:
            AddUser.objects.get(email=email)
        except:
            if validate_password(password):
                # global otp
                otp = randint(1000, 9999)
                request.session['otp'] = str(otp)
                request.session['name'] = name
                request.session['phone'] = phone
                request.session['email'] = email
                request.session['password'] = enc_password
                send_mail(
                    "Email verification for bloscot",
                    f"otp for verification is {otp}",
                    "hiteshkashyap1195@gmail.com",
                    [email],
                    fail_silently=False,
                    )

                #AddUser.objects.create(name=name, phone=phone, email=email, password=enc_password)
                #msg = "Successfully Register"
                msg = "please check your mail for otp"
                return render(request, 'otp.html')

            else:
                #msg = "user already register"
                msg = "invalid password please follow password condition"
                return render(request, "signup.html", {'msg':msg})
            
        else:
            msg = "user alredy registered"
        
        return render(request, "login.html", {'msg': msg})
        

class Checkotp(View):
    def get(self, request):
        return render(request, "signup.html")
    
    def post(self, request):
        otp1 = request.POST.get("otp")
        otp2 = request.session['otp']
        if otp1 == otp2:
            name = request.session['name']
            phone = request.session['phone']
            email = request.session['email']
            enc_password = request.session['password']
            AddUser.objects.create(name=name, phone=phone, email=email, password=enc_password)

            del request.session['otp']
            del request.session['name']
            del request.session['phone']
            del request.session['email']
            del request.session['password']

            msg = "user registered successfully"

            return render(request, "login.html", {'msg':msg})
        
        else:

            msg = "invalid otp"
            return render(request, "signup.html", {'msg':msg})

def logout(request):
    del request.session['email']
    del request.session['islogin']
    return render(request, "login.html")
        




        #return HttpResponse(f"{name} {phone} {email} {password}")
       #return render(request, f"{name} {phone} {email} {password}")
       

