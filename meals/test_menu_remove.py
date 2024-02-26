from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from django.test import TestCase, Client
from django.urls import reverse
from .models import Meal
from .admin import MealAdmin


class AdminRemoveItemTestCase(TestCase):
    '''
    This test case is used to remove items from
    the menu using the admin interface.
    '''
    def setUp(self):
        # Create a superuser
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )

        # Initialize the client and log in as the superuser
        self.client = Client()
        self.client.login(username='admin', password='adminpassword')

        # Add items to the menu
        categories = ['Entree', 'Side Dishes', 'Desserts']
        for category in categories:
            meal_data = {
                'name': f'Test Meal {category}',
                'description': f'Test description for {category}',
                'people': 1,
                'price': 9.99,
                'calories': 500,
                'allergens': 'Test Allergens',
                'preparation_time': 20,
                'slug': f'test-{category.lower()}',
                'category': category
            }
            # Add the item to the menu
            self.client.post(reverse('admin:meals_meal_add'), meal_data)
            print(f"Added {category} to the menu.")

    def test_remove_items(self):
        # Remove items from each category
        categories = ['Entree', 'Side Dishes', 'Desserts']
        for category in categories:
            meal = Meal.objects.get(name=f'Test Meal {category}')
            response_delete = self.client.post(
                reverse('admin:meals_meal_delete', args=(meal.id,))
            )
            print(f"Removed {category} from the menu.")

        # Register the Meal model with the custom admin site
        admin_site = AdminSite()
        admin_site.register(Meal, MealAdmin)
