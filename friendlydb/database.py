import json
import os
from typing import Union
from datetime import datetime
import logging
from converter import JsonObject

import typing


class Friendly(object):
    def __init__(self, path=None, debug: bool = None) -> None:
        self.path = path
        self.debug: bool = debug if debug is True else False
        self.sendDebugMessage('Debugmode: Active')
        self.cache: list = []

    def sendDebugMessage(self, msg) -> Union[None, str]:
        if self.debug is True:
            print('DEBUG[{}]: {}'.format(
                datetime.utcnow().strftime('%k:%M:%S'), msg))
            return
        else:
            return 'debug is not enabled'

    def getAll(self) -> list:
        with open(self.path, 'r') as f:
            data = json.load(f)
        self.sendDebugMessage(msg='Found data! Collected Data!')
        return [data]

    def countAll(self) -> int:
        with open(self.path, 'r') as f:
            data: dict = json.load(f)
        return len(data.keys())

    # database-actions
    def select(self, cache: bool = None, **kwargs) -> list:
        cache = True if cache else False
        localCache: list = []
        selection: list = []
        kwargsAsList = [i for i in kwargs if not i == 'limit']
        kwargsWeight: int = len(kwargsAsList)
        # caching
        if cache is True:
            for cachedObject in self.cache:
                counter: int = 0
                for key in cachedObject.keys():
                    for kwarg in kwargsAsList:
                        if key == kwarg and cachedObject[key] == kwargs[kwarg]:
                            counter += 1
                if counter == kwargsWeight:
                    localCache.append(cachedObject)
        if localCache:
            return localCache
        with open(self.path, 'r') as file:
            data: dict = json.load(file)
        for key in data.keys():
            true_counter: int = 0
            dataFromKey = data[key]
            for kwarg in kwargsAsList:
                if kwargs[kwarg] == dataFromKey[kwarg]:
                    true_counter += 1
            localCache.append({"counter": true_counter, "key": key})
        for i in localCache:
            if i['counter'] == kwargsWeight:
                selection.append(data[i['key']])
        if kwargs.get('limit'):
            selection = selection[:-(len(selection) - kwargs.get('limit'))]
        else:
            pass
        for dct in selection:
            self.cache.append(dct)
        return selection

    def insert_one(self, arg: typing.Union[JsonObject, dict]) -> bool:
        if isinstance(arg, JsonObject):
            arg = arg.to_json_wi()
        elif type(arg) is dict:
            arg = arg
        else:
            return False
            # TODO: RAISE ERROR
        with open(self.path, 'r') as file:
            dat: dict = json.load(file)
        identity = self.countAll()
        arg: dict = {str(identity + 1): arg}
        dat.update(arg)
        self.cache.append(arg)
        print(arg)
        with open(self.path, 'w') as f:
            json.dump(dat, f, indent=4)
        return True

    def insert_bulk(self, args: list) -> bool:
        for arg in args:
            if isinstance(arg, JsonObject):
                arg = arg.to_json_wi()
            elif type(arg) is dict:
                arg = arg
            else:
                raise Exception('Your list does not contain dict or instance of JsonObjectClass')
            self.cache.append(arg)
            with open(self.path, 'r') as file:
                dat: dict = json.load(file)
            identity = self.countAll()
            arg: dict = {str(identity + 1): arg}
            dat.update(arg)
            self.cache.append(arg)
            with open(self.path, 'w') as f:
                json.dump(dat, f, indent=4)
        return True
