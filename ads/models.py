from django.db import models

class RecipeModel(models.Model):
    banner_image = models.CharField(max_length=250,default=True)
    slug_title = models.CharField(max_length=250, blank=True)
    title = models.CharField(max_length=250)
    recipe = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title:
            self.slug_title = self.title.replace(" ", '-')
        super(RecipeModel, self).save(*args, **kwargs)


class SEO(models.Model):
    seo_data = models.TextField()

    def __str__(self):
        return self.seo_data[:90]