from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"


class Products(models.Model):
    TABLETS = 'tabs'
    CAPSULES = 'caps'
    POWDER = 'pow'
    TOFFEES = 'tof'
    TABSANDCAPS = 'tc'
    TABSCAPSPOW = 'tcp'
    OTHER = 'ot'

    release_form_choices = (
        (TABLETS ,'Tablets'),
        (CAPSULES ,'Capsules'),
        (POWDER, 'Powder'),
        (TOFFEES, 'Toffees'),
        (TABSANDCAPS, 'Tablets and Capsules'),
        (TABSCAPSPOW, 'Tablets, capsules and powder'),
        (OTHER, 'Other'),
    )
     
   

    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    model = models.CharField(max_length=200, blank=True)
    brand = models.CharField(max_length=200, default='Orthomol pharmazeutische Vertriebs GmbH')
    release_form = models.CharField(max_length=120, choices=release_form_choices, default='Capsules')
    course_duration = models.IntegerField(blank=True, default='30')
    expiration_date = models.DateTimeField(blank=True)
    category = models.ForeignKey(to="Categories", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} quantity - {self.quantity}"

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount / 100, 2)
        return self.price

    class Meta:
        db_table = "product"
