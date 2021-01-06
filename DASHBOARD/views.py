# Direct Imports
import json
import getpass

# Relative Imports
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from datetime import datetime

# Project Imports
from utilities.helpers import establish_ldap_connection, validate_user


def authenticate_user(request):
    """
    Authorizes logged user for portal accessibility.
    :return: response (Logged user details)
    """
    try:
        username = request.META['REMOTE_USER']
    except KeyError:
        username = getpass.getuser()
    # username = 'uidn7731'

    # Check in User model
    try:
        mdl_user = User.objects.get(username=username)
        response_status = status.HTTP_200_OK
        response_data = {'name': mdl_user.first_name, 'message': 'Successfully authenticated user',
                         'is_admin': mdl_user.is_superuser}
    except User.DoesNotExist:
        # Check in LDAP and create user
        ldap_connection = establish_ldap_connection()
        is_valid = validate_user(username, ldap_connection)
        if not is_valid:
            response_status = status.HTTP_401_UNAUTHORIZED
            response_data = {'name': None, 'is_admin': False,
                             'message': 'No such user exists in <i>LDAP: CW01 domain</i>.'}
        else:
            mdl_user = User.objects.create(username=username, first_name=is_valid, is_active=True,
                                           last_login=datetime.now())
            response_status = status.HTTP_200_OK
            response_data = {'name': mdl_user.first_name, 'is_admin': False,
                             'message': 'Successfully authenticated user'}
    return HttpResponse(json.dumps(response_data), content_type='application/json', status=response_status)