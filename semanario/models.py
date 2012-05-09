# coding=utf-8
from django.db import models
from ckeditor.fields import RichTextField
#from PIL import _imaging
# Tupla con categorias
categories = (('1','Nacional',),('2','Internacional',),('3','Agenda',),
              ('4','Humor',),)

# Tupla con colores de edición
colors = (('yellow','Amarillo'),('blue','Azul'),('red','Rojo'),)

# Tabla para almacenar autores
class Author(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nombre')
    bio = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.name)

# Tabla para las ediciones
class Edition(models.Model):
    def folder_up_banner(self,name):
        """
        Funcion para generar la ruta para almacenar el banner del head
        cuando exista
        """
        banner = 'images/'+self.ed+'/'+name
        return banner

    ed = models.CharField(max_length=4, verbose_name='Edición No', unique=True)
    dfrom = models.DateField(verbose_name='Fecha desde',)
    dto = models.DateField(verbose_name='Fecha hasta',)
    color = models.CharField(max_length=20,choices=colors,
                             verbose_name='Color de la edición')
    bannerh = models.FileField(upload_to=folder_up_banner,
                               verbose_name='Banner header',blank=True)
    linkbanner = models.CharField(max_length=255, verbose_name='Enlace ' \
                                                               'banner',
                                  blank=True)

    def __unicode__(self):
        return u'%s' % (self.ed)

# Tabla donde se guardan los articulos

class Article(models.Model):
    def folder_up_img(self,name):
        folder = 'images/'+self.edition.ed+'/'+name
        return folder

    def folder_up_pdf(self,name):
        folder = 'pdfs/'+self.edition.ed+'/'+name
        return folder

    edition = models.ForeignKey(Edition,to_field='ed', verbose_name='Edición '\
                                                                    'No:')
    category = models.CharField(max_length=20,choices=categories,
                                verbose_name='Categoria')
    order = models.CharField(max_length=2,verbose_name='Orden')
    title = models.CharField(max_length=255,verbose_name='Título')
    author = models.ForeignKey(Author,verbose_name='Autor',blank=True)
    abstract = RichTextField(verbose_name='Gancho',blank=True)
    imgthums = models.FileField(upload_to=folder_up_img,
                                verbose_name='Imágen gancho')
    imgarticle = models.FileField(upload_to=folder_up_img,
                                  verbose_name='Imágen artículo',blank=True)
    content = RichTextField(verbose_name='Contenido artículo',blank=True)
    readmore = models.BooleanField(verbose_name='Enlace leer más',default=True)
    pdf = models.FileField(verbose_name='PDF', upload_to=folder_up_pdf,
                           blank=True)