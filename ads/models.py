from django.db import models
from django.urls import reverse

class RecipeModel(models.Model):
    banner_image = models.CharField(max_length=250,default=True)
    slug_title = models.CharField(max_length = 250, null = True, blank = True)
    title = models.CharField(max_length=250)
    recipe = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title:
            self.slug_title = self.title.replace(" ", '-')
        super(RecipeModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ads:desktop_single_page_recipes', args=[self.slug_title])
    
    def get_absolute_url_mobile(self):
        return reverse('ads:mobile_single', args=[self.slug_title])

class SEO(models.Model):
    seo_data = models.TextField()

    def __str__(self):
        return self.seo_data[:90]