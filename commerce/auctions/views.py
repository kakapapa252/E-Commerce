from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Listing, Wishlist
from .forms import CreateForm
from django.db.models import Q
from django.contrib import messages

def index(request):
    listings = Listing.objects.all().order_by("created_by").reverse()
    return render(request, "auctions/index.html", context={"listings":listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.info(request, f"Logged in as: {username}")
            return HttpResponseRedirect(reverse("index"))
        else:
                
            return render(request, "auctions/login.html")
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, f"Logged Out")
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, "Passwords must match.")
            return render(request, "auctions/register.html")
        if len(password)<4:
            messages.error(request, "Password Must Contain 4 Characters.")
            return render(request, "auctions/register.html")
        if '@' not in email or ('.com' not in email and '.in' not in email):
            messages.error(request, "Enter correct Email")
            return render(request, "auctions/register.html")
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error(request, "Username already taken.")
            return render(request, "auctions/register.html")
        login(request, user)
        messages.success(request, f"Logged in as: {username}")
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            commit = form.save(commit=False)
            commit.created_by = request.user 

            commit = commit.save()
            messages.success(request, f"Created!")
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Error Detected")
            return HttpResponseRedirect(reverse("create"))


    form = CreateForm
    return render(request, "auctions/create.html", context={"form": form})



def add_to_wishlist(request,idx):
    item = get_object_or_404(Listing,idx=idx)
    user = request.user
    wished_item,created = Wishlist.objects.get_or_create(wished_item=item, user =user,)
    if created:
        messages.success(request, f"Added To Wishlist") 
        wished_item.save()
    else:
        messages.info(request, f"Already in Wishlist!")
        wished_item.save()

    #print ('added',user,wished_item)
    return HttpResponseRedirect(reverse("wishlist"))


def wishlist(request):
    try:
        user = request.user
        items =  Wishlist.objects.filter(user=user)
        new_list = [i.wished_item.idx for i in items.all()]
        dates = [i.added_date for i in items.all()]
        listings = Listing.objects.in_bulk(new_list, field_name='idx')
        list_value = listings.values()
        lum_sum = 0
        for one in list_value:
            lum_sum += one.price
        """print(items.all())id
                    print('')
                    print(new_list)
                    print('')
                    print([(listings.values())])
                    
                    print(d)"""

        listings_dates = list(zip(list_value,dates))
        return render(request,"auctions/wishlist.html", context={"items":listings_dates,"lum_sum":lum_sum})
    except TypeError:
        return render(request,"auctions/not_auth.html")


def remove_from_wishlist(request,idx):
    try:
        user = request.user
        item = get_object_or_404(Listing,idx=idx)
        title = item.title
        wished_item = Wishlist.objects.get(wished_item=item, user =user,)
        wished_item.delete()
        messages.success(request, f"Removed {title}")
        return HttpResponseRedirect(reverse("wishlist"))
    except:
        messages.error(request, f"Unable to remove item.")
        return HttpResponseRedirect(reverse("wishlist"))


def item_page(request,idx):
    item = get_object_or_404(Listing,idx=idx)
    return render(request,"auctions/item_page.html", context={"item":item})


def my_created(request):
    try:
        user = request.user
        listings =  Listing.objects.filter(created_by=user)
        return render(request,"auctions/my_created.html", context={"listings":listings})
    except TypeError:
        return render(request,"auctions/not_auth.html")



def remove_from_created(request,idx):
    try:
        user = request.user
        created_item =  Listing.objects.get(idx=idx, created_by =user,)
        title = created_item.title
        created_item.delete()
        messages.success(request, f"Removed {title}")
        return HttpResponseRedirect(reverse("my_created"))
    except:
        messages.error(request, f"Unable to remove item.")
        return HttpResponseRedirect(reverse("my_created"))