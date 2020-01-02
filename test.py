
from azure.identity import DefaultAzureCredential
from azure.keyvault.certificates import CertificateClient
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from datetime import datetime  
from datetime import timedelta
import requests, base64, os, slack
from slack import WebClient


# def f():  
#     s = "func1"
#     print (s)  

# def g():  
#     s = "func2"
#     print (s)

# f()
# g()

def sm(param1):
    sc = '@pedro.aguiar'
    su = 'Finacial Bot SRE'
    stk = os.environ.get('slacktoken')
    client = WebClient(token=stk)
    client.chat_postMessage(channel=sc, username=su,  text=param1)

def psm():
    if 1 == 1:
        sm('message 1')
    else:
        sm('message 2')
psm()