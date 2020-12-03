from azure.storage.queue import (
    QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

import os, uuid, base64

def base64ToString(a_base64_string):
    return base64.b64decode(a_base64_string).decode('ascii')

processing_queue_name = "processing-queue"
connect_str = "DefaultEndpointsProtocol=https;AccountName=ninjagoinsbu;EndpointSuffix=core.windows.net"

# Authentication libraryy
from azure.identity import ClientSecretCredential


# Info for authenticationg
# Display name : huyeduon-restapi
# Application (client) ID : c4f505e2-b31b-42ad-8294-11991044cece
# Directory (tenant) ID : e34b6079-b8db-43a4-8104-4768856bd06c
# Object ID : 52a4d658-867e-41fa-947d-2f51befd0f2d


tenant_id ="e34b6079-b8db-43a4-8104-4768856bd06c"
client_id="c4f505e2-b31b-42ad-8294-11991044cece"
client_secret="E9LpKrW-rqF7bRE3-2aMSML4Hq~-k.R.rw"

# Get the application credentials
app_credentials = ClientSecretCredential(tenant_id, client_id, client_secret)

# Create a queue client
queue_client = QueueClient.from_connection_string(connect_str, processing_queue_name, credential=app_credentials)

# Setup Base64 encoding and decoding functions

queue_client.message_encode_policy = BinaryBase64EncodePolicy()
queue_client.message_decode_policy = BinaryBase64DecodePolicy()

print("Client connected to Queue")

print("Peek messages in the queue...")

messages = queue_client.peek_messages(max_messages=5)
for peeked_message in messages:
    print("Message: ", base64ToString(peeked_message.content))