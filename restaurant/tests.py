from django.test import TestCase
from django.urls import reverse
import json

from . import models


# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = models.MenuItem.objects.create(title="Ice Cream", price=80, inventory=100)
        self.assertEqual(str(item), "Ice Cream : 80")


class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model
        models.MenuItem.objects.create(title='Item 1', price=10.99, inventory=5)
        models.MenuItem.objects.create(title='Item 2', price=7.99, inventory=10)
        models.MenuItem.objects.create(title='Item 3', price=5.49, inventory=15)

    def test_get_all(self):
        # Retrieve all the models.MenuItem objects added for the test purpose
        url = reverse('menu-items')  # Replace 'menu-list' with the actual URL title of your view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the retrieved data
        serialized_data = json.loads(response.content)

        # Get all the models.MenuItem objects from the database
        all_menus = models.MenuItem.objects.all()

        # Check if the number of serialized items matches the number of objects in the database
        self.assertEqual(len(serialized_data), all_menus.count())

        # Optionally, you can check if the serialized data matches the expected values
        for i, menu in enumerate(all_menus):
            self.assertEqual(str(serialized_data[i]['title']), str(menu.title))
            self.assertEqual(float(serialized_data[i]['price']), float(menu.price))
            self.assertEqual(int(serialized_data[i]['inventory']), int(menu.inventory))

