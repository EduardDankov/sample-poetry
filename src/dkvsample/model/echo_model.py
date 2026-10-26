'''
Data model for POST /echo endpoint.

Author: Eduard Dankov <contact@dankov.dev>
'''

from pydantic import BaseModel


class EchoModel(BaseModel):
    '''
    Echo data model, contains 2 optional string keys for testing.
    '''
    skey1: str | None = None
    skey2: str | None = None
