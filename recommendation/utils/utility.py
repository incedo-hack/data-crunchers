class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class Cors:
    def __init__(self, enable=False):
        self.enable = enable

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            if self.enable:
                kwargs['headers'] = {"Content-Type": "application/json",
                                     "Access-Control-Allow-Origin": "*",
                                     "Access-Control-Allow-Credentials": True
                                     }
            else:
                kwargs['headers'] = {"Content-Type": "application/json"}
            return func(*args, **kwargs)
        return wrapper


class Structure:
    _fields = []

    def __init__(self, **kwargs):
        for name in self.__class__._fields:
            setattr(self, name, kwargs.get(name))


class LdapStruct(Structure):
    _fields = ['ldap_host', 'ldap_port', 'ldap_timeout', 'bind_username', 'bind_password', 'auto_bind', 'is_ssl']


class UserSearchStruct(Structure):
    _fields = ['search_base', 'search_attr', 'attributes']

