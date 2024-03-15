class UsersServices:
    def __init__(self,UserID,UserName,firstname,lastname,Password):
        self.UserID=UserID
        self.UserName = UserName
        self.firstname = firstname
        self.lastname = lastname
        self.Password = Password
    
    # #Method to create a new user  
    # @staticmethod 
    # def CreateNewUser(user_info):
    #     return UsersServices(**user_info)
        
    # #Method for login validation
    # def LoginValidation(self):
    #     if not self.UserName.isalnum():
    #         print('Username can only contain letters and numbers')
    #     elif len(self.Password) < 8:
    #         print('Password must be at least  6 characters long')
    #     else:
    #         return True