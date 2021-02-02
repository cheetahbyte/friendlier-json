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
