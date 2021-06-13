from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns




class place(models.Model):
    placename = models.CharField(max_length=200, default="#")
  
    placeimage = models.CharField(max_length=5000, null=True, blank=True, default="#")
    placetagline = models.CharField(max_length=200, default="#")
    placedescription1 = models.TextField(max_length=5000, null=True, blank=True, default="#")
    placedescription2 = models.TextField(max_length=5000, null=True, blank=True, default="#")
    placegooglemap = models.CharField(max_length=200, null=True, blank=True, default="#")
    

    def __str__(self):
        """String for representing the Model object."""
        return self.placename

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('place-detail', args=[str(self.id)])

