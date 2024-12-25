# -*- coding: utf-8 -*-

from inspect import getmodule


def introspection_info(obj):
    obj_type = type(obj).__name__
    obj_attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    obj_methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    obj_module = getmodule(obj) if getmodule(obj) else 'builtin'

    result = {
        'type': obj_type,
        'attributes': obj_attributes,
        'methods': obj_methods,
        'module': obj_module
    }

    return result

class MyClass:
    def __init__(self, value):
        self.value = value
        self.description = "Это экземпляр MyClass"

    def increment(self):
        self.value += 1
        return self.value

    def decrement(self):
        self.value -= 1
        return self.value

    def reset(self):
        self.value = 0
        return self.value

    def __str__(self):
        return f"MyClass(value={self.value}, description='{self.description}')"


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)
    
    print()
    
    class_info = introspection_info(MyClass(10))
    print(class_info)

