from django.db import models
from django.urls import reverse

class MyModelName(models.Model):
    """A typical class defining a model, derived from the class Model"""

    #Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field Documentation")

    #metadata
    class Meta:
        ordering=['-my_field_name']

    #Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName"""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in admin site etc.)"""
        return self.my_field_name