from sqlalchemy import Column,Integer,String,DateTime,Boolean,Text,func,ForeignKey, Enum as SQLEnum
from core.database import Base
from passlib.context import CryptContext
from enum import Enum
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserType(str, Enum):
    ADMIN = "admin"
    USER = "user"

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(250),nullable=False)
    password = Column(String,nullable=True)
    is_active = Column(Boolean,default=True)
    create_date = Column(DateTime,server_default=func.now())
    update_date = Column(DateTime, server_default=func.now(),server_onupdate=func.now())
    
       
    def hash_password(self, plain_password: str) -> str:
        """Hashes the given password using bcrypt."""
        return pwd_context.hash(plain_password)

    def verify_password(self, plain_password: str) -> bool:
        """Verifies the given password against the stored hash."""
        return pwd_context.verify(plain_password, self.password)

    def set_password(self,plain_text: str) -> None:
        self.password = self.hash_password(plain_text)

class TokenModel(Base):
    __tablename__ = "tokens"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    token = Column(String, nullable=False, unique=True)
    create_date = Column(DateTime,server_default=func.now())


   
    