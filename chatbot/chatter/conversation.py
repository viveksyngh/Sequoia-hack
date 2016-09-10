

class Converse:

    def bot_reply(self, bot_message):
        from .constants import PAYLOAD
        try:
            _text = PAYLOAD[bot_message.content]
            bot_message.send_text(_text)
        except KeyError:
            return "i'm bot"
