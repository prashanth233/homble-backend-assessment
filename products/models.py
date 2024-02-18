from datetime import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """
    Very basic structure. To be further built up.
    """
    edited_at = models.DateTimeField(
                _("edited at"),
                auto_now = True, 
                help_text = _("Timestamp of the most recent object edit."),)
    
    ingredients = models.CharField(_("ingredients"),
                max_length = 500,
                help_text = _("List of ingredients (max 500 chars)."),
                blank = True,
                null = True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.edited_at = timezone.now()
        super().save(*args, **kwargs)

    name = models.CharField(
        _("display name"),
        max_length=150,
        unique=True,
        help_text=_("This will be displayed to user as-is"),
    )
    selling_price = models.PositiveSmallIntegerField(
        _("selling price (Rs.)"),
        help_text=_("Price payable by customer (Rs.)"),
    )
    description = models.TextField(
        _("descriptive write-up"),
        unique=True,
        help_text=_("Few sentences that showcase the appeal of the product"),
    )
    is_refrigerated = models.BooleanField(
        help_text=_("Whether the product needs to be refrigerated"),
        default=False,
    )
    category = models.ForeignKey(
        "categories.Category",
        related_name="products",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    managed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="managed_products",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}" 

    class Meta:
        # Just to be explicit.
        db_table = "product"
        ordering = []
        verbose_name = "Product"
        verbose_name_plural = "Products"
class Sku(models.Model):
    MEASUREMENT_CHOICES = [
        ('gm', 'Grams'),
        ('kg', 'Kilograms'),
        ('mL', 'Milliliters'),
        ('L', 'Liters'),
        ('pc', 'Piece'),
    ]

    STATUS_CHOICES = [
        (0, 'Pending for approval'),
        (1, 'Approved'),
        (2, 'Discontinued'),
    ]

    product = models.ForeignKey(
        "products.Product",
        related_name="skus",
        on_delete=models.CASCADE
    )
    size = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(999)]
    )
    measurement_unit = models.CharField(
        max_length=2,
        choices=MEASUREMENT_CHOICES,
        default='gm'
    )
    selling_price = models.PositiveIntegerField()
    platform_commission = models.PositiveSmallIntegerField()
    cost_price = models.PositiveIntegerField()
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = 0  # Set default status to "Pending for approval"
            self.selling_price = self.platform_commission + self.cost_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.size} {self.measurement_unit} (Rs. {self.selling_price})"

    @property
    def markup_percentage(self):
        if self.cost_price != 0:
            return (self.platform_commission / self.cost_price) * 100
        return 0
    
    class Meta:
        db_table = "sku"
        ordering = []
        verbose_name = "SKU"
        verbose_name_plural = "SKUs"