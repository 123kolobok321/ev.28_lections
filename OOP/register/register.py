import json
import hashlib
import os


DIR_PATH = os.getcwd()
FILE_PATH = DIR_PATH + '/users.json'

class RegisterMixin:
    '''Миксин для регистрации'''
    def _hash_password(self, password, salt=None):
        if not salt:
            salt = os.urandom(32)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
        return hashed_password
    
    def _validate_password(self, password, password2):
        if len(password) < 8:
            raise ValueError('Password is too short! Must be at list 8 symbols!')
        elif password.isdigit() or password.isalpha():
            raise ValueError('Password must be contain digits and characters!')
        elif password != password2:
            raise ValueError('Password didn\'t match!')
        
    def register(self, username, first_name, last_name, password, password2):
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
            try:
                id = data[-1]['id'] + 1
            except (IndexError, ValueError):
                data = []
                id = 1
            is_username_used = any([x['username'] == username for x in data])

        self._validate_password(password, password2)
        salt = os.urandom(32)
        hashed_password = {'password': self._hash_password(password, salt), 'salt':salt}

        with open(FILE_PATH, 'w') as file:
            if is_username_used:
                json.dump(data, file)
                raise ValueError('Username is already taken!')

            user = {'id': id, 'username': username, 'first_name': first_name, 'last_name': last_name, 'password': password}
            data.append(user)
            json.dump(data, file, indent=4)
            return {'status': 201, 'msg': 'Successfully registered'}

class LoginMixin:
    '''Миксин для логина'''
    def login(self, username, password):
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
            try:
                user = list(filter(lambda x: x['username'] == username, data))[0]
            except IndexError:
                raise ValueError('Invalid password or username!')
            
            if password != user['password']:
                raise ValueError('Invalid password or username!')
            
        return {'status': 200, 'msg': 'Successfully logged in!', 'user': user['username']}

obj = RegisterMixin()
obj.register('JohnSnow29', 'John', 'Snow', 'bastard124', 'bastard124')

# obj = LoginMixin()
# print(obj.login('JohnSnow26', '1'))

            
            





