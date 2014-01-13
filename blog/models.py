from django.db import models
import os
import PIL
import PIL.ImageOps

class Category(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

class Post(models.Model):
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public'),
        (3, 'Hidden'))
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date='created')
    body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    adopted = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name="posts")

    def __unicode__(self):
        return self.title

def image_path(instance, filename):
    return "images/{0}/{1}".format(instance.post.id, os.path.basename(filename))

class Image(models.Model):
    title = models.CharField(max_length=200)
    post = models.ForeignKey(Post, related_name='images')
    image = models.ImageField(upload_to=image_path)

    def save(self):
        super(Image, self).save()
        im = PIL.Image.open(self.image.path)
        im = PIL.ImageOps.fit(im, (100, 100), PIL.Image.ANTIALIAS, 0, (0.5, 0.0))
        im.save(self.thumbnail_path(), "JPEG")

    def thumbnail_path(self):
        file, ext = os.path.splitext(self.image.path)
        return file + ".thumbnail" + ".jpg"

    def __unicode__(self):
        return u'%s' % self.title
