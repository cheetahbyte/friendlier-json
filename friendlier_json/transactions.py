import datetime
import json
import typing


class Object(object):
    """Converts anything to json :)"""

    def __init__(self, **kwargs) -> None:
        self.data: dict = {}
        for i in kwargs:
            self.data.update({i: kwargs[i]})

    def to_json(self) -> dict:
        """Returns the dict from the class"""
        return self.__dict__['data']


class Reader:
    def __init__(self):
        self.file = None
        self.actual_time = datetime.datetime.utcnow()

    def all(self) -> dict:
        with open(self.file, 'r') as f:
            data = json.load(f)
        return data

    def count(self) -> int:
        """Counts all entry's"""
        with open(self.file, 'r') as f:
            data: dict = json.load(f)
        return len(data.keys())

    # Database Actions here, do not touch !

    def select(self, **kwargs) -> list:
        with open(self.file, 'r') as f:
            data: dict = json.load(f)
        selection: list = []
        kwargs_weight = [i for i in kwargs if not i == 'limit']
        cache: list = []
        for key in data.keys():
            true_counter = 0
            data_from_key = data[key]
            for i in kwargs_weight:
                if kwargs[i] == data_from_key[i]:
                    true_counter += 1
            cache.append({"true": true_counter, "key": key})
        for i in cache:
            if i['true'] == len(kwargs_weight):
                selection.append(data[i['key']])
        if kwargs.get('limit'):
            x = len(selection) - kwargs.get('limit')
            selection = selection[:-x]
        else:
            pass
        return selection

    def insert(self, arg: typing.Union[Object, dict]) -> bool:
        if isinstance(arg, Object):
            arg = arg.to_json()
        elif type(arg) is dict:
            arg = arg
        else:
            return False
        # TODO: Raise error here
        with open(self.file, 'r') as file:
            dat: dict = json.load(file)

        identity = self.count()
        arg: dict = {identity + 1: arg}
        dat.update(arg)
        # print(arg)
        with open(self.file, 'w') as f:
            json.dump(dat, f, indent=4)
        return True