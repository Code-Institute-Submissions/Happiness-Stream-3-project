from django.shortcuts import render,get_object_or_404,redirect
from .models import Sell
from django.contrib.auth.decorators import login_required
from.forms import SellForm
from django.utils import timezone

# Create your views here.
@login_required
def create_for_sale_ad(request):
    if request.method == "POST":
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.seller = request.user
            ad.created_date = timezone.now()
            ad.save()
            return redirect('checkout')
    else:
        form = SellForm()
    return render (request, 'sell.html', {'form':form})

    
def do_search(request):
    sell = Sell.objects.filter(name__icontains=request.GET['q'])
    return render(request,"sell.html",{"sells":sells})