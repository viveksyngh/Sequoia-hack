from .models import ChatContext
from workflow import dbapi as db


class ChatterAPI(object):

    def create_context(self, topic, initaited_by, happay_user, referene_id):
        kwargs = {"topic": topic,
                  "initaited_by": initaited_by,
                  "happay_user": happay_user,
                  "referene_id": referene_id}
        return db.create_instance(ChatContext, **kwargs)

    def close_context(self, chat_context):
        return db.update_instance(chat_context, {"is_closed": True})
