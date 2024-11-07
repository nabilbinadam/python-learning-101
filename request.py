

"""
REQUEST>>>>>>PROCESS>>>>RESPONSEE
-request to sign in, dalam json
- hantar dalam Post Request
- Backend terima dalam Json.
- Backend kena decode Json file
- Backend kena Loop Json file cari[info]
- Backend if else check password,email,username in database atau tidak
"""
data = {
"username":"nabil_adam",
"email": "nabil@gmail.com",
"password": "18643"

}


def passwordRequest(request):

    decode_json= list(request.decode())
    db = user.model()
    for data in decode_json:
        if "password"and "email" and "username" in db:
            return json.response(token)
    
    
    