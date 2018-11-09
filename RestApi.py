import requests
#https://reqres.in/api/
class REST:
    def __init__(self):
        pass
    
    def getUsersAPI(self):
        r=requests.get("https://reqres.in/api/users")
        jsonObj = r.json()
        noOfUsers = len(jsonObj['data'])
        statusCode = r.status_code
        print(jsonObj)
        print("statusCode :- "+str(statusCode))
        print("noOfUsers :- "+str(noOfUsers))
    
    def getSingleUserAPI(self,id):
        r=requests.get("https://reqres.in/api/users/"+str(id))
        jsonObj = r.json()
        statusCode = r.status_code
        print(jsonObj)
        print("statusCode :- "+str(statusCode))
    
    def getResourcesAPI(self):
        r=requests.get("https://reqres.in/api/unknown")
        jsonObj = r.json()
        noOfResources = len(jsonObj['data'])
        statusCode = r.status_code
        print(jsonObj)
        print("statusCode :- "+str(statusCode))
        print("noOfResources :- "+str(noOfResources))
    
    def getSingleResourceAPI(self,id):
        r=requests.get("https://reqres.in/api/unknown/"+str(id))
        jsonObj = r.json()
        statusCode = r.status_code
        print(jsonObj)
        print("statusCode :- "+str(statusCode))
        
    def postUserAPI(self,data):
        r=requests.post("https://reqres.in/api/users",data)
        jsonObj = r.json()
        statusCode = r.status_code
        print(jsonObj)
        print("statusCode :- "+str(statusCode))
        
    def putUserAPI(self,data):
        r=requests.put("https://reqres.in/api/users",data)
        jsonObj = r.json()
        statusCode = r.status_code
        print(jsonObj)
        print("statusCode :- "+str(statusCode))
    
    def patchUserAPI(self,data):
        r=requests.patch("https://reqres.in/api/users",data)
        jsonObj = r.json()
        statusCode = r.status_code
        print(jsonObj)
        print("statusCode :- "+str(statusCode))
                
    def deleteUserAPI(self,id):
        r=requests.delete("https://reqres.in/api/users/"+str(id))
        statusCode = r.status_code
        print("statusCode :- "+str(statusCode))
    
    def registerUserAPI(self,data):
        r=requests.post("https://reqres.in/api/register",data)
        jsonObj = r.json()
        statusCode = r.status_code
        print(jsonObj)
        print("statusCode :- "+str(statusCode))   
    
    def loginUserAPI(self,data):
        r=requests.post("https://reqres.in/api/login",data)
        jsonObj = r.json()
        statusCode = r.status_code
        print(jsonObj)
        print("statusCode :- "+str(statusCode)) 
                 
def main():
    print('='*30)
    r=REST()
    r.getUsersAPI()
    print('='*30)
    r.getSingleUserAPI(3)
    r.getSingleUserAPI(13)
    print('='*30)
    r.getResourcesAPI()
    print('='*30)
    r.getSingleResourceAPI(10)
    r.getSingleResourceAPI(100)
    data={"name": "morpheus","job": "leader"}
    r.postUserAPI(data)
    data={"name": "morpheus","job": "Manager"}
    r.putUserAPI(data)   
    data={"name": "morpheus","job": "Manager"}
    r.patchUserAPI(data)   
    r.deleteUserAPI(2)
    data={"name": "morpheus","job": "Manager"}
    r.registerUserAPI(data)
    data={"email": "sydney@fife","password": "pistol"}
    r.registerUserAPI(data)
    data={"email": "sydney@fife"}
    r.registerUserAPI(data)
    data={"name": "morpheus","job": "Manager"}    
    r.loginUserAPI(data)
    data={"email": "sydney@fife","password": "pistol"}
    r.loginUserAPI(data)
    data={"email": "sydney@fife"}
    r.loginUserAPI(data)
    
if __name__=='__main__':
    main()