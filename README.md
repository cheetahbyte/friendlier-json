# Friendlier Json

Bored of the normal json? Fed up with SQL? Then Friendlier Json will be exactly the right thing for you!
#### Why should you use it?
- It was made with ❤️ !
- It is comparatively fast ⏩ ! (more about this soon)
- It is easy to understand 🧠 ! 

Little Example:
```python
from friendlier_json import Reader
reader = Reader()
reader.file = 'path/to/your/json'
reader.select(limit=2)# Limits the number of results to 2 👍
```
### "Advanced" Examples
–––
#### Inserting ✍️:
```python
from friendlier_json import Reader, Object
reader = Reader()
reader.file = 'path/to/your/json'
person1 = Object(name='Maik', age=15)
#the reader can take both the class and a JSON object or a dict as argument. There are 2 methods
reader.insert(person1) # method 1
reader.insert(person1.to_json()) #method 2
```


Your .json will look like this:
```json
{
    "1": {
        "name": "Maik",
        "age": 15
    }
}
```
#### Selecting  🔭:
```python
from friendlier_json import Reader
reader = Reader()
reader.file = 'path/to/your/json'
result = reader.select(name='Maik', age=15)
print(result)
# this will return a list object
```
#### Benchmarks 📊:
##### Inserting:
| Quantity | Time required (s) |
|:--------:|:-----------------:|
| 1        | 0.000429          |
| 10       | 0.004077          |
| 100      | 0.110214          |
| 1000     | 6.013882          |

##### Selecting:
| Quantity | Time required (s) |
|:--------:|:-----------------:|
| 1        | 0.002409          |
| 10       | 0.003234          |
| 100      | 0.00242           |
| 1000     | 0.003081          |
