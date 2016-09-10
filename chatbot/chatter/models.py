from __future__ import unicode_literals

from django.db import models
#from AccessControl.models import HappayUser


# class ChatContext(models.Model):
#     BOT = 0
#     USER = 1
#     INITIATOR = ((BOT, "bot"), (USER, "user"),)

#     topic = models.CharField(max_length=100)
#     initaited_by = models.IntegerField(choices=INITIATOR)
#     is_closed = models.BooleanField(default=False)
#     happay_user = models.ForeignKey(HappayUser, related_name="chatcontext")
#     created_on = models.DateTimeField(auto_now_add=True, db_index=True)
#     updated_on = models.DateTimeField(auto_now=True, db_index=True)
#     referene_id = models.CharField(max_length=250)

#     def __unicode__(self):
#         return "{0}-{1}".format(self.topic, self.get_initaited_by_display())
