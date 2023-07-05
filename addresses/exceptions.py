from rest_framework.exceptions import APIException, status


class VerifyAddress(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "This user already has an address."
