import json

from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .constants import VERIFY_TOEKN, PAGE_ACCESS_TOKEN
from .bot import BotMessage
import requests
from utils import get_messaging_events
import json
# from .models import ChatContext
# from .conversation import Converse
# from AccessControl.models import SocialUser, HappayUser
# from workflow import dbapi as db
# from TransactionEngine.models import Transaction


class FacebookBotView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FacebookBotView, self).dispatch(request, *args, **kwargs)

    def __iter(self, _payload):
        for entry in _payload['entry']:
            for data in entry['messaging']:
                _keys = data.keys()
                if 'message' in _keys or 'postback' in _keys:
                    yield data
                try:
                    data['optin']['ref']
                    yield data
                except KeyError:
                    pass

    def get(self, request):
        """
        webhook verify endpoint
        """
        _params = request.GET
        verify_token = _params.get('hub.verify_token', '')
        if verify_token != VERIFY_TOEKN:
            return HttpResponse()
        # hub_subscribe = request.GET.get('hub.subscribe')
        hub_challenge = _params.get('hub.challenge', '')
        return HttpResponse(hub_challenge)

    def post(self, request):
        """
        Facebook messenger webhook entry point
        """
        _body = request.body.decode('utf-8')
        payload = json.loads(_body)
        if payload["object"] == "page":
            sender_id, message = get_messaging_events(payload)
            r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                              params={"access_token": PAGE_ACCESS_TOKEN},
                              data=json.dumps({
                                            "recipient": {"id": sender_id},
                                            "message": {"text": message}
                                        }),
                             headers={'Content-type': 'application/json'})
            if r.status_code != requests.codes.ok:
                print r.text
            return HttpResponse()
