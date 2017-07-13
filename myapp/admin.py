from myapp.models import book,genre,reviews
from django.contrib import admin
#from models import book
# Register your models here.

@admin.register(book)
class bookAdmin(admin.ModelAdmin):
	pass

@admin.register(genre)
class genreAdmin(admin.ModelAdmin):
	pass

@admin.register(reviews)
class reviewsAdmin(admin.ModelAdmin):
	pass