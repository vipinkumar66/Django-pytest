from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(
        verbose_name="title",
        help_text="required",
        max_length=255
    )
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    description = models.TextField(
        verbose_name="description",
        help_text="Not Required",
        blank=True
    )
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name="Regular Price",
        help_text = "Not more than 999.99",
        error_messages={
            "name":{
                "max_length": "The price must be between 0.00 and 999.99"
            }
        },
        max_digits=5,
        decimal_places=2
    )
    discount_price = models.DecimalField(
        verbose_name="Discount Price",
        help_text="Not more than 999.99",
        error_messages={
            "name":{
                "max_length": "The price must be between 0.00 and 999.99"
            }
        },
        max_digits=5,
        decimal_places=2

    )
    created_at = models.DateTimeField("Created at", auto_now_add=True, editable=True)
    updated_at = models.DateTimeField("Update at", auto_now=True)

    def __str__(self):
        return self.title
