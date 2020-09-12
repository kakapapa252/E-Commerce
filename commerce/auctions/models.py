from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings


class User(AbstractUser):
    pass


class Listing(models.Model):
	idx = models.AutoField(primary_key=True)
	title = models.CharField(max_length=250)
	summary = models.TextField()
	price = models.DecimalField(max_digits=10,decimal_places=2)
	listing_date = models.DateTimeField("date_listed", default=timezone.now())
	thumbnail = models.ImageField(null=True, blank=True,)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,)

	def __str__(self):
		return (f"This product {self.title} has id: {self.idx}")


	

class Wishlist(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	wished_item = models.ForeignKey(Listing,on_delete=models.CASCADE)
	added_date = models.DateTimeField(default=timezone.now())
	slug = models.CharField(max_length=30, null=True, blank=True,)

	def __str__(self):
		return (f"This product {self.wished_item.title} has id: {self.wished_item.idx} added by {self.user}")

