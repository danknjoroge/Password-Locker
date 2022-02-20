#!/usr/bin/env python3.9



from user import User
from credentials import Credentials

def create_users(name, passw):
    newUser = User(name, passw)
    return newUser

def save_users(user):
    user.save_user()

def existing_user_check(name):
    return User.user_exist(name)

def login_user(name, password):
    login= User.login(name, password)
    if login != False:
        return User.login(name, password)

def display_users():
    return User.display_user()

def delete_user(user):
    return user.delete_user()

def create_credentials(accountName,accountUsername,accountPassword):
    newCredential = Credentials(accountName,accountUsername,accountPassword)
    return newCredential

def save_credentials(credentials):
    credentials.save_credential()

def delete_credentials(credentials):
    credentials.delete_credentials()

def display_credentials():
    return Credentials.display_credentials()

