# technical_test

Use below credentials

https://secure-plains-79901.herokuapp.com/my-pets/
username : admin
password : qwerty123456


# USER SIGNUP
url : http://localhost:8000/signup/
Endpoints : /signup/
Method : POST
Parameter : { email="", password="", username="" }

"response": [
    "message": "Successfully Created Your Account.",
    "success": "true",
    "status": 201
   ]
}


# USER LOGIN
url : http://localhost:8000/login/
Endpoints : /login/
Method : POST
Parameter : { email="", password="", }

"response": {
    "message": "Successfully login",
    "status": 200
}


# USER LOGOUT
url : http://localhost:8000/user/logout/
Endpoints : /logout/
Method : POST
header : { 'token': "" }
Parameter : { 'token':  }
response : {
    "message": "Successfully logout",
    "status": 200
}


# CREATE PET DETAIL 
url : http://localhost:8000/pets/
Endpoints : /pets/
Method : POST
header : {'Authorization': 'Token  '}
Parameter : {'pet_type': '', 'name': '', 'birthday': '' }
response : {
    "message": "Successfully logout",
    "status": 200
}

"""
NOTE: Pass parameters in following ways - 
For 'pet_type' type as follows: for Dog type 'D' and for Cat type 'C'
For 'birthday' type date in this format [YYYY-MM-DD]    
For name type text character with numbers.
"""

# GET PET DETAIL 
url : http://localhost:8000/pets/
Endpoints : /pets/
Method : GET
header : {'Authorization': 'Token  '}
Parameter : { }
response : [{
    "id": "",
    "owner": "",
    "name": "",
    "pet_type": "",
    "birthday": "", 
}]


# GET PET DETAIL BY ID 
url : http://localhost:8000/pets/(pet.id)/
Endpoints : /pets/(pet.id)/
Method : GET
header : {'Authorization': 'Token  '}
Parameter : { }
response: {
    "id": "",
    "owner": "",
    "name": "",
    "pet_type": "",
    "birthday": "", 
}


# UPDATE PET DETAIL 
url : http://localhost:8000/pets/(pet.id)/
Endpoints : /pets/(pet.id)/
Method : PUT
header : {'Authorization': 'Token  '}
Parameter : {'pet_type': '', 'name': '', 'birthday': '' }
response: {
    "id": "",
    "owner": "",
    "name": "",
    "pet_type": "",
    "birthday": "", 
}

"""
NOTE: 
1. Enter data in the field which you want.
2. Pass parameters in following ways - 
For 'pet_type' type as follows: for Dog type 'D' and for Cat type 'C'
For 'birthday' type date in this format [YYYY-MM-DD]    
For name type text character with numbers.
"""

# DELETE PET DETAIL 
url : http://localhost:8000/pets/(pet.id)/
Endpoints : /pets/(pet.id)/
Method : PUT
header : {'Authorization': 'Token  '}
Parameter : {'pet_type': '', 'name': '', 'birthday': '' }
response: {
    "id": "",
    "owner": "",
    "name": "",
    "pet_type": "",
    "birthday": "", 
}

"""
NOTE: 
1. Enter data in field which you want to update.
2. Pass parameters in following ways - 
For 'pet_type' type as follows: for Dog type 'D' and for Cat type 'C'
For 'birthday' type date in this format [YYYY-MM-DD]    
For name type text character with numbers.
"""
