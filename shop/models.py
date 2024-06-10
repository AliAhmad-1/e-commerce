from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy,reverse


class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True,null=True,blank=True)

    class Meta:
        ordering=['name']
        indexes=[
        models.Index(fields=['name'])
        ]
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if self.slug is None:
            self.slug=slugify(self.name)
        return super(Category,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shop:products_list_by_category", args=[self.slug])
    

class Product(models.Model):

    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='c_products')
    name=models.CharField(max_length=150)
    slug=models.SlugField(max_length=150,blank=True,null=True)
    image=models.ImageField(upload_to="products_image/%Y/%m/%d",blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']    
        indexes=[

        models.Index(fields=['id','slug']),
        models.Index(fields=['name']),
        models.Index(fields=['-created'])

        ]

    def get_absolute_url(self):
        return reverse_lazy("shop:product_detail", kwargs={"id": self.id,'slug':self.slug})
    
    def save(self,*args, **kwargs):
        if self.slug is None:
            self.slug=slugify(self.name)
        return super(Product,self).save(*args, **kwargs)