import requests

import time
import calendar

import hmac
import hashlib


# fill request body
# master encryption key is given by Tipalti
def complete_return_request(payeeID, payerName, invoiceRefCode, master_encryption_key):
    url = "https://api.sandbox.tipalti.com/V9/PayeeFunctions.asmx"
    key = encyption_key(payeeID, payerName, master_encryption_key)
    timestamp = calendar.timegm(time.gmtime())

    body = """
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
            <CancelInvoice xmlns="http://Tipalti.org/">
              <payerName> %s </payerName>
              <timestamp> %d </timestamp>
              <key> %s </key>
              <invoiceRefCode> %s </invoiceRefCode>
            </CancelInvoice>
          </soap:Body>
        </soap:Envelope>""" % (payerName, timestamp, key, invoiceRefCode)

    headers = {'SOAPAction': 'http://Tipalti.org/CancelInvoice', 'Content-Type': 'text/xml'}
    response = requests.post(url, data=body, headers=headers)

    return response


# key encryption
def encyption_key(payee_id, payer_name, master_encryption_key):

    utc_timestamp = str(int(time.time()))  # https://www.epochconverter.com/
    EAT = ""

    plain_text_key = payer_name + str(payee_id) + utc_timestamp + EAT
    encrypted_utf_key = plain_text_key.encode()
    final_encryption = hmac. \
        new(master_encryption_key.encode(), msg=encrypted_utf_key, digestmod=hashlib.sha256).digest()
    # print(str(final_encryption))
    return final_encryption
