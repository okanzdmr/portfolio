from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify

class Technology(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
    def p(self):
        from projects.models import Project
        return Project.objects.filter(categories__id=self.id)
class Project(models.Model):
    title = models.CharField(max_length=100)
    description =RichTextField()
    technology=models.ManyToManyField("Technology",related_name='tech')
    slug = models.SlugField(unique=True, editable=False, max_length=330)
    published_date = models.DateTimeField(auto_now_add=True,
        blank=True, null=True)
    model_pic = models.ImageField(upload_to='pic_folder/',blank=False)
    codepen=models.CharField(max_length=50,blank=True)
    link=models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Project.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self,force_insert=False, force_update=False, *args, **kwargs):
        if self.pk:
            orig = Project.objects.get(pk=self.pk).title
            if self.title==orig:
                print("title same")
                return super(Project, self).save(*args, **kwargs)
            else:
                print("title changed")
                self.slug = self.get_unique_slug()
                return super(Project, self).save(*args, **kwargs)

        else:
            self.slug = self.get_unique_slug()
            return super(Project, self).save(*args, **kwargs)
