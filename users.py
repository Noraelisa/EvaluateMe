from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username,password,admin):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password,admin) VALUES (:username,:password,:admin)"
        db.session.execute(sql, {"username":username,"password":hash_value,"admin":admin})
        db.session.commit()
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id",0)

def is_admin():
    sql = "SELECT admin FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":session.get("user_id")})
    admin = result.fetchone()
    if admin == None:
        return False
    else:
        if admin[0] == True:
            return True
        else:
            return False   
  