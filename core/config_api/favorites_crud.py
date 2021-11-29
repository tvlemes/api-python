import firebase_admin
from core.config_api.firebase_connection import FirebaseConnection

class FavoritesCrud(FirebaseConnection):
    client = FirebaseConnection
    
    # INSERT FAVORITES
    def create(self, data):
        """Create todo in firestore database"""
        doc_ref = self._collection.document()
        id = doc_ref.id
        data = {
            'id': id,
            'name': data['name'],
            'url_name': data['url_name'],
            'url_image': data['url_image'],
            'briefsummary': data['briefsummary'],
            'tags': data['tags'].split(),
            'favorites': data['favorites'],
        }
        doc_ref.set(data)
        
    # UPDATE FAVORITES BY ID
    def update(self, id, data):
        """Update todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        data = {
            'id': id,
            'name': data['name'],
            'url_name': data['url_name'],
            'url_image': data['url_image'],
            'briefsummary': data['briefsummary'],
            'tags': data['tags'].split(),
            'favorites': data['favorites'],
        }
        doc_ref.update(data)