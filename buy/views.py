from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Buy, BuyImage

# Create your views here.
def buy_all(request):
    buy = Buy.objects.all()
    return render(request, "buy.html", {"buys": buy})
    
def do_search(request):
    buy = Buy.objects.filter(name__icontains=request.GET['q'])
    return render(request,"buy.html",{"buys": buy})
    
def buy_details(request, id):
    this_buy = get_object_or_404(Buy, pk=id)
    buy_images = BuyImage.objects.filter(pk=id)
    return render(request, "buy_details.html", {"buys" : this_buy, 'buy_images': buy_images})
