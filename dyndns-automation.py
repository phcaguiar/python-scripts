import os
#certbotcommand = 'certbot certonly -d $CERTBOT_ZONE --manual --preferred-challenges dns --dry-run -m pedro.aguiar@stone.com.br --manual-public-ip-logging-ok'
#certbotcommand = 'certbot certonly --manual --manual-auth-hook /root/python-scripts/dyndns-auth.py --manual-cleanup-hook /root/python-scripts/dyndns-cleanup.py -d $CERTBOT_ZONE --dry-run -m pedro.aguiar@stone.com.br -manual-public-ip-logging-ok'
certbotcommand = 'certbot certonly --manual --manual-auth-hook /root/python-scripts/dyndns-auth.py -d $CERTBOT_ZONE --dry-run -m pedro.aguiar@stone.com.br --manual-public-ip-logging-ok'
#certbotcommand = 'ls -l'
os.system(certbotcommand)