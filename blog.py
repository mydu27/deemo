from flask import Flask,render_template
from pymongo import MongoClient
from config import MongoDB

app = Flask(__name__)
mongo = MongoClient()

@app.route('/')
def index():
    onlines_users = mongo.db.system.users.find()
    return render_template('index.html',onlines_usersonlines_users=onlines_users)
#增
@app.route('/add/')
def add():
    user = mongo.db.users
    user.insert({"username":"geekpark","password":"123456"})
    if user:
        return "用户已存在!"
    else:
        return "Added User!"

#查
@app.route('/find/<username>')
def find(username):
    user = mongo.db.users
    username = user.find_one({"username":username})
    if username:
        return "你查找的用户:" + username["username"] + "密码是:" + username["password"]
    else:
        return "你查找的用户不存在!"

#改
@app.route('/update/<username>')
def update(username):
    user = mongo.db.users
    passwd = "abcd1234"
    username = user.find_one({"username":username})
    username["password"] = passwd
    user.save(username)
    return "update OK" + username["username"]

#删
@app.route('/delete/<username>')
def delete(username):
    user = mongo.db.users
    username = user.find_one({"username": username})
    user.remove(username)
    if username:
        return "Remove" + username["username"] + "ok!"
    else:
        return "用户不存在，请核对后再操作"

if __name__ == '__main__':
    app.run(debug=True)