from django.conf.urls.defaults import *
import settings 
from settings import MEDIA_ROOT, DEBUG
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'afrikimage.views.home',name='home'),

    url(r'^auteur$', 'afrikimage.views.auteur',name='auteur'),

    url(r'^galerie/(?P<num>\d+)*$','afrikimage.views.galerie',name='galerie'),

    url(r'^photographes$', 'afrikimage.views.photographe',name='photographe'),

    url(r'^ajoutphoto$' , 'afrikimage.views.add_photo',name='ajoutphoto'),
    
    url(r'^ajoutautor$', 'afrikimage.views.add_autor',name='ajoutautor'),

    url(r'^infoauteur/(?P<id>\d+)$','afrikimage.views.infoauteur',name='infoauteur'),

    url(r'^ajout_lieux$' , 'afrikimage.views.add_lieux' , name = 'ajout_lieux'),
    
    url(r'^admin/', include(admin.site.urls)),
    


    url(r'^static/(?P<path>.*)$', 
             'django.views.static.serve',
             {'document_root': MEDIA_ROOT, 'show_indexes': True}),
)
handler404 = "galerie.afrikimage.views.my_custom_404_view"
