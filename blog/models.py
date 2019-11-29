
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, editable=False, max_length=330)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if self.pk:
            orig = Post.objects.get(pk=self.pk).title
            if self.title == orig:
                print("title same")
                return super(Post, self).save(*args, **kwargs)
            else:
                print("title changed")
                self.slug = self.get_unique_slug()
                return super(Post, self).save(*args, **kwargs)

        else:
            self.slug = self.get_unique_slug()
            return super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    author = models.CharField(max_length=40)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

