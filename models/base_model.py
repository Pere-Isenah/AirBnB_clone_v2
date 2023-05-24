#!/usr/bin/python3
"""Defines a base class for all models"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()


class BaseModel:
    """A base class for all models

    Attributes:
        id (sqlalchemy.String): The BaseModel id
        created_at (sqlalchemy.DateTime): The datetime at creation
        updated_at (sqlalchemy.DateTime): The datetime as at last update
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow()) 
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        """Instantiates a new class instance

         Args:
            *args (any): Unused
            **kwargs (dict): Key/value pairs of attributes
        """
        if not kwargs or 'updated_at' not in kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            if kwargs:
                for k, v in kwargs.items():
                    setattr(self, k, v) 
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
        self.save()

    def __str__(self):
        """Returns a string representation of the class instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """updates the `updated_at` attribute after each change"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dictionary format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """Deletes the current class instance from storage"""
        models.storage.delete(self)