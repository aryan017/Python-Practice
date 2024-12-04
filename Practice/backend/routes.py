from app import app,db
from flask import request,jsonify
from models import Friend

# Get All Friends
@app.route("/api/friends", methods=["GET"])
def get_friends():
    try :
        friends = Friend.query.all()  # Fetch all Friend objects from the database
        result = [friend.to_JSON() for friend in friends]  # Convert each to JSON
        return jsonify(result)  # Return the result as JSON
    except Exception as e :
        return jsonify({"error" : str(e)})


# Create Friend
@app.route("/api/friends",methods=["POST"])
def create_Friend() :
    
    try :
        data=request.json()
        name=data.get("name")
        role=data.get("role")
        description=data.get("description")
        gender=data.get("gender")
        
        # Add image Avatar for the Current Friend 
        if gender=="male":
            img_urL=f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender=="female":
            img_urL=f"https://avatar.iran.liara.run/public/girl?username={name}"
        else:
            img_urL=None
    
        new_Friend=Friend(name=name,role=role,description=description,gender=gender,img_urL=img_urL)
    
        db.session.add(new_Friend)
        db.session.commit()
    
        return jsonify({"msg : Friend Created SuccessFully"}),201
    
    except Exception as e : 

        db.session.rollback()
        
        return jsonify({"msg" :  str(e)}),500
    
    