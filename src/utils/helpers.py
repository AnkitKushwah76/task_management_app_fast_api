from fastapi import Request, HTTPException,status, Depends
from src.utils.db import get_db
from src.utils.settings import settings
from sqlalchemy.orm import Session
from jwt.exceptions import InvalidTokenError
from src.user.models import UserModel
import jwt

def is_authenticated(request: Request, db:Session = Depends(get_db)):
    try:
      token = request.headers.get("authorization")
      if not token:
          raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)
      token = token.split(" ")[-1]
      data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
      user_id = data.get("_id")
      # exp_time = data.get("exp")
      # current_time = datetime.now/().timestamp()

      # if current_time > exp_time:
          # raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)
      user = db.query(UserModel).filter(UserModel.id == user_id).first()
      if not user :
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)
      return user
    except InvalidTokenError:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)