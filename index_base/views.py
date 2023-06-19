from django.shortcuts import render

# Create your views here.
def index_base_def(request):
    return render(request, 'index_base.html')