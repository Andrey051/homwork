import inspect

class ClassHome():
    number = 50

    def some_class(x):
        pass


def introspection_info(obj):
    dict_ = {}
    dict_["type"] = type(obj)
    #print(f"Тип объекта: {type(obj)}")
    dict_["attributes"] = dir(obj)
    #print(f"Атрибут объекта: {dir(obj)}")
    dict_["methods"] = inspect.getmembers(obj)
    #print(f"Метод: {inspect.getmembers(obj)}")
    dict_["module"]= inspect.getmodule(obj)
    #print(f"Модуль: {inspect.getmodule(obj)}")
    return dict_


number_info = introspection_info(42)
print(number_info)

obj_home= ClassHome()
number_info = introspection_info(obj_home)
print(number_info)

number_info = introspection_info(ClassHome)
print(number_info)