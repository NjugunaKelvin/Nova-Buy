from django.shortcuts import render

# Create your views here.
def summary(request):
    return render(request, 'cart_summary.html', {})
    pass

def add(request):
    pass

def delete(request):
    pass

def update(request):
    pass