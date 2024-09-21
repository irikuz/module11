class Intro:
    def __init__(self, obj):
        self.obj = obj

    def introspection_info(obj):
        info = {
            'type': type(obj),
            'attributes': dir(obj),
            'methods': [method for method in dir(type(obj)) if callable(getattr(type(obj), method))],
            'module': obj.__module__
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
