VERIFY_TOEKN = "hackbot"

PAGE_ACCESS_TOKEN = "EAAEtiAMUiHkBALaPIVMKBQHsbAIpdnbfucXlZB8AdADdV05T3Y8cfX6IZCjofrg5ZBMWqZBOUfuJPHWWMqNsix7LSTMotfy2FPCGQLxCHa8MFFtnxh7fGZBIhlppfQNWpZCkHXx0FszCTr85ChxNFPv7EKqjYHZBarRH2Mxsb7VJQZDZD"

RECIPIENT_ID = 1271454969556110
SENDER_ID = 1271454969556110

POST_TEXT_URL = "https://graph.facebook.com/v2.6/me/messages?access_token={0}"

attach_bill = "You have new transaction. Would you like to add bill ?"


PAYLOAD = {"attach_bill_yes": "Please upload bill image",
           "attach_bill_no": "Ok. you can do next time."}

TRANS_ACTION = {"display": attach_bill,
                "no": {"display": "No",
                       "payload": "attach_bill_no",
                       "reply": "You can do next time."},
                "yes": {"display": "Yes",
                        "payload": "attach_bill_yes",
                        "reply": "Please upload bill image."}}
