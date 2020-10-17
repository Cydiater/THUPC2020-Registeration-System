import jwt
import time

from RegSystem.settings import SECRET_KEY

headers = {
    'alg': "HS256",  
}

def generate(username):
    token_dict = {
        'username' : username,
        'iat' : time.time(),
    }

    jwt_token = jwt.encode(token_dict, 
                        SECRET_KEY, 
                        algorithm="HS256", 
                        headers=headers, 
                        ).decode('ascii')  

    return jwt_token

def verify(jwt_token):
    print("草：", jwt_token)

    try:
        data = jwt.decode(jwt_token, SECRET_KEY, algorithms='HS256')
        return True
    except :
        return False
