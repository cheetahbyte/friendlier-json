# Friendlier Json
Bored of the normal json? Fed up with SQL? Then Friendlier Json will be exactly the right thing for you!

#### Why should I use friendlier json?
- It was made with ❤️ ! 
- It is comparatively fast ⏩ ! ( 200 entries / 1s (Insert) )
- Easy to understand 🧠 !
 
 Little Example
```py
from friendlier_json import Reader
reader = Reader()
reader.file = 'path/to/your/file'
reader.select(limit=2) # Limits the number of results to 2 👍
```
### "Advanced" Examples
----
#### Inserting ✍️:
```py
from friendlier_json import Reader, Object
reader=Reader()
reader.file = 'path/to/your/json'
## Time to declare the object
person1 = Object(name='Maik', age=15) 
# the reader can take both the class and a JSON object or a dict as argument.
# method 1
reader.insert(person1)
#method 2
reader.insert(person1.to_json())
# to_json immediately converts the class to a dict
```
Your json will look like this
```json
{
	"1": {
	"name": "Maik",
	"age": 15
	}
}
```
#### Selecting 🔭:
```py
from friendlier_json import Reader
reader=Reader()
reader.file = 'path/to/your/json'
result = reader.select(name='Maik', age=15)
print(result)
```
Do you have any ideas on how I can improve this package even more? Feel free to let me know !