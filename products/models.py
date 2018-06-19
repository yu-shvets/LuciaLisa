from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class CommonInfo(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created']

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Category(MPTTModel):

    class Meta(object):
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=256, verbose_name='title')
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children',
                            db_index=True, on_delete=models.CASCADE, verbose_name='parent сategory')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return "{}".format(self.title)


class Item(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Item"
        verbose_name_plural = "Items"

    TYPE_CHOICES = (('Men', 'Men'),
                    ('Women', 'Women'))

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=256, verbose_name='name')
    title_image = models.ImageField(upload_to='catalogue/products', verbose_name='title image')
    description = models.TextField(blank=True, null=True, verbose_name='description')
    type = models.CharField(choices=TYPE_CHOICES, max_length=9, blank=True, default='---------', verbose_name='type')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='сategory')
    recommended_items = models.ManyToManyField('self', blank=True, verbose_name='recommended')
    sales = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.sales:
            for item in self.specs_set.all():
                item.sales_price = item.price - item.price * self.sales / 100
                item.save()
        else:
            for item in self.specs_set.all():
                item.sales_price = None
                item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.category, self.title)

    def get_first_specs(self):
        return Specs.objects.filter(item=self).first()


class Image(models.Model):

    class Meta(object):
        verbose_name = "Image"
        verbose_name_plural = "Images"

    image = models.ImageField(upload_to='catalogue/products', verbose_name='image')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='item')

    def __str__(self):
        return "{}-{}".format(self.item, self.image)


class Specs(models.Model):

    class Meta(object):
        verbose_name = "Specs"
        verbose_name_plural = "Specs"

    weight = models.FloatField(blank=True, null=True, verbose_name='weight, gr')
    size = models.FloatField(blank=True, null=True, verbose_name='size')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='price')
    sales_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    specs = models.TextField(blank=True, null=True, verbose_name='other specs')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Feedback(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback"

    name = models.CharField(max_length=256, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    feedback = models.TextField(verbose_name='feedback')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.item, self.name)
