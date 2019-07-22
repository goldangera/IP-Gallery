from django.shortcuts import render, redirect 
from django.http import HttpResponse, Http404
from .models import Location,Category,Image
import pyperclip
# Create your views here.
def gen_pics(request):
   images = Image.objects.all()
   category_results = Category.objects.all()
   location_results = Location.objects.all()
   return render(request, 'all-pics/general.html', {"all_images":images})
def search_results(request):
   if 'searchItem' in request.GET and request.GET["searchItem"]:
       search_term = request.GET.get("searchItem")
       searched_image = Image.search_by_category(search_term)
       message = f"{search_term}"
       return render(request, 'all-pics/search.html', {"message": message, "searchItem": searched_image})
   else:
       message = "You haven't searched for any thing"
       return render(request, 'all-pics/general.html', {"message": message})
def get_category(request):
   category_results = Category.objects.all()
   location_results = Location.objects.all()
   return render(request, 'all-pics/general.html', {'category_results': category_results, 'location_results': location_results})
def get_location(request):
   category_results = Category.objects.all()
   location_results = Location.objects.all()
   return render(request, 'all-pics/general.html', { 'category_results': category_results, 'location_results': location_results})

