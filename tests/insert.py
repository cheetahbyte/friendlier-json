import asyncio
from pprint import pprint

from friendlier_json import Reader, Object
import datetime, names, random

start = datetime.datetime.utcnow()

reader = Reader()
reader.file = 'test.json'
# for i in range(200):
#    obj = Object(first_name=names.get_first_name(), last_name=names.get_last_name(), cash=random.randint(10, 20),
#                 random1=random.randint(100, 110))
#    reader.insert(obj)
print('Took: ' + str((datetime.datetime.utcnow() - start).total_seconds()) + 's')
