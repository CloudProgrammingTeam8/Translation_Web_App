from django.shortcuts import render
# from .models import Post

# Create your views here.
def translate(request):
    return render(request, 'trans/index.html')