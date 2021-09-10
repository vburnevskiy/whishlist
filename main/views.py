from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import WishList
from .forms import ProductForm

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {"title": "Wishlist | about project"})

def list_page(request, pk):
    """
    FBV - function base view - наш случай
    CBV - class base view
    """
    # print('PK ', pk)
    # print(wishlist)
    wishlist = get_object_or_404(WishList, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        product = form.save()
        wishlist.product.add(product)
        wishlist.save()
        # form.save()
        # print(form.pk)
    elif request.method == "GET":
        form = ProductForm()
        # wishlist = get_object_or_404(WishList, pk=pk)
    return render(request,
                  'wish_list.html',
                  {'wishlist': wishlist,
                   'is_owner_list': wishlist.owner == request.user,
                   'form': form
                   }
                  )


