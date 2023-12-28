from django.shortcuts import render

def index(request):
   return render(request, 'index.html')
def about(request):
   return render(request, 'about.html')
def blog(request):
   return render(request, 'blog.html')
def contact(request):
   return render(request, 'contact.html')
def project(request):
   return render(request, 'project.html')
def service(request):
   return render(request, 'service.html')
def single(request):
   return render(request, 'single.html')
