import json
from contextlib import suppress

import pydantic
from converter import JsonObject, Document
from typing import *
import os
import random
import string


class Friendly(object):
    def __init__(self, path: str = None, debug: bool = False) -> None:
        self.path = path
        self.debug = debug

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    @staticmethod
    def check_file(path) -> None:
        if os.path.isfile(path):
            pass
        else:
            with open(path, "w") as file:
                json.dump({}, file)
                file.close()

    @staticmethod
    def __validate_object(arg: Union[pydantic.BaseModel, dict, JsonObject]) -> dict:
        """ This converts and checks specified arguments."""
        if isinstance(arg, pydantic.BaseModel):
            return arg.dict()
        elif isinstance(arg, JsonObject):
            return arg.to_json()
        elif type(arg) is dict:
            return arg

    @staticmethod
    def gen_objid():
        letters = string.ascii_letters + string.digits
        objid = "".join(random.choice(letters) for _ in range(20))
        return objid

    def test(self):
        self.check_file(path=self.path)

    def insert(self, arg: Union[pydantic.BaseModel, JsonObject, dict], table: str = "default") -> str:
        self.check_file(self.path)
        table_name = table
        inserted_id = self.gen_objid()
        arg = self.__validate_object(arg)
        with open(self.path, "r") as file:
            data: dict = json.load(file)
        local: dict = data.copy()
        table: list
        try:
            table: list = local[table]
        except KeyError:
            local[table_name] = []
            table = local[table_name]
        try:
            if arg["_id"] is not None:
                inserted_id = arg["_id"]
        except KeyError:
            arg.update({"_id": inserted_id})
        table.append(arg)
        with open(self.path, "w") as f:
            json.dump(local, f, indent=4)
        return inserted_id

    def select_one(self, **kwargs):
        """This is the equivalent of find, only with an ORM-like specification of the search conditions."""
        self.check_file(self.path)
        with suppress(KeyError):
            table = kwargs.get("table") if kwargs.get("table") else "default"
            with open(self.path, "r") as file:
                data = json.load(file)
            data = data[table]
            # apply filters
            for obj in data:
                counter: int = 0
                for kw in [kw for kw in kwargs if not kw == "table"]:
                    if obj[kw] == kwargs[kw]:
                        counter += 1
                    if counter == len([kw for kw in kwargs if not kw == "table"]):
                        return Document(obj)

    def find_one(self, filtr: dict, table: str = "default"):
        """ This is the equivalent of select, the search arguments are passed here as dict. """
        self.check_file(self.path)
        with suppress(KeyError):
            with open(self.path, "r") as file:
                data = json.load(file)
            data = data[table]
            # apply filters
            for obj in data:
                counter: int = 0
                for key in filtr.keys():
                    if obj[key] == filtr[key]:
                        counter += 1
                if counter == len(filtr.keys()):
                    return Document(obj)

    def delete(self, filter: dict, table: str ) -> None:
        self.check_file(self.path)
        with open(self.path, "r") as file:
            data = json.load(file)
        real = data
        data = data[table]
        localcache: list = []
        for obj in data:
            counter:int = 0
            for fkey in filter.keys():
                try:
                    if filter[fkey] == obj[fkey]:
                        counter += 1
                except KeyError:
                    pass
            localcache.append({f"{counter}": obj})
        for cached_dict in localcache:
            for key in cached_dict.keys():
                if int(key) == len(filter.keys()):
                    data.remove(cached_dict[key])
        real[table] = data
        with open(self.path, "w") as f:
            json.dump(real, f, indent=4)


    def update(self, filtr: dict, new: dict, table:str) -> str:
        self.delete(filtr, table)
        self.insert(new, table)
