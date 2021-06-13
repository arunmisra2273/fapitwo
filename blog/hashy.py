from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hashy():
    def bashy(password: str):
        return password_context.hash(password)
