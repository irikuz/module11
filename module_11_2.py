class Intro:
    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        info = {
            "type": type(self.obj),
            "attributes": [attr for attr in dir(self.obj)
                           if not callable(getattr(self.obj, attr))],
            "methods": [attr for attr in dir(self.obj)
                        if callable(getattr(self.obj, attr))],
            "module": getattr(self.obj, '__module__', 'builtins'),
        }
        return info

    def __str__(self):
        return str(self.introspection_info())


number_info = Intro(42)
print(number_info)

list_info = Intro([1, 2, 3])
print(list_info)

string_info = Intro("Irina")
print(string_info)

dict_info = Intro({"key": "value"})
print(dict_info)
