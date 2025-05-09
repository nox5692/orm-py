class BaseORMEntity:
    @classmethod
    def get_descriptors(cls):
        from .attribute import Attribute

        return {
            name: attr
            for name, attr in cls.__dict__.items()
            if isinstance(attr, Attribute)
        }
