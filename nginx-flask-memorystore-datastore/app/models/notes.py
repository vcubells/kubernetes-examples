# Imports the Google Cloud client library
from google.cloud import datastore
import config

class Notes(object):

    def __init__(self):
        self.client = datastore.Client(config.PROJECT_ID)
        

    def find(self):
        """
        Obtener todas las notas
        """
        notes = []

        query = self.client.query()

        for note in query.fetch():
            note['id'] = note.key.id

            notes.append(note)

        return notes

    def findOne(self, id):
        """
        Obtener la nota con id
        """
        key = self.client.key('Note', int(id))
        
        note = self.client.get(key)

        note['id'] = note.key.id

        return note


    def create(self, data):
        """
        Insertar una nota nueva
        """
        key = self.client.key('Note')

        note = datastore.Entity(key)

        note.update(data)

        self.client.put(note)



        return note.key


    def delete(self, id):
        """
        Eliminar una nota
        """
        key = self.client.key('Note', int(id))
        
        self.client.delete(key)


    def update(self, id, data):
        """
        Actualizar una nota
        """
        with self.client.transaction():
            key = self.client.key('Note', int(id))
            note = self.client.get(key)

            if not note:
                raise ValueError(
                    'Note {} does not exist.'.format(id))

            note.update(data)

            self.client.put(note)

