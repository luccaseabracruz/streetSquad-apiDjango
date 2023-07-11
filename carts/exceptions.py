from rest_framework.exceptions import APIException, status


class VerifyOrderedQuantity(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Ordered quantity must be greater than 0."


class VerifyStockQuantity(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Ordered quantity is out of stock."


class VerifyStockQuantityAndOrderedQuantity(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Ordered quantity plus the quantity in your cart is out of stock"
