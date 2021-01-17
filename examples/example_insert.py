from friendlier_json import Reader, Object
import datetime

time = datetime.datetime.utcnow()
reader = Reader()
reader.file = 'test.json'
person1 = Object(name='Maik', age=15)
reader.insert(person1)
