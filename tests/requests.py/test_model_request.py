from django.test import TestCase
from order_requests.models import Request


class RequestModelTest(TestCase):
    def test_status_properties(self):
        result = Request._meta.get_field("status").null
        message = "Verifique se a propriedade status pode ser null."
        self.assertTrue(result, message)

        expected = "realizado"
        result = Request._meta.get_field("status").default
        message = f"Verifique se a propriedade status possui {expected} como default."
        self.assertEqual(expected, result, message)

        result = Request._meta.get_field("status").choices
        expected_choices = ["realizado", "em andamento", "concluido"]
        message = f"Verifique se a propriedade status foi definida de acordo com a lista de choices {expected_choices}"
        result_choices = [choice[0] for choice in result]
        for choice in expected_choices:
            self.assertIn(choice, result_choices, message)


    def test_created_at_properties(self):
        result = Request._meta.get_field("created_at").auto_now_add
        message = f"Verifique se a propriedade 'auto_now_add' de 'created_at' foi definida."
        self.assertTrue(result, message)

    def test_updated_at_properties(self):
        result = Request._meta.get_field("updated_at").auto_now
        message = f"Verifique se a propriedade 'auto_now' de 'updated_at' foi definida."
        self.assertTrue(result, message)

    def test_product_quantity_properties(self):
        result = Request._meta.get_field("product_quantity").null
        message = "Verifique se a propriedade product_quantity não pode ser null."
        self.assertFalse(result, message)
