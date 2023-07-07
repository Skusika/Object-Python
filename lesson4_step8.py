import json
# Задача номер 1
# Класс DictMixin представляет собой миксин,
# который добавляет в класс, наследующий его, метод to_dict().
# Этот метод позволяет преобразовать объект в словарь.

# Вариант один
class DictMixin:
    def to_dict(self):
        return json.loads(json.dumps(self, default=lambda x: x.__dict__))
# Вариант два
class DictMixin:
    def __repr__(self):
        return str(self.__dict__)

    def to_dict(self):
        return eval(self.__repr__())
# Вариант три
class DictMixin:
    def to_dict(self) -> dict:
        dct = self.__dict__
        for k, v in dct.items():
            if isinstance(v, DictMixin):
                dct[k] = v.to_dict()
            if isinstance(v, list):
                for i,k in enumerate(v):
                    if isinstance(k, DictMixin):
                        v[i] = k.to_dict()
        return dct
# Вариант четыре
class DictMixin:
    def to_dict(self):
        a = {}
        for i, j in self.__dict__.items():
            if isinstance(j, DictMixin):
                a[i] = j.to_dict()
            elif isinstance(j, list):
                p = []
                for item in j:
                    p.append(item.to_dict())
                a[i] = p
            else:
                a[i] = j
        return a


# Задача номер 2
# Внутри миксина JsonSerializableMixin обязательно должен быть метод to_json(),
# который возвращает итоговую строку сериализации объекта
# Вариант один
class JsonSerializableMixin:
    def to_json(self):
        data = json.loads(json.dumps(self, default=lambda x: x.__dict__))
        return json.dumps(data)
# Вариант два
import json
class JsonSerializableMixin(json.JSONEncoder):

    def default(self, obj):
        return obj.__dict__
    def to_json(self):
        return json.dumps(self, cls=JsonSerializableMixin)
# Вариант три
class JsonSerializableMixin:
    def to_json(self):
        a = json.dumps(self.__dict__, default=lambda x: x.__dict__)
        return a
