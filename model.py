import json

class database:
    def __init__(self, path):
        self.db = path   
        
    def getData(self):
        with open(self.db, encoding='UTF-8') as file:
            data = json.load(file)    
        return data
        
    def setData(self,  updateFile):
        jsonUpdateFile = json.dumps(updateFile)
        print(jsonUpdateFile)
        with open (self.db,'w', encoding='UTF-8') as file :
            file.write(jsonUpdateFile)
        return self.getData()    
    
    def getItemByID(self, id):
        for item in self.getData():
            if item.get('id') == id:
                return item
    
    
    def enumerateItem(self, id):
        for  index, item in enumerate(self.getData()):
            if item.get('id') == id:
                return index
            
    def checksIfUserExists(self, new_user):
        for user in self.getData():
            if new_user.get("username") == user.get("username"):
                return {"msg": "Username already used", "status": "error"} 
            elif new_user.get("email") == user.get("email"):
                return {"msg": "Email already used", "status": "error"}
            else:
                return False

    def createNewItem(self, new_item):
        if self.checksIfUserExists(new_item) == False: 
            users = self.getData()
            users.append(new_item)
            return  self.setData(users)
        else:
            return self.checksIfUserExists(new_item)
    
    def createNewPost(self, new_post):
        posts = self.getData()
        posts.append(new_post)
        return self.setData(posts)
                
    def DeleteItem(self, id):
        index = self.enumerateItem(id)
        users = self.getData()
        del users[index]
        modified_users = self.setData(users)
        
        return modified_users

        
    def editItem(self, new_item, id):
        index = self.enumerateItem(id)
        data = self.getData()
        data[index].update(new_item)
        self.setData(data)
        return data[index]


    def getPostsByAuthor(self, author):
        matched = []
        for post in self.getData():
            if post.get('author') == author:
                matched.append(post)    
            
        return matched
    

        
    
class authentication:
    def __init__(self):
        return
    
    def validateLogin(self, credentials, db):
        for user in db:
            if (user.get('email') == credentials['email']) & (user.get('password') == credentials['password']):
                return {"token": user.get('jwt'), "user": user.get('username')}
            else:
                return {"msg": "User don't exist", "status": "error"}
 