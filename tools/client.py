from requests_oauthlib import OAuth2Session
import os

# https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html

client_id = 'Yzk8KdACpNT1df6YjcLF1O4yzTrpt3tfu5a7krdI'
client_secret = '1LwJhElM3KA01SJ2g4cWqv5A92lJdlf0cZXA2l4aaeeL9sOcIuIWJLwYPuXB6PR6eu8ELAXEaWRsBM3sfWahqH1pY8V1kEcwafKNkiMaCsNOfid2ci3c7GqOJPLPtakV'
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'

base = 'http://127.0.0.1:8000'
oauth = OAuth2Session(client_id)
auth_url, state = oauth.authorization_url(base+'/o/authorize/')
print(auth_url)
auth_resp = input('response: ')
token = oauth.fetch_token(base+'/o/token/', authorization_response=auth_resp, client_secret=client_secret)
resp = oauth.get(base+'/o/userinfo')
print(resp.text)
