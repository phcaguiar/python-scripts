from azure.identity import DefaultAzureCredential
from azure.keyvault.certificates import CertificateClient
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from datetime import datetime  
from datetime import timedelta
import requests, base64, os, slack
from slack import WebClient

def slack_message(slack_text):
    slack_channel = '@pedro.aguiar'
    slack_username = 'Finacial Bot SRE'
    slack_token = os.environ.get('slacktoken')
    client = WebClient(token=slack_token)
    client.chat_postMessage(channel=slack_channel, username=slack_username,  text=slack_text)

def queue_build():

    personal_access_token = os.environ.get('personal_access_token')
    base_url = os.environ.get('base_url')
    organization_name = os.environ.get('organization_name')
    project_name = os.environ.get('project_name')
    build_id = os.environ.get('build_id')
    fully_url = base_url + organization_name + '/' + project_name + '/_apis/build/builds?api-version=5.1'
    credentials = BasicAuthentication('', personal_access_token)
    connection = Connection(base_url=base_url + organization_name, creds=credentials)
    params_dict = {"buildNumber":build_id, "definition":{"id":build_id}}
    USERNAME = ''
    USER_PASS = USERNAME + ':' + personal_access_token
    pat_base_64 = base64.b64encode(USER_PASS.encode()).decode()
    head = {'Authorization': 'Basic %s' % pat_base_64, 'Accept': 'application/json'}
    requests.post(fully_url, json=params_dict, headers=head)

def get_certdate():

    credential = DefaultAzureCredential()
    certificate_client = CertificateClient(vault_url=(os.environ.get('kvurl')), credential=credential)
    certificate = certificate_client.get_certificate(certificate_name=(os.environ.get('certname')))
    cert_date = certificate.properties.expires_on.strftime("%d/%m/%Y")
    limit_date = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
    slack_token = os.environ.get('slacktoken')

    if cert_date == limit_date:
        queue_build()
        slack_message('O certificate vai expirar')
    else:
        slack_message('O certificate não vai expirar')

get_certdate()