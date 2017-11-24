from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View

from .models import KirrURL

# Create your views here.

def test_view(request):
    return HttpResponse("some stuff")

# FB: function based view
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # return HttpResponse("hello = {shortcode}".format(shortcode=obj.url)) ;
    return HttpResponseRedirect(obj.url)

# CB : class based view
class KirrCBView(View):
    def get(self, request,shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        # return HttpResponse("Hello again = {shortcode}".format(shortcode=shortcode)) ;
        return HttpResponseRedirect(obj.url)

    def post(self, request, *args, **kwargs):
        return HttpResponse()


'''
# FB: function based view
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):

    print(request.method)
    # try :
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = obj = KirrURL.objects.all().first()

    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url

    obj = get_object_or_404(KirrURL, shortcode=shortcode)

    return HttpResponse("hello = {shortcode}".format(shortcode=obj.url)) ;

'''