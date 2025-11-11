from django.db import models

import uuid

from multiselectfield import MultiSelectField

from embed_video.fields import EmbedVideoField


# Create your models here.

class BaseClass(models.Model):

    uuid=models.UUIDField(unique=True,default=uuid.uuid4)

    active_status=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    class Meta:

        abstract=True

class IndustryChoices(models.TextChoices):

    MOLLYWOOD='Mollywood','Mollywood'

    HOLLYWOOD='Hollywood','Hollywood'

    BOLLYWOOD='Bollywood','Bollywood'

    TOLLYWOOD='Tollywood','Tollywood'

class CerificationChoices(models.TextChoices):

    A='A','A'

    UA='U/A','U/A'

    U='U','U'

    S='S','S'

class GenreChoices(models.TextChoices):

    ACTION = 'Action','Action'

    ROMANTIC = 'Romantic','Romantic'

    THRILLER = 'Thriller','Thriller'

    COMEDY = 'Comedy','Comedy'

    HORROR = 'Horror','Horror'

class ArtistsChoices(models.TextChoices):

    MOHANLAL = 'Mohanlal','Mohanlal'

    MAMMOOTTY = 'Mammootty','Mammootty'

    NIVINPAULY = 'Nivin Pauly','Nivin Pauly'

class LanguagesChoices(models.TextChoices):

    MALAYALAM = 'Malayalam','Malayalam'

    ENGLISH = 'English','English'

    HINDI = 'Hindi','Hindi'

    TAMIL = 'Tamil','Tamil'

    TELUGU = 'Telugu','Telugu'

    KANNADA = 'Kannada','Kannada'

class Movie(BaseClass):

     name=models.CharField(max_length=30)

     photo = models.ImageField(upload_to='movies/banner-images')

     description = models.TextField()

     release_date=models.DateField()

     industry=models.CharField(max_length=20,choices=IndustryChoices.choices)    

     runtime=models.TimeField()

     certification=models.CharField(max_length=5,choices=CerificationChoices.choices)  
     
     genre = MultiSelectField(choices=GenreChoices.choices)

     artists = MultiSelectField(choices=ArtistsChoices.choices)

     video = EmbedVideoField()

     tags = models.TextField()

     languages = MultiSelectField(choices=LanguagesChoices.choices)
     
     class Meta:
        
        verbose_name = 'Movies'

        verbose_name_plural = 'Movies'
        
        def __str__(self):
        
            return f'{self.name}'
    


     
