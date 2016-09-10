from .constants import (
    SENDER_ID, PAGE_ACCESS_TOKEN)
from messengerbot import (
    MessengerClient, messages, attachments,
    templates, elements)


class BotButton:

    @classmethod
    def postback_button(self, title, payload):
        """
        creates post

        :text: display text
        : payload: postback payload
        """
        return elements.PostbackButton(title=title, payload=payload)

    @classmethod
    def button_template(self, text, postbacks_buttons):
        """
        creates button templates

        :text: display text for button
        :postbacks_buttons: list of buttons
        """
        return templates.ButtonTemplate(
            text=text,
            buttons=postbacks_buttons)


class BotMessage:

    TEXT = "text"
    ATTACHMENTS = "attachments"
    POSTBACK = "postback"
    PAYLOAD = "payload"

    def __init__(self, *args, **kwargs):
        self.messenger = MessengerClient(access_token=PAGE_ACCESS_TOKEN)
        self.recipient = messages.Recipient(recipient_id=SENDER_ID)

    def __parse(self, dic, m_type=True):
        _keys = dic.keys()

        if self.TEXT in _keys:
            if m_type:
                return self.TEXT
            return dic[self.TEXT]

        elif self.ATTACHMENTS in _keys:
            _attachments = dic[self.ATTACHMENTS][0]
            if m_type:
                return _attachments['type']
            # attahcments can be multiple
            return _attachments['payload']['url']
        elif self.PAYLOAD in _keys:
            if m_type:
                return self.PAYLOAD
            return dic[self.PAYLOAD]
        return ""

    def __send(self, message):
        """
        :message: Message object
        """
        request = messages.MessageRequest(self.recipient, message)
        self.messenger.send(request)

    def set_message_attributes(self, post_data):
        """
        Set message attributes on self
        """
        _message = post_data.get('message')
        if not _message:
            _message = post_data.get('postback', {})
        self.id = _message.get('mid', 0)
        self.sequence = _message.get('seq', 0)
        self.type = self.__parse(_message, True)
        self.content = self.__parse(_message, False)
        self.recipient_id = post_data['recipient']['id']
        self.sender_id = post_data['sender']['id']
        self.timestamp = post_data['timestamp']

    def send_text(self, text):
        """
        send text to page
        """
        message = messages.Message(text=text)
        self.__send(message)

    def send_options(self, **kwargs):
        """
        send options to page
        """
        display = kwargs.get('display', '')
        _no_dic = kwargs.get("no", {})
        _yes_dic = kwargs.get("yes", {})

        def button(dic):
            display = dic.get('display', '')
            payload = dic.get('payload', '')
            return BotButton.postback_button(display, payload)

        buttons = map(button, [_no_dic, _yes_dic])

        template = BotButton.button_template(display, buttons)
        attachment = attachments.TemplateAttachment(template=template)
        message = messages.Message(attachment=attachment)
        self.__send(message)
