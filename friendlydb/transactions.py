import json
import typing

import prettytable
import pydantic

from .converter import JsonObject


class Friendly(object):
    def __init__(self, path=None, debug: bool = False) -> None:
        self.path = path
        self.debug = debug
        self.cache = list()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    @staticmethod
    def __validate_object(arg: typing.Union[pydantic.BaseModel, dict, JsonObject]):
        if isinstance(arg, pydantic.BaseModel):
            return arg.dict()
        elif isinstance(arg, JsonObject):
            return arg.to_json_wi()
        elif type(arg) is dict:
            return arg

    def __show_value(self, arg: typing.Union[pydantic.BaseModel, JsonObject, dict]):
        return self.__validate_object(arg)

    def insert(self, arg: typing.Union[pydantic.BaseModel, JsonObject, dict]):
        arg = self.__validate_object(arg)
        with open(self.path, "r") as f:
            data: dict = json.load(f)
        # TODO: Add support for table
        default_table: dict = data['_default']
        default_table.update({f"{len(default_table) + 1}": arg})
        data.pop("_default")
        data['_default'] = default_table
        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)
        self.cache.append(arg)

    def search(self, **kwargs) -> list:
        localCache: list = list()
        selection: list = list()
        with open(self.path, "r") as file:
            data: dict = json.load(file)
        data = data['_default']
        data_pool = data.update(self.cache)
        for key in data.keys():
            counter = 0
            data_key: dict = data[key]
            for kwarg in [kw for kw in kwargs if not kw == "limit"]:
                if kwargs[kwarg] == data_key[kwarg]:
                    counter += 1
            localCache.append({"counter": counter, "key": key})
        for obj in localCache:
            if obj['counter'] == len([kw for kw in kwargs if not kw == "limit"]):
                selection.append(data[obj["key"]])
        if kwargs.get('limit'):
            selection = selection[:-(len(selection) - kwargs.get('limit'))]
        else:
            pass
        for dct in selection:
            self.cache.append(dct)
        return selection

    def delete(self, **kwargs) -> str:
        selection = self.search(**kwargs)
        if len(selection) > 3:
            query = selection[:-len(selection) + 1]
        else:
            query = selection
        if len(selection) == 0:
            raise ValueError("No matching entry in database")
        with open(self.path, 'r') as f:
            data_raw = json.load(f)
        data = data_raw['_default']
        for key in data.keys():
            pre_data = data[key]
            if pre_data == query[0]:
                data.pop(key)
                break
        with open(self.path, 'w') as file:
            json.dump(data_raw, file, indent=4)
        return 'Dropped: ' + str(query[0])

    def list_all(self, directprint: bool = False):
        table = prettytable.PrettyTable()
        with open(self.path, "r") as f:
            data: dict = json.load(f)
        data: dict = data["_default"]
        column: list = []
        for i in data.keys():
            for x in data[i].keys():
                column.append(x)
            break
        table.field_names = column
        for i in data.keys():
            for_row = list()
            for x in data[i]:
                for_row.append(data[i][x])
            table.add_row(for_row)
        if directprint is True:
            print(table)
        else:
            return table
