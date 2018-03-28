from pymongo import MongoClient
import config

class Notes(object):

    def __init__(self):
        client = MongoClient(config.MONGO_URI)
        db = client.notes
        self.collection = db.notes


    def find(self):
        """
        Obtener todas las notas
        """
        cursor = self.collection.find()

        notes = []

        for note in cursor:
            notes.append(note)

        return notes

    def findOne(self, id):
        """
        Obtener la nota con id
        """
        note = self.collection.find_one({'_id': id})

        return note


    def create(self, note):
        """
        Insertar una nota nueva
        """
        result = self.collection.insert_one(note)

        return result

    def delete(self, id):
        """
        Eliminar una nota
        """
        result = self.collection.delete_one({'_id': id})

        return result

    def update(self, id, note):
        """
        Actualizar una nota
        """
        result = self.collection.replace_one({'_id': id}, note )

        return result
