from django.test import TestCase
from .models import Product, Box
from .utils import find_best_box


class FindBestBoxTests(TestCase):

    def setUp(self):
        # This runs before EVERY test below.
        # We create a few sample boxes here so we can test selection logic.

        self.small_box = Box.objects.create(
            name="Small Box",
            length=10, width=10, height=10,
            max_weight=2, cost=20
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            length=20, width=20, height=20,
            max_weight=5, cost=30
        )

        self.large_box = Box.objects.create(
            name="Large Box",
            length=30, width=30, height=30,
            max_weight=10, cost=50
        )

        # An expensive box that's the same size as medium box,
        # so we can test "pick cheapest among options that fit"
        self.medium_box_expensive = Box.objects.create(
            name="Medium Box (Pricey)",
            length=20, width=20, height=20,
            max_weight=5, cost=45
        )
        
    def test_product_fits_smallest_box(self):
        product = Product(
            name="Tiny Item",
            length=5, width=5, height=5,
            weight=1
        )

        result = find_best_box(product)
        self.assertEqual(result, self.small_box)
        
        
    def test_cheapest_box_selected_when_multiple_fit(self):
        product = Product(
            name="Medium Item",
            length=18, width=18, height=18,
            weight=4
        )

        result = find_best_box(product)

        self.assertEqual(result, self.medium_box)
        
    def test_no_box_fits_returns_none(self):
        product = Product(
            name="Oversized Item",
            length=50, width=50, height=50,
            weight=100
        )

        result = find_best_box(product)

        self.assertIsNone(result)