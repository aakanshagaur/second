from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256 as sha
from .models import AddUser
from random import randint
from django.core.mail import send_mail
from .form import Blog


# Create your views here.
def validate_password(password:str):
    if len(password)>=8:
        lower = 0 
        upper = 0 
        special = 0 
        number = 0 
        for i in password:
            if i.islower():
                lower +=1

            elif i.isupper():
                upper += 1

            elif i.isnumeric():
                number += 1 
            
            elif i in "~!@#$%^&*()[]()":
                special += 1

        if lower>=1 and upper>=1 and number>=1 and special>=1 :
            return True
    return False







def index(request):
    # if request.session.get("islogin"):
        # return render(request, "afterlogin.html")
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def login(request):
    # if request.session.get("islogin"):
        # return render(request, 'afterlogin.html')
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')





class Afterlogin(View):

    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            obj = AddUser.objects.get(email=email)
        
        except:
            msg = "User not found"
            return render(request, "login.html", {'msg':msg})
        
        else:
            if sha.verify(password, obj.password):
                request.session['email'] = email
                request.session['islogin'] = "true"
                return render(request, "afterlogin.html")
            else:
                msg = "Incorrect Password"
                return render(request,"login.html", {'msg':msg})
            







class AfterSignup(View):

    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        enc_password = sha.hash(password)
        try:
            AddUser.objects.get(email=email)

        except:
            if validate_password(password):
                # global otp

                otp = randint(1000, 9999)
                request.session['otp']= str(otp)
                request.session['name'] = name
                request.session['email'] = email
                request.session['phone'] = phone
                request.session['password'] = enc_password
                send_mail(
                    "Email Verification for bloscot",
                    f"OTP for Verification is {otp}",
                    "aakanshagaur0143@gmail.com",
                    [email],
                    fail_silently=False,
                )
                # Uncomment the following line to create the user
                # AddUser.objects.create(name=name, email=email, phone=phone, password=enc_password)
                msg = "Please check your mail for OTP"
                return render(request, 'otp.html', {'msg': msg})
            else:
                # User already exists
                msg = "Invalid password please follow password conditions"
                return render(request, 'signup.html', {'msg': msg})
        
        else:
            msg = "User already registered"
            return render(request, "login.html", {'msg':msg})




        #         otp = randint(1000,9999)
        #         send_mail(
        #             "Email verification for bloscot", 
        #             f"OTP for verification is {otp}",
        #             "aakanshagaur0143@gmail.com",
        #             [email],
        #             fail_silently= False,
        #         )

        #     # AddUser.objects.create(name = name,  email = email,phone = phone, password = enc_password)
        #     # msg = "Successfully Registered"
        #         msg = "please check your mail for OTP"
        #         return render(request, 'otp.html',{'msg':msg})
        
        # else:
        #     msg = "Invalid password"
        #     return render(request, 'signup.html',{'msg':msg})



        # except:
        #     if validate_password(password):
        #         otp = randint(1000, 9999)
        #         send_mail(
        #                 "Email Verfication for bloscot", 
        #                 f"OTP for Verification is {otp}",
        #                 "aakanshagaur0143@gmail.com", 
        #                 [email],
        #                 fail_silently = False,
        #                 )
        #     # AddUser.objects.create(name = name,  email = email,phone = phone, password = enc_password)
        #    # msg = "Successfully Registered"
        #         msg = "Please check you mail for OTP"
        #         return render(request, 'otp.html', {'msg':msg})

        #     else:
        #     #msg= "User already Registered"
        #         # msg = "invalid password please follow password conditions"
        #         return render(request, 'signup.html', {'msg':msg})


       # return HttpResponse(f"{name} {email} {phone} {password}")


class checkotp(View):
    def get(self, request):
        return render(request, "signup.html")
    
    def post(self, request):
        otp1  = request.POST.get("otp")
        otp2  = request.session['otp']
        if otp1==otp2:
            name = request.session['name']          
            email = request.session['email']           
            phone = request.session['phone']           
            enc_password = request.session['password']  
        
            AddUser.objects.create(name = name,  email = email,phone = phone, password = enc_password)

            del request.session['otp']
            del request.session['name']
            del request.session['email']
            del request.session['phone']
            del request.session['password']
        
            msg = "User Registered Successfully"
            return render(request, "login.html", {'msg':msg})
        else:
            msg = "Invalid OTP"
            return render(request, "signup.html", {'msg':msg})
        

# def logout(request):
#     del request.session['email']
#     del request.session['islogin']
#     return render(request, "index.html")


def addblog(request):
    form = Blog()
    return render(request, "blogform.html", {'form':form})
    



            

        
  



