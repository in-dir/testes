from datetime import datetime, timedelta
from typing import Optional

import json
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from passlib.context import CryptContext

from pydantic import BaseModel

with open("data.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()

@app.get('/profile')
async def read_profile():
    for data_diri in data['data']:
        return data_diri

@app.get('/profile/wishlist')
async def read_wishlist():
    for data_katalog in data['katalog']:
        return data_katalog
