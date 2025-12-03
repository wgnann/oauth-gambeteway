from requests_oauthlib import OAuth2Session
import os

# https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html

client_id = 'Yr6286ShBNbVeILJZygYYogZICbYXpamH9H4sSN8'
client_secret = 'kQu21cFMid3Z05gMUotwWuFn4HD7nx35yTPkEyxyk3pdSCWEmKKJRjSVLUzJ3N4QCT3AisKggaLtb083rRN56Wl8ukOzCYRfFP1EcgxJkGztrxKGMGBwajc3xK798c2K'
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'

base = 'http://oauth2.ime.usp.br:8080'
oauth = OAuth2Session(client_id)
auth_url, state = oauth.authorization_url(base+'/o/authorize/')
print(auth_url)
auth_resp = input('response: ')
token = oauth.fetch_token(base+'/o/token/', authorization_response=auth_resp, client_secret=client_secret)
print(token)
