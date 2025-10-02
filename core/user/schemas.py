
from pydantic import BaseModel, Field, model_validator


class UserLoginSchema(BaseModel):
    username: str = Field(..., max_length=250, description="username of the user")
    password: str = Field(..., max_length=250, description="password of the user")


class UserRegisterSchema(BaseModel):
    username: str = Field(..., max_length=250, description="username of the user")
    password: str = Field(..., description="password of the user")
    password_confirm: str = Field(..., description="confirm password of the user")

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match")
        return self


class UserRefreshTokenSchema(BaseModel):
    token: str = Field(..., description="refresh token of the user")
