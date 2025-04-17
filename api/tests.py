from django.test import TestCase
import pickle

# Create your tests here.


# dev_28 시리얼라이제이션의 이해


def add_view(num1, num2):
    return num1 + num2


def suv_view(num1, num2):
    return num1 - num2


class ObjectAPITest(TestCase):
    def setUp(self):
        pass

    def test_path(self):

        dict = {
            "products": add_view,
            "categories": suv_view,
        }
        url = "products"

        print(dict[url](1, 2))

        url = "sub"
        print(dict[url](1, 2))
