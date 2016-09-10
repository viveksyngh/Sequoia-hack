import urllib
import cStringIO
from django.core.files.base import File


def image_file(image_url):
    """
    returns file object
    """
    return cStringIO.StringIO(urllib.urlopen(image_url).read())


def core_file(file_obj, file_name=''):
    """"
    returns core-file object
    """
    return File(file_obj, file_name)

def get_messaging_events(data):
    """Generate tuples of (sender_id, message_text) from the
    provided payload.
    """
    messaging_events = data["entry"][0]["messaging"]
    for event in messaging_events:
        if "message" in event and "text" in event["message"]:
            return event["sender"]["id"], event["message"]["text"]
