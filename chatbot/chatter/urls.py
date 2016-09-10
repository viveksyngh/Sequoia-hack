from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import FacebookBotView

urlpatterns = [
    url(r'^facebook',
        csrf_exempt(FacebookBotView.as_view()), name="chatfacebook"),
]
