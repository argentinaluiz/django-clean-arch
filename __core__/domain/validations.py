
from __core__.domain.exceptions import EntityValidationException
import uuid

class DomainValidation:

    @staticmethod
    def not_null(field, value):
        if not value:
            raise EntityValidationException('The %s field is required' % field)

    @staticmethod
    def max_length(field, value, max):
        if len(value) > max:
            raise EntityValidationException('The %s field must be %s characters or less' % (field, str(max)))

    @staticmethod
    def min_length(field, value, min):
        if len(value) < min:
            raise EntityValidationException('The %s field must be %s characters or more' % (field, str(min)))
    
    @staticmethod
    def boolean(field, value):
        if value != True and value != False:
            raise EntityValidationException('The %s field must be boolean' % (field))
    
    @staticmethod
    def uuid(field, value):
        try:
            uuid.UUID(str(value))
        except ValueError:
            raise EntityValidationException('The %s field must be a valid uuid' % (field))
