from dyn.tm.session import DynectSession
import os

# Login DynDNS
def login_dyndns():
    customer = os.environ.get('customer')
    username = os.environ.get('username')
    password = os.environ.get('password')

    my_session = DynectSession(customer, username, password)

# Delete TXT record
def delete_txtrecord():

    zone = os.environ.get('zone')
    fqdn = os.environ.get('fqdn')
    txtdata = os.environ.get('CERTBOT_VALIDATION')
    ttl = os.environ.get('ttl')
    
    classdyn.tm.records.TXTRecord(zone, fqdn, txtdata, ttl, delete=True)

login_dyndns()
delete_txtrecord()