from django.test import TestCase
from users.models import User
from addresses.models import Address
from requests.models import Request
from products.models import Product


class UserModelTest(TestCase):
    def test_username_properties(self):
        expected = 150
        result = User._meta.get_field("username").max_length
        message = f"Verifique se a propridade username possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)

        result = User._meta.get_field("username").unique
        message = "Verifique se a propridade username foi definida como única."
        self.assertTrue(result, message)

        result = User._meta.get_field("username").null
        message = f"Verifique se a propriedade username não pode ser null."
        self.assertFalse(result, message)

    def test_email_properties(self):
        expected = 70
        result = User._meta.get_field("email").max_length
        message = f"Verifique se a propridade email possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)

        result = User._meta.get_field("email").unique
        message = "Verifique se a propridade email foi definida como única."
        self.assertTrue(result, message)

        result = User._meta.get_field("email").null
        message = f"Verifique se a propriedade email não pode ser null."
        self.assertFalse(result, message)

    def test_contact_properties(self):
        expected = 20
        result = User._meta.get_field("contact").max_length
        message = f"Verifique se a propridade contact possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)

        result = User._meta.get_field("contact").null
        message = f"Verifique se a propriedade contact não pode ser null."
        self.assertFalse(result, message)

    def test_full_name_properties(self):
        expected = 120
        result = User._meta.get_field("full_name").max_length
        message = f"Verifique se a propridade full_name possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)

        result = User._meta.get_field("full_name").null
        message = f"Verifique se a propriedade full_name não pode ser null."
        self.assertFalse(result, message)

    def test_is_seller_properties(self):
        result = User._meta.get_field("is_seller").null
        message = "Verifique se a propriedade is_seller tem a possibilidade de ser null."
        self.assertTrue(result, message)

        expected = False
        result = User._meta.get_field("is_seller").default
        message = f"Verifique se a propriedade is_seller possui {expected} como default."
        self.assertEqual(expected, result, message)

    def test_created_at_properties(self):
        result = User._meta.get_field("created_at").auto_now_add
        message = f"Verifique se a propriedade 'auto_now_add' de 'created_at' foi definida."
        self.assertTrue(result, message)

    def test_updated_at_properties(self):
        result = User._meta.get_field("updated_at").auto_now
        message = f"Verifique se a propriedade 'auto_now' de 'updated_at' foi definida."
        self.assertTrue(result, message)

    def test_password_properties(self):
        result = User._meta.get_field("password").null
        message = f"Verifique se a propriedade password não pode ser null."
        self.assertFalse(result, message)

        expected = 120
        result = User._meta.get_field("password").max_length
        message = f"Verifique se a propridade password possui max_length definida como {expected}."
        self.assertEqual(expected, result, message)


class UserAddressRelationTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create_user(
            username="client",
	        email="client@mail.com",
	        password="Senha1234!",
	        contact="99999999",
	        full_name="Client Teste",
        )

        cls.address = Address.objects.create(
            zip_code="71500500",
            street="x street",
            number = 100,
            city="Gotham City",
            state="Gotham",
            country="DC Country",
            user=cls.user
        )
    
    def test_if_a_user_can_have_one_address(self):
        self.assertIs(self.user, self.address.user)

    def test_if_a_address_can_have_one_user(self):
        self.assertIs(self.address, self.user.address)
