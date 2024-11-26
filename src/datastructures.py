
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)


    # DISPLAY ALL MEMBERS
    def get_all_members(self):
        return self._members


    # DISPLAY - Single Member
    def get_member(self, id):
        # loop through each dict in self._members and find a particular Jackson by id number (for...in loop)
        for member in self._members:
            # if the id is found, return the member
            if member["id"] == id:
                print("Member found!")
                print(member)
                return member

    # ADD - Single Member
    def add_member(self, member):
        member["id"] = self._generateId()
        member["name"] = (member["first_name"]) + " " + (self.last_name)
        self._members.append(member)

    # DELETE - Single Member
    def delete_member(self, id):
        # loop through each dict in self._members and find a particular Jackson by id number (for...in loop)
        for member in self._members:
            # if the id is found, delete the member
            if member["id"] == id:
                del self._members["id"]
            return None