from django.test import TestCase
from addresses.models import Address


class AddressModelTest(TestCase):
    def test_zip_code_properties(self):
        result = Address._meta.get_field("zip_code").null
        message = "Verifique se a propriedade result não pode ser null."
        self.assertFalse(result, message)
        
    def test_street_properties(self):
        result = Address._meta.get_field("street").null
        message = "Verifique se a propriedade result não pode ser null."
        self.assertFalse(result, message)

        expected = 50
        result = Address._meta.get_field("street").max_length
        message = f"Verifique se a propridade street possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)

    def test_number_properties(self):
        result = Address._meta.get_field("number").null
        message = "Verifique se a propriedade result não pode ser null."
        self.assertFalse(result, message)

        expected = 50
        result = Address._meta.get_field("number").max_length
        message = f"Verifique se a propridade number possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)


    def test_city_properties(self):
        result = Address._meta.get_field("city").null
        message = "Verifique se a propriedade city não pode ser null."
        self.assertFalse(result, message)

        expected = 50
        result = Address._meta.get_field("city").max_length
        message = f"Verifique se a propridade city possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)

    def test_state_properties(self):
        result = Address._meta.get_field("state").null
        message = "Verifique se a propriedade state não pode ser null."
        self.assertFalse(result, message)

        expected = 50
        result = Address._meta.get_field("state").max_length
        message = f"Verifique se a propridade state possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)

    def test_country_properties(self):
        result = Address._meta.get_field("country").null
        message = "Verifique se a propriedade country não pode ser null."
        self.assertFalse(result, message)

        expected = 50
        result = Address._meta.get_field("country").max_length
        message = f"Verifique se a propridade country possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)
