from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import FacebookBotView, UberInitiatedMessage

urlpatterns = [
    url(r'^facebook',
        csrf_exempt(FacebookBotView.as_view()), name="chatfacebook"),
     url(r'^uberridecallback',
        csrf_exempt(UberInitiatedMessage.as_view()), name="uberridecallback"),

]
