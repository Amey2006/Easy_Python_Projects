from passlib.context import CryptContext

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(pw:setattr):
    return pwd_context.hash(pw)

def verify_it(plain:str,hashed:str):
    return pwd_context.verify(plain,hashed)