from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=250, verbose_name='Categorys', unique=True)
    imgcat = models.ImageField(upload_to='imgcategory/%Y/%m/%d/', verbose_name='Photo Category', blank=True)

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Tag')
    slug = models.SlugField(max_length=50, verbose_name='Url Tag', unique=True)

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

class LevelofDifficulty(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Level of difficulty')
    slug = models.SlugField(max_length=50, verbose_name='Url Level of difficulty', unique=True)

    def get_absolute_url(self):
        return reverse_lazy('levelofdifficulty', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=50, verbose_name='Url Product', unique=True, blank=True)
    shortcontent = models.TextField(verbose_name='Brief product description')
    content = models.TextField(verbose_name='Full product description')
    hour = models.PositiveSmallIntegerField(validators=[MaxValueValidator(23)], null=True, blank=True, default=0, verbose_name='hour')
    minutes = models.PositiveSmallIntegerField(validators=[MaxValueValidator(59)], null=True, blank=True, default=0, verbose_name='minutes')
    price = models.DecimalField(max_digits=19, decimal_places=3, null=True, verbose_name='Price')
    levelofdifficulty = models.ForeignKey(LevelofDifficulty, on_delete=models.PROTECT, null=True, verbose_name='Level of Difficulty',
                                 related_name='product')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Product category',
                                 related_name='product')
    tags = models.ManyToManyField(Tag, blank=True, related_name='product')
    photo_preview = models.ImageField(upload_to='photo_preview/%Y/%m/%d/', verbose_name='Photo preview', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published/Unpublished')
    date_posted = models.DateTimeField(default=timezone.now, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
