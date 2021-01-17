from friendlier_json import Reader, Object
import datetime

time = datetime.datetime.utcnow()
reader = Reader()
reader.file = 'test.json'
reader.select(limit=1000)
