from app import app, db
from flask import request, jsonify
from app.models import User

@app.route('/api/users',methods=['POST'])
def create_user():
    data = request.json
    if not data:
        return jsonify({'error':'Missing Data'}), 400
    
    required_fields = ['username','email','password']
    for field in required_fields:
        if field not in data:
            return jsonify({'error':'Missing Data'}), 400
        
    user = User(username=data['username'],email=data['email'],password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id':user.id,'username':user.username,'email':user.email})

@app.route('/api/users',methods=['GET'])
def get_all_users():
    users = User.query.all()

    # return jsonify([{'id':user.id,'username':user.username,'email':user.email} for user in users])
    output = []
    for user in users:
        output.append({'id':user.id,'username':user.username,'email':user.email})
    return jsonify(output)


