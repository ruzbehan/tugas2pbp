# Create your tests here.
from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def setUp(self):
        # Membuat beberapa objek Product untuk digunakan dalam testing
        Product.objects.create(name="Laptop", price=15000, description="Laptop high-end", quantity=10)
        Product.objects.create(name="Mouse", price=200, description="Wireless mouse", quantity=50)

    def test_main_url_is_exist(self):
        # Test apakah URL utama '/' dapat diakses
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        # Test apakah view utama menggunakan template 'main.html'
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        # Test untuk halaman yang tidak ada, apakah menghasilkan 404
        response = Client().get('/nonexistent/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        # Test untuk memastikan produk berhasil dibuat
        laptop = Product.objects.get(name="Laptop")
        mouse = Product.objects.get(name="Mouse")

        self.assertEqual(laptop.price, 15000)
        self.assertEqual(laptop.quantity, 10)
        self.assertEqual(mouse.price, 200)
        self.assertEqual(mouse.quantity, 50)

    def test_string_representation(self):
        # Test untuk memastikan method __str__ mengembalikan name produk
        product = Product.objects.get(name="Laptop")
        self.assertEqual(str(product), product.name)

    def test_quantity_positive(self):
        # Test untuk memastikan quantity produk positif (atau >= 0)
        product = Product.objects.get(name="Laptop")
        self.assertGreaterEqual(product.quantity, 0)
