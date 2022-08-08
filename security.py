
from models.user import UserModel


def aunthentication(username,password):
    user = UserModel.get_username(username) 
    if user is not None  and user.password == password:
        return user
def identity(payload): 
    user_id=payload['identity']
    return UserModel.get_id(user_id)  