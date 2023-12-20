# myapp/middleware.py
from django.utils.translation import activate

class ForceDefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # activate('fr')  # Set your default language code here
        response = self.get_response(request)
        return response
