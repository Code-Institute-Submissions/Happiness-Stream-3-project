from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Buy, BuyImage
from sell.models import Sell    


# Create your views here.
def buy_all(request):
    ads = Sell.objects.all()
    return render(request, "buy.html", {"ads": ads})

def buy_details(request, id):
    this_ad = get_object_or_404(Sell, pk=id)
    return render(request, "ad_details.html", {"ad" : this_ad})
    
def do_search(request):
    buy = Buy.objects.filter(name__icontains=request.GET['q'])
    return render(request,"buy.html",{"buys": buy})
    
