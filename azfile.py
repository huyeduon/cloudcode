from azure.core.exceptions import (
    ResourceExistsError,
    ResourceNotFoundError
)

from azure.storage.fileshare import (
    ShareServiceClient,
    ShareClient,
    ShareDirectoryClient,
    ShareFileClient
)

import os, uuid, base64

connect_str = "DefaultEndpointsProtocol=https;AccountName=ninjagoinsbu;EndpointSuffix=core.windows.net"

# Create a ShareServiceClient from a connection string
service_client = ShareServiceClient.from_connection_string(connection_string)

def create_file_share(self, connection_string, share_name):
    try:
        # Create a ShareClient from a connection string
        share_client = ShareClient.from_connection_string(
            connection_string, share_name)

        print("Creating share:", share_name)
        share_client.create_share()

    except ResourceExistsError as ex:
        print("ResourceExistsError:", ex.message)
        