from fastapi import APIRouter,Depends,HTTPException,Path,Query,status,Cookie
from fastapi.responses import JSONResponse,Response
from user.schemas import UserLoginSchema,UserRegisterSchema,UserRefreshTokenSchema
from sqlalchemy.orm import Session
from user.models import UserModel,TokenModel
from core.database import get_db
from typing import List
import secrets
from auth.jwt_auth import generate_refresh_token,generate_access_token,get_authenticated_user,decode_refresh_token

def generate_token(length=32):
    return secrets.token_hex(length // 2)

router = APIRouter(tags=["users"],prefix="/users")

@router.post("/login")
async def user_login(request:UserLoginSchema,db:Session = Depends(get_db)):
    user_obj = db.query(UserModel).filter_by(username = request.username.lower()).first()
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="username or password not valid")
    if not user_obj.verify_password(request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="password is invalid")
  

    access_token = generate_access_token(user_obj.id)
    refresh_token = generate_refresh_token(user_obj.id)
    return JSONResponse(content = {"detail": "Login successful", "access_token":access_token,"refresh_token":refresh_token})

@router.post("/register")
async def user_register(request:UserRegisterSchema,db:Session = Depends(get_db)):
    if db.query(UserModel).filter_by(username = request.username.lower()).first():
        raise HTTPException(status.HTTP_201_CREATED, detail="user already exist")
    user_obj = UserModel(username = request.username.lower())
    print("DEBUG password raw:", repr(request.password), "len:", len(request.password))

    user_obj.set_password(request.password)
    db.add(user_obj)
    db.commit()
    return JSONResponse(content = {"detail": "user registerd suuccessfully"})



@router.post("/refresh_token")
async def user_refresh_token(request:UserRefreshTokenSchema,db:Session = Depends(get_db)):
    user_id = decode_refresh_token(request.token)
    access_token = generate_access_token(user_id)
    return JSONResponse(content= {"access_token":access_token})