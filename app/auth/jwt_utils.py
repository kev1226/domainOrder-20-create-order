from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv()


def decode_token(token: str):
    secret = os.getenv("SECRET_KEY")
    try:
        return jwt.decode(token, secret, algorithms=["HS256"])
    except Exception as e:
        print("❌ JWT Decode Error:", e)
        return None
