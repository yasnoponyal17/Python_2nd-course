from controllers.databaseController import DatabaseController

class UserController:
    def __init__(self, db: DatabaseController):
        self.db = db

    def list_users(self):
        return self.db._read_users()
    
    def get_user_currencies(self, user_id):
        return self.db._read_user_currencies(user_id)
    
    def get_user(self, user_id):
        return self.db._get_user(user_id)