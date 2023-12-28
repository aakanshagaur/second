from django.shortcuts import render
from .models import AddUser
from django.views import View
# Create your views here.



def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def gallery(request):
    return render(request, 'gallery.html')
def service(request):
    return render(request, 'service.html')
def contact(request):
    return render(request, 'contact.html')


class AfterContact(View):

    def get(self, request):
        return render(request, 'contact.html')
    
    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            AddUser.objects.get(email=email)
        except:
            AddUser.objects.create(name=name, phone=phone, email=email, message=message)
            msg="Successfull, you'll get call or mail soon.. Thanks for Contact Us"
            return render(request, 'contact.html', {'msg':msg})
        else:
            pass