"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

John = {
    "first_name": "John",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}

Jane = {
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
}

Jimmy = {
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
}

# Function Call To Add Hard-Coded Family Members
jackson_family.add_member(John)
jackson_family.add_member(Jane)
jackson_family.add_member(Jimmy)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# GET ALL MEMBERS
@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    
    return jsonify(members), 200


# GET - single member
@app.route('/member/<int:id>', methods=['GET'])
def get_single_member(id):
    # call the get_member() method
    member = jackson_family.get_member(id)
    
    # check to see if a member was found or None
    if member == None:
        return {}  # jsonify(f'Member {id} not found!'), 404
    
    return member, 200

# ADD - single member
@app.route('/member', methods=['POST'])
def add_single_member():
    member = request.json
    print(f'{member} added!')
    jackson_family.add_member(member)
    if member != None:
        return "Sucessfully added", 200

# DELETE - single member
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_single_member(id):
    # retrieve the member using the get_member(id) method in family structure
    member = jackson_family.get_member(id)
    # check to see if a member was found or None
    if member != None:
        # use the delete_member(id) method in family structure 
        jackson_family.delete_member(id)
        # return a jsonified message stating that the member was successfully removed (200)
        return jsonify({
            "message": "Successfully deleted",
            "done": True
        }), 200
    
    else:
       return jsonify({
            "message": "Member not found",
            "done": False
        }), 404
    
    
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
