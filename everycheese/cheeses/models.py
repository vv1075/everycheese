from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField

class Cheese(TimeStampedModel):
     name = models.CharField("Name of Cheese", max_length=255)
     slug = AutoSlugField("Cheese Address",
        unique=True, always_update=False, populate_from="name")
     description = models.TextField("Description", blank=True)
     country_of_origin = CountryField( "Country of Origin", blank=True)
     
     class Firmness(models.TextChoices):
          UNSPECIFIED = "unspecified", "Unspecified"
          SOFT = "soft", "Soft"
          SEMI_SOFT = "semi-soft", "Semi-Soft"
          SEMI_HARD = "semi-hard", "Semi-Hard"
          HARD = "hard", "Hard"
          
     def get_absolute_url(self):
          """Return absolute URL to the Cheese Detail page."""
          return reverse(
               'cheeses:detail', kwargs={"slug": self.slug}
               )    
     # Other Fields Here...

     
     firmness = models.CharField("Firmness", max_length=20,
           choices=Firmness.choices, default=Firmness.UNSPECIFIED)
     
     def __str__(self):
         return self.name