from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("create/", views.create, name="create"),
    path("add_to_wishlist/<idx>", views.add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("remove_from_wishlist/<idx>", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("item_page/<idx>", views.item_page, name="item_page"),
    path("my_created/", views.my_created, name="my_created"),
    path("remove_from_created/<idx>", views.remove_from_created, name="remove_from_created")
]
