from dyn.tm.session import DynectSession
import os
def dyndns():
    customer = (os.environ.get('customer'))
    username = (os.environ.get('username'))
    password = (os.environ.get('password'))
    my_session = DynectSession(customer, username, password)
    # error: ogin: Credentials you entered are incorrect and/or you are logging in from an unauthorized network.. login: Login failed.
dyndns()