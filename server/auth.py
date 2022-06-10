import os
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette import status


X_API_KEY = APIKeyHeader(name="X-API-KEY")


def check_api_key(api_key: str = Depends(X_API_KEY)):
    if api_key == os.getenv('API_KEY'):
        return api_key

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid API Key',
    )
