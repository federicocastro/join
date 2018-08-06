from datetime import timedelta
from django.conf import settings

from authentication.serializers import UserAndPermissionsSerializer


def jwt_custom_response_payload_handler(token, user=None, request=None):
    """
    Custom JWT response.

    :param token:
    :param user:
    :param request:
    :return:
    """
    jwt_settings = getattr(settings, 'JWT_AUTH', {})
    refresh_limit_td = jwt_settings.get('JWT_REFRESH_EXPIRATION_DELTA', None)
    refresh_limit = 0
    if refresh_limit_td is not None and isinstance(refresh_limit_td, timedelta):
        refresh_limit = refresh_limit_td.total_seconds()
    return {
        'token': token,
        'refresh_limit': refresh_limit,
        'user': UserAndPermissionsSerializer(user).data if user else None
    }
