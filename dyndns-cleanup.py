from dyn.tm.session import DynectSession
from dyn.tm.records import TXTRecord
import os

# Login DynDNS
def login_dyndns():
    customer = os.environ.get('customer')
    username = os.environ.get('username')
    password = os.environ.get('password')

    DynectSession(customer, username, password)

# Delete TXT record
def delete_txtrecord():

    zone = os.environ.get('CERTBOT_ZONE')
    fqdn = os.environ.get('CERTBOT__FQDN')
    txtdata = os.environ.get('CERTBOT_VALIDATION')
    ttl = os.environ.get('CERTBOT_TTL')
    
    TXTRecord(zone, fqdn, txtdata, ttl, delete=True)

login_dyndns()
delete_txtrecord()