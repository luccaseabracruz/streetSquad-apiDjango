from django.test import TestCase
from products.models import Product


class AddressModelTest(TestCase):
    def test_name_properties(self):
        result = Product._meta.get_field("name").null
        message = "Verifique se a propriedade name não pode ser null."
        self.assertFalse(result, message)

        expected = 120
        result = Product._meta.get_field("name").max_length
        message = f"Verifique se a propridade name possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)

        
    def test_category_properties(self):
        result = Product._meta.get_field("category").null
        message = "Verifique se a propriedade category não pode ser null."
        self.assertFalse(result, message)

        result = Product._meta.get_field("category").choices
        expected_choices = ["roupas", "calçados", "acessórios"]
        message = f"Verifique se a propriedade category foi definida de acordo com a lista de choices {expected_choices}"
        result_choices = [choice[0] for choice in result]
        for choice in expected_choices:
            self.assertIn(choice, result_choices, message)

        
    def test_price_properties(self):
        result = Product._meta.get_field("price").null
        message = "Verifique se a propriedade price não pode ser null."
        self.assertFalse(result, message)
        
    def test_stock_quantity_properties(self):
        result = Product._meta.get_field("stock_quantity").null
        message = "Verifique se a propriedade stock_quantity não pode ser null."
        self.assertFalse(result, message)
        
    def test_url_field_properties(self):
        result = Product._meta.get_field("url_field").null
        message = "Verifique se a propriedade url_field pode ser null."
        self.assertTrue(result, message)

    def test_created_at_properties(self):
        result = Product._meta.get_field("created_at").auto_now_add
        message = f"Verifique se a propriedade 'auto_now_add' de 'created_at' foi definida."
        self.assertTrue(result, message)

    def test_updated_at_properties(self):
        result = Product._meta.get_field("updated_at").auto_now
        message = f"Verifique se a propriedade 'auto_now' de 'updated_at' foi definida."
        self.assertTrue(result, message)