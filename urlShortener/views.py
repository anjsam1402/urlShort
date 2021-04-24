from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from .models import URL, createHash

@csrf_protect
def home(request):
	return render(request, 'index.html')
@csrf_protect
def trim(request):
   url = request.GET["url"]

   try:
      check = URL.objects.get(full_url__exact = url)
      shortUrl = check.url_hash
   except URL.DoesNotExist:
      entry = URL(full_url=url)
      shortUrl = createHash(url)
   return render(request, 'index.html',{
         'shrinkedURL':shortUrl
		})

def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()

    return redirect(url.full_url)