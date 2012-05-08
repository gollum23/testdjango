# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404
from django.shortcuts import get_list_or_404
from models import *
import os
from django.conf import settings


def index(request,num):
    try:
        nacional = Article.objects.filter(category=1,
                                          edition=num).order_by('order')
        internacional = Article.objects.filter(category=2,
                                               edition=num).order_by('order')
        agenda = Article.objects.filter(category=3,edition=num)
        hum = Article.objects.filter(category=4,edition=num)
        edi = Edition.objects.get(ed=num)
    except Edition.DoesNotExist:
        raise Http404
    return render_to_response('index.html',{'articulosN':nacional,
                                            'articulosI':internacional,
                                            'agenda':agenda,
                                            'humor':hum,
                                            'edicion':edi})

def article(request,num,article):
    try:
        detail = Article.objects.get(order=article,edition=num)
        edi = Edition.objects.get(ed=num)
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('articulo.html',{'detalle':detail,
                                               'edicion':edi,})

def humor(request,num):
    myfiles = settings.MEDIA_ROOT+'/humor/'+num+'/'
    try:
        os.chdir(myfiles)
        x=0
        d={}
        for file in os.listdir("."):
            d[x]=('/humor/'+num+'/'+file)
            x=x+1
    except os.error:
        raise Http404
    return render_to_response('humor.html',{'imghumor':d})

def custom404(self):
    return render_to_response('404.html')