from dyn.tm.session import DynectSession
from dyn.tm.records import TXTRecord
import os, time

# Login DynDNS
def login_dyndns():
    customer = os.environ.get('customer')
    username = os.environ.get('username')
    password = os.environ.get('password')

    DynectSession(customer, username, password)

# Create TXT record
def create_txtrecord():

    zone = os.environ.get('CERTBOT_ZONE')
    fqdn = os.environ.get('CERTBOT__FQDN')
    txtdata = os.environ.get('CERTBOT_VALIDATION')
    ttl = os.environ.get('CERTBOT_TTL')
    
    TXTRecord(zone, fqdn, txtdata, ttl, create=True)

# Sleep to make sure the change has time to propagate over to DNS

def delay():
    time.sleep(5)

login_dyndns()
create_txtrecord()
delay()