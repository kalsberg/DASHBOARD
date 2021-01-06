import json

from ldap3 import ALL, Server, Connection
from DASHBOARD import settings as root_settings


def establish_ldap_connection():
    """
    Connects to LDAP server
    :return: conn (Connection Object)
    """
    # Connect to server
    server = Server(root_settings.LDAP_SERVER, get_info=ALL)
    domain = "{0}@contiwan.com".format(root_settings.SYS_USER_ID)
    password = root_settings.SYS_USER_PWD
    conn = Connection(server, domain, password)
    conn.bind()
    return conn


def validate_user(username, conn):
    """
    Validates if input user exists in LDAP
    :param username: Username
    :param conn: Connection Object
    :return: boolean (user existence)
    """
    # Search for user
    search_filter = '(sAMAccountName={0})'.format(username)
    conn.search('dc=contiwan,dc=com', search_filter,  attributes=['displayName'])

    # Retrieve Full Name and username
    entries = conn.entries
    attributes = (json.loads(entries[0].entry_to_json()))['attributes']
    name = ' '.join(attributes['displayName'][0].split(', ')[::-1])
    return name if len(entries) else False