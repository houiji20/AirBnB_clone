#!/usr/bin/python3
"""Base class to base other classes on."""
from uuid import uuid4
from datetime import datetime
from . import storage

class BaseModel():
    """Base class for models."""

    def __init__(self, **kwargs):
        """Initialize Instance."""
        if (kwargs):
            for key in kwargs:
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(kwargs[key]))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation."""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save Instance to storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Class to dict."""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()

        return dict
