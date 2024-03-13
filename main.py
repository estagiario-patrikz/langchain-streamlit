from langchain_community.document_loaders import TextLoader
from langchain.document_loaders import googledriveLoader
from langchain_community.document_loaders import GoogleDriveLoader

import os

loader = googledriveLoader (
    document_id = ['1XBm3gA4PX1OApPVkTVahHgNX3-U17IQFnn-9WhrNjrs'],
    credentials_path = ('/credentials.json')
)

docs = loader.load()