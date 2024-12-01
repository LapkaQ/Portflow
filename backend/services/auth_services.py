from authlib.integrations.starlette_client import OAuth

oauth = OAuth()

def configure_oauth():
    oauth.register(
        name='google',
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_id='your-google-client-id',
        client_secret='your-google-client-secret',
        client_kwargs={
            'scope': 'email openid profile',
            'redirect_url': 'your-redirect-url'
        }
    )
