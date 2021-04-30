import json


class JsonObject(object):
    """ Converts anything to json :) """

    def __init__(self, **kwargs) -> None:
        self.data: dict = {}
        for i in kwargs:
            self.data.update({i: kwargs[i]})

    def __repr__(self):
        return '<JsonObject:%s>' % self.__dict__['data']

    def to_json(self) -> dict:
        """Returns an beautiful json object"""
        return dict(json.dumps(self.__dict__['data'], indent=4))

    def to_json_wi(self) -> dict:
        return self.__dict__['data']


class Document(object):
    r""" Takes a Dictonnary and makes a beautiful class out of it."""

    def __init__(self, dictonary: dict) -> None:
        for key in dictonary.keys():
            setattr(self, str(key), dictonary[key])
