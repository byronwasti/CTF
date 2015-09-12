from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

import xml.etree.ElementTree as ET

def checkSignature(msg, sig):
    h = SHA.new(msg.encode('utf-8'))

    verifier = PKCS1_v1_5.new(key)

    return verifier.verify(h, sig)

tree = ET.parse('email.xml')
root = tree.getroot()

# yay for globals
for name in range(1,6):
    key = RSA.importKey(open('{}.pem'.format(name)).read())
    print("checking a key...")

    for mail in root:
        sender = mail[0].text
        topic = mail[1].text
        msg = mail[2].text
        sig = mail[3].text
        if checkSignature(msg, sig):
            print(msg)
