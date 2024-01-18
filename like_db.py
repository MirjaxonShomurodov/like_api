import json
import tinydb
from tinydb import TinyDB, Query
from tinydb.table import Document

class LikeDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = TinyDB(db_path, indent=4)
        self.users = self.db.table('users')
        self.images = self.db.table('images')
        self.table = self.db.table('api')




    def add_image(self,image_id:str, message_id:str,url:str):
        """Adds an image to the database
        args:
            image_id: The id of the image
            message_id: The id of the message that the image is attached to
        """
        image = Document({'image_id': image_id, "url":url},doc_id=message_id)
        return  self.images.insert(image)
    

    def add_user(self,image_id,user_id):

        user = Document({image_id:{
                                        "like":True,
                                        "dislike":False
                                        }
                                    },
                        doc_id=user_id
                    )

        return self.users.insert(user)

    def get_likes_dislike(self, image_id:str):
        """Counts all users likes
        returns
            all users likes
        """
        likes = 0
        dislike = 0
        for user in self.users:
                if user[image_id]['like']:
                    likes += 1
                else:
                    dislike += 1
        return likes, dislike
  
    def all_dislikes(self,dislikes:str):
        """Counts all users dislikes
        returns
            all users dislikes
        """
        q = tinydb.Query()
        return self.table.search(q.dislikes == dislikes)
    
    def all_likes(self,likes:str):

        q = tinydb.Query()
        return self.table.search(q.likes == likes)
        
    def add_like(self, user_id:str,image_id:str):
        '''
        Add a like to the database
        args:
            user_id: The user id of the user who liked the post
            image_id: The image id of the image that was liked
        returns:
            The number of likes and dislikes for the post
        '''
        if self.users.contains(doc_id=user_id):
            user_doc = self.users.get(doc_id=user_id)
            user_doc[image_id] = {
                'like': True, 
                'dislike': False
                }
        else:
            user_doc = {image_id: {
                'like': True, 
                'dislike': False
                }
            }
        user_doc = Document(user_doc, doc_id=user_id)
        self.users.insert(user_doc)
        

    def add_dislike(self, user_id:str,image_id:str):
        '''
        Add a dislike to the database
        args:
            user_id: The user id of the user who disliked the post
        returns:
            The number of likes and dislikes for the post
        '''
        if self.users.contains(doc_id=user_id):
            user_doc = self.users.get(doc_id=user_id)
            user_doc[image_id] = {
                'like': False, 
                'dislike': True
                }
        else:
            user_doc = {image_id: {
                'like': False, 
                'dislike': True
                }
            }
        user_doc = Document(user_doc, doc_id=user_id)
        self.users.insert(user_doc)