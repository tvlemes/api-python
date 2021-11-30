import firebase_admin
from core.config_api.firebase_connection import FirebaseConnection


class CourseCrud(FirebaseConnection):
    client = FirebaseConnection
    
    # INSERT EXPERIENCE
    def create(self, data):
        """Create todo in firestore database"""
        doc_ref = self._collection.document()
        id = doc_ref.id
        data = {
            'id': id,
            'name': data['name'],
            'institution': data['institution'],
            'workload': data['workload'],
            'briefsummary': data['briefsummary'],
            'content': data['content'],
            'start_date': data['start_date'],
            'departure_date': data['departure_date'],
            'url_image': data['url_image'],
            'tags': data['tags'].split(),
        }
        doc_ref.set(data)
        
    # UPDATE EXPERIENCE BY ID
    def update(self, id, data):
        """Update todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        data = {
            'id': id,
            'name': data['name'],
            'institution': data['institution'],
            'workload': data['workload'],
            'briefsummary': data['briefsummary'],
            'content': data['content'],
            'start_date': data['start_date'],
            'departure_date': data['departure_date'],
            'url_image': data['url_image'],
            'tags': data['tags'].split(),
        }
        doc_ref.update(data)