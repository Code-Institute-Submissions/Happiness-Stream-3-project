from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Rent, RentImage

# Create your views here.
def rent_all(request):
    rent = Rent.objects.all()
    return render(request, "rent.html", {"rents": rent})
    
def do_search(request):
    rent = Rent.objects.filter(name__icontains=request.GET['q'])
    return render(request,"rent.html",{"rents": rent})
    
def rent_details(request, id):
    this_rent = get_object_or_404(Rent, pk=id)
    rent_images = RentImage.objects.filter(pk=id)
    return render(request, "rent_detail.html", {"rent" : this_rent, 'rent_images': rent_images})
