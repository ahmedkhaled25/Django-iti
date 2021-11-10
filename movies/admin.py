from django.contrib import admin
from .models import Movie, Cast, Category, Review

class InlineReview(admin.StackedInline):
    model = Review

class MovieAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    list_display = ('name', 'likes', 'rate')
    inlines = [InlineReview]

admin.site.register(Movie, MovieAdmin)

admin.site.register(Cast)
admin.site.register(Category)
admin.site.register(Review)

# Register your models here.
