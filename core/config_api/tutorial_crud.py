import firebase_admin
from core.config_api.firebase_connection import FirebaseConnection


class TutorialCrud(FirebaseConnection):
    client = FirebaseConnection
    
    # INSERT EXPERIENCE
    def create(self, data):
        """Create todo in firestore database"""
        doc_ref = self._collection.document()
        id = doc_ref.id
        data = {
            'id': id,
            'name': data['name'],
            'technology': data['technology'],
            'description': data['description'],
            'markdown': data['markdown'],
            'tags': data['tags'].upper().split(),
        }

        doc_ref.set(data)
        
    # UPDATE EXPERIENCE BY ID
    def update(self, id, data):
        """Update todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        data = {
            'id': id,
            'name': data['name'],
            'technology': data['technology'],
            'description': data['description'],
            'markdown': data['markdown'],
            'tags': data['tags'].upper().split(),
        }
        doc_ref.update(data)