from django.db import models
from django.contrib import admin

class Auteur(models.Model):
    """
    Table photographe
    """
    #~ identifiant = models.AutoField(prymary_key = True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    nationalite = models.CharField(max_length=30)
    date1 = models.DateField (verbose_name='date de naissance')
    adresse = models.TextField (max_length=200)
    email = models.EmailField ()
    experience= models.TextField(max_length=200, blank=True)
    def __unicode__(self):
        return "%s %s" % (self.nom,self.prenom)


class Lieux(models.Model):

    cadre = models.CharField(max_length=15,choices= (('I','Interieur'),
                                                     ('E','Exterieur')))
    saison = models.CharField(max_length=15,choices= (('P','Printemps'),
                                                     ('E','Ete'),
                                                     ('A','Automne'),
                                                     ('H','Hiver')))
    type_in =models.CharField(max_length=15,verbose_name="type d'interieur",
                                            choices= (('M','Maison'),
                                                      ('B','Bureau'),
                                                      ('S','Studio'),
                                                      ('A','Autre')))
    type_ex =models.CharField(max_length=15,verbose_name="type d'exterieur",
                                            choices=(('V','Ville'),
                                                     ('V','Village'),
                                                     ('N','Nature')))
    def __unicode__(self):
        return "%s>%s>%s>%s" %(self.cadre,self.saison,self.type_in,self.type_ex)


class Photo(models.Model):
    """
    Table Image 
    """
    photographe = models.ForeignKey(Auteur)
    title = models.CharField(max_length=50 ,verbose_name = "Titre de l'image")
    format = models.CharField(max_length = 50)
    mode = models.CharField(max_length =30 , choices=(('N','N/B'),
                                                      ('C','Couleur')))
    date = models.DateField(verbose_name="date de prise de vue")
    type_p=models.CharField(max_length=20,
                                verbose_name="Type de prise de vue",
                            choices=(('A','Argentique'),
                                     ('N','Numerique')))
    photo = models.ImageField(upload_to="photos/")
    thumbnail = models.ImageField(upload_to="thumbnails/", editable=False)
    lieux = models.ForeignKey(Lieux)
    appareil = models.CharField(max_length=40,
                                verbose_name=u"Appareil utilise")
    sens = models.CharField(max_length=20,choices=(('H','Horizontale'),
                                                    ('V','Verticale'),
                                                    ('C','Carree')))
    description = models.TextField(max_length=200,blank=True)

    def save(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os 

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (500,500)

        # Ouvre la photo originale en utilisant la librairie PIL

        image = Image.open(self.photo)

        # convertir l'mage en mode RGB si necessaire
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')

        #Utilisation de PIL Image pour creer un thumbnail
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # sauvegarde du thumbnail 
        temp_handle = StringIO()
        image.save(temp_handle, 'JPEG')
        temp_handle.seek(0)

        # sauvegarde du champ thumbnail

        suf = SimpleUploadedFile(os.path.split(self.photo.name)[-1],
                temp_handle.read(), content_type='image/JPEG')
        self.thumbnail.save(suf.name+'.JPEG', suf, save=False)
        # Sauvegarde de l'instance photo
        super(Photo, self).save()

    class Admin:
        pass

    def __unicode__(self):
        return "%s" %(self.title)

        
        
admin.site.register(Photo)
admin.site.register(Auteur)
admin.site.register(Lieux)
