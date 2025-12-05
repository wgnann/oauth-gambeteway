from oauth2_provider.oauth2_validators import OAuth2Validator

class CustomOAuth2Validator(OAuth2Validator):
    oidc_claim_scope = None

    def get_additional_claims(self, request):
        return {
            'name': request.user.name,
            'email': request.user.main_email,
        }
