from django.core.management.base import BaseCommand
from products.models import Sku

class Command(BaseCommand):
    help = 'Update prices for existing Sku records'

    def handle(self, *args, **options):
        skus = Sku.objects.all()
        for sku in skus:
            sku.platform_commission = sku.selling_price * 0.25
            sku.cost_price = sku.selling_price - sku.platform_commission
            sku.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated prices for Sku records'))
