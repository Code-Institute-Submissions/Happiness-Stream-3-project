from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Buy

# Create your views here.
def buy_all(request):
    buy = Buy.objects.all()
    return render(request, "buy.html", {"Buy": buy})
    
def do_search(request):
    buy = Buy.objects.filter(name__icontains=request.GET['q'])
    return render(request,"buy.html",{"Buy": buy})
    
def buy_details(request, id):
    this_buy = get_object_or_404(Buy, pk=id)
    return render(request, "product_detail.html", {"buy" : this_buy})
