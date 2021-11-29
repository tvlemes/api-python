import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.conf import settings

class FirebaseConnection:
    
    def __init__(self, collection_name):
        """Class construct"""
        if not firebase_admin._apps: 
            cred = credentials.Certificate(
                settings.FIREBASE_ADMIN_CERT 
            )
            firebase_admin.initialize_app(cred)
        self._db = firestore.client()
        self._collection = self._db.collection(collection_name) 
  

    # GET ALL 
    def all(self):
        """Get all todo from firestore database"""
        docs = self._collection.get()
        docs = self._collection.stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]

    # GET BY ID
    def get_by_id(self, id):
        """Get todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        doc = doc_ref.get()

        if doc.exists:
            return {**doc.to_dict(), "id": doc.id}
        return
    
    # DROP BY ID
    def delete_by_id(self, id):
        """Delete todo on firestore database using document id"""
        self._collection.document(id).delete()