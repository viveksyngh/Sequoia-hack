from TransactionEngine.models import Transaction
from .constants import TRANS_ACTION
from .bot import BotMessage
from .api import ChatterAPI


def messenger_attach_bill(transaction):
    """
    Ping bot for new transaction not having bill attached to it
    """
    # create context
    topic = "new_transaction_attach_bill"
    api = ChatterAPI()
    api.create_context(topic, 0 , transaction.user, transaction.txn_id)
    # ping messenger
    bot = BotMessage()
    bot.send_options(**TRANS_ACTION)
    print "messenger: ", transaction.txn_id
