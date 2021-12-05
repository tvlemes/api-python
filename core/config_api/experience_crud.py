import firebase_admin
from core.config_api.firebase_connection import FirebaseConnection


class ExperienceCrud(FirebaseConnection):
    client = FirebaseConnection

    # INSERT EXPERIENCE
    def create(self, data):
        """Create todo in firestore database"""
        doc_ref = self._collection.document()
        id = doc_ref.id
        data = {
            'id': id,
            'company': data['company'],
            'occupation': data['occupation'],
            'briefsummary': data['briefsummary'],
            'activities': data['activities'],
            'tags': data['tags'].split(),
            'start_date': data['start_date'],
            'departure_date': data['departure_date'],
        }
        doc_ref.set(data)
        
    # UPDATE EXPERIENCE BY ID
    def update(self, id, data):
        """Update todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        data = {
            'id': id,
            'company': data['company'],
            'occupation': data['occupation'],
            'briefsummary': data['briefsummary'],
            'activities': data['activities'],
            'tags': data['tags'].split(),
            'start_date': data['start_date'],
            'departure_date': data['departure_date'],
        }
        doc_ref.update(data)