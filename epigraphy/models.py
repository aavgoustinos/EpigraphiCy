from django.db import models 
from storages.backends.s3boto3 import S3Boto3Storage  # Import the S3Boto3Storage

from ckeditor.fields import RichTextField
from .constants import *
from django.contrib import admin
from django.utils.html import format_html
    
def photos(instance, filename):
    title = instance.title
    return f'{title}/photos/{filename}'
def files(instance, filename):
    title = instance.title
    return f'{title}/files/{filename}'



class Epigraphy(models.Model):
    
    place = models.ForeignKey('Monument', on_delete=models.SET_NULL, null=True, help_text="Corresponding to Site")
    title = models.CharField(max_length=100, help_text="Enter the ID")
    short_name = models.CharField(max_length=100,)

    
    image_1 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)  
    image_2 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)
    image_3 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)
    image_4 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)  
    image_5 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)
    image_6 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)
    image_7 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)
    image_8 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)
    image_9 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)
    image_10 = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)
                                  
                                  
                                  
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    past_location =  models.CharField(null=True, blank=True,max_length=1000)
    current_location =  models.CharField(null=True, blank=True,max_length=1000)

   
    
    object_type =  models.CharField(null=True, blank=True,max_length=600, choices=OBJECTTYPE)
    
    state_of_preservation =  models.CharField(null=True, blank=True,max_length=100, choices= STATEOFPRESERVATION)
    type_of_writing =  models.CharField(null=True, blank=True,max_length=200, choices=TYPEOFWRITING)
    language =  models.CharField(null=True, blank=True,max_length=50, choices=LANGUAGE)
    type_of_inscription =  models.CharField(null=True, blank=True,max_length=100, choices=TYPEOFINSCRIPTION)
    
    promoter =  models.CharField(null=True, blank=True,max_length=50, choices=PROMOTER)
    material =  models.CharField(null=True, blank=True,max_length=500, choices=MATERIAL)
    specific_material =  models.CharField(null=True, blank=True,max_length=100)
    administrative_district =  models.CharField(null=True, blank=True,max_length=100, choices=ADMINISTRATIVEDISTRICT)
    
    height =  models.CharField(null=True, blank=True,max_length=100)
    width =  models.CharField(null=True, blank=True,max_length=100)
    depth_diameter =  models.CharField(null=True, blank=True,max_length=100)
    letter_heights =  models.CharField(null=True, blank=True,max_length=100)

    
   
    #state_of_preservation =  models.CharField(null=True, blank=True,max_length=200)
    
    motivation =  models.CharField(null=True, blank=True,max_length=1000)

    day =  models.CharField(null=True, blank=True,max_length=100)
    month =  models.CharField(null=True, blank=True,max_length=100)

    year_from =  models.CharField(null=True, blank=True,max_length=100)
    year_to =  models.CharField(null=True, blank=True,max_length=100)
    
    
    description =  RichTextField(null=True, blank=True,default=None)
    bibliography =  RichTextField(null=True, blank=True,default=None)
    transcription_interpreted =  RichTextField(null=True, blank=True,default=None)
    transcription_diplomatic =  RichTextField(null=True, blank=True,default=None)
    translation =  RichTextField(null=True, blank=True,default=None)
    apparatus =  RichTextField(null=True, blank=True,default=None)
 
     
    full_epidoc_xml = models.FileField(null=True,blank=True,upload_to=files,storage=S3Boto3Storage(),)

    RTI_URL = models.URLField(null=True, blank=True,max_length = 100)
    
    three_dimensional_URL = models.URLField(null=True, blank=True,max_length = 100)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    iconographic_elements = models.ManyToManyField("IconographicElement",  blank=True,)
  

    # Prepopulate from the title field the image_one
    def save(self, *args, **kwargs):
        if not self.image_1:
            self.image_1 = self.title
        super().save(*args, **kwargs)

        
    
    def __str__(self):
        return self.title
    
    
    
    

    class Meta:
        verbose_name = "Inscription"
        verbose_name_plural = "Inscriptions"



class Monument(models.Model):
    
    TYPE = (
        ('Castle', 'Castle'),
        ('Lintel', 'Lintel'),
    )
    
    title = models.CharField(max_length=100, help_text=" Site")
    type =  models.CharField(null=True, blank=True,max_length=20, choices=TYPE)
    
    site_image = models.ImageField(null=True,blank=True,upload_to=photos,storage=S3Boto3Storage(),)  
    
    three_dimensional_URL = models.URLField(null=True, blank=True,max_length = 100)
    three_360_URL = models.URLField(null=True, blank=True,max_length = 100)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True,default=None)
    bibliography = RichTextField(null=True, blank=True,default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"



class IconographicElement(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
   
     
