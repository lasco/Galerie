from django.shortcuts import render_to_response,HttpResponseRedirect
from afrikimage.models import * 
from form import SearchForm ,PhotoForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.http import Http404
from django.core.files.uploadedfile import SimpleUploadedFile





def my_custom_404_view(request):
    """
    """
    return render_to_response('404.html', {})

def home(request):
    a = Photo.objects.order_by("-date")[:5]
    
    return render_to_response('home.html',{'a':a})

#~ def home(request, *args, **kwargs):
    #~ num = kwargs["num"] or 1
    #~ photo = Photo.objects.all()
    #~ #on charge toutes photos de base de donnee
    #~ paginator = Paginator(photo,3)
    #~ try:
        #~ page = paginator.page(int(num))
    #~ 
    #~ except EmptyPage:
        #~ #affiche une erreur 404 personnalise si la page est vide
        #~ raise Http404
    #~ #s'execute si le numero de la page est 2
    #~ page.is_before_first = (page.number == 2)
    #~ #si le numero de la page est egale au numero de l'avant 
    #~ #de l'anvant dernier
    #~ page.is_before_last = (page.number == paginator.num_pages - 1)
    #~ #on constitue l'url de la page suivante
    #~ page.url_next = reverse('home', args=[int(num) + 1])
    #~ #on constititue l'url de page precedente
    #~ page.url_previous = reverse('home',args=[int(num) - 1])
    #~ #constitue l'url de la premiere page
    #~ page.url_first = reverse('home')
    #~ #on constitue l'url de la derniere page
    #~ page.url_last = reverse('home', args = [paginator.num_pages])
    #~ ctx = {'page':page,'paginator':paginator}
    #~ 
    #~ return render_to_response('home.html',ctx)
    
def photographe (request):
    photogr = Auteur.objects.all()

    return render_to_response('photographe.html',{'photogr':photogr})

def galerie(request):
    a = Photo.objects.select_related().order_by("photographe__nom")
    return render_to_response('galerie.html',{'a':a})

    
def add_photo(request):
    c = {}
    c.update(csrf(request))
    form = PhotoForm()
    c =({'form':form})
    if request.method == 'POST':
        #~ from ipdb import set_trace; set_trace()
        form = PhotoForm(request.POST,request.FILES)
        img = request.POST['photo']
        data=   {
                    'photographe': request.POST['photographe'],\
                    'title': request.POST['title'],\
                    'format': request.POST['format'],\
                    'mode': request.POST['mode'],\
                    'date':request.POST['date'],\
                    'type_p': request.POST['type_p'],\
                    'lieux':request.POST['lieux'],\
                    'appareil':request.POST['appareil'],\
                    'sens': request.POST['sens'],\
                    'description':request.POST['description'],\
                }
        print data
        file_data = {'photo':SimpleUploadedFile(img)}
        print file_data
        
        form = PhotoForm(data,file_data)
        #~ from ipdb import set_trace; set_trace()
        #~ if form.is_valid():
            #~ form.save()
            #~ return HttpResponseRedirect(reverse('home'))
        c.update({'form':form})
    c.update(csrf(request))
    return render_to_response('add_photo.html',c)
    


def auteur (request):
    #on initialise une dictionnaire vide
    c = {}
    c.update(csrf(request))
    # charge le formulaire dans le fichier form.py
    form = SearchForm()
    c=({'form':form})
    if request.method == 'POST':
        name = request.POST['nom']
        last_name = request.POST['prenom']
        try:
            autor = Photo.objects.filter(photographe__nom =name,photographe__prenom=last_name)
            info = autor[0]
            c.update({'autor':autor,'info':info})
        except:
            error ="ce photographe n est pas dans la base de donnee"
            c.update({'error':error,'form':form})
    c.update(csrf(request))
    return render_to_response('auteur.html',c)
