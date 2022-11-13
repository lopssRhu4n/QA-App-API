import json

class db_users:
    def __init__(self):
        self.db = 'db/users.json'
        
    def getDb(self):
        with open(self.db, encoding='UTF-8') as file:
            data = json.load(file)    
        return data
        
    def setDb(self,  updateFile):
        jsonUpdateFile = json.dumps(updateFile)
        print(jsonUpdateFile)
        with open (self.db,'w', encoding='UTF-8') as file :
            file.write(jsonUpdateFile)
        return self.getDb()    
        
        

class db_posts:
    def __init__(self):
        self.db = 'db/posts.json'
        
    def getDb(self):
        with open(self.db, encoding='UTF-8') as file:
            data = json.load(file)    
        return data
        
    def setDb(self,  updateFile):
        jsonUpdateFile = json.dumps(updateFile)
        print(jsonUpdateFile)
        with open (self.db,'w', encoding='UTF-8') as file :
            file.write(jsonUpdateFile)
        return self.getDb()    