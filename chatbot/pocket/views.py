from django.shortcuts import render
import requests
from requests import POCKET_CONSUMER_KEY

# Create your views here.

class StartAuth(View):

    def dispatch(self, request, *args, **kwargs):
        return super(StartAuth, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        redirect_uri = "https://" + request.META["HTTP_HOST"] + "/pocketauthcode"
        res = request.post("https://getpocket.com/v3/oauth/request", 
                           data=json.dumps({
                                    "redirect_uri" : redirect_uri,
                                    "consumer_key" : POCKET_CONSUMER_KEY
                            }),
                            headers={'Content-type': 'application/json'})
        
