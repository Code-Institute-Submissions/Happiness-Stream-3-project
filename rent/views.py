from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Rent

# Create your views here.
def rent_all(request):
    rent = Rent.objects.all()
    return render(request, "rent.html", {"Rent": rent})
    
def do_search(request):
    rent = Rent.objects.filter(name__icontains=request.GET['q'])
    return render(request,"rent.html",{"Rent": rent})
    
def rent_details(request, id):
    this_buy = get_object_or_404(Rent, pk=id)
    return render(request, "rent_detail.html", {"Rent" : this_buy})
