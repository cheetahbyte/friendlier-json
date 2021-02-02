# Friendlier Json
![CodeQL](https://github.com/py-alpha-woelfchen/friendlier-json/workflows/CodeQL/badge.svg)
![PyPI - License](https://img.shields.io/pypi/l/friendlier-json)
![PyPI](https://img.shields.io/pypi/v/friendlier-json)
![Discord](https://img.shields.io/discord/718571168403292251)

#### Why should you use it?
- It was made with ❤️ !
- It is comparatively fast ⏩ ! (more about this soon)
- It is easy to understand 🧠 !
- It caches a lot ! 😋

Little Example:
```python
from friendlydb import Friendly
driver = Friendly
driver.path = 'path/to/your/json'
driver.select(limit=2)# Limits the number of results to 2 👍
```
### "Advanced" Examples
–––
#### Inserting ✍️:
```python
from friendlydb import Friendly, JsonObject
driver = Friendly(debug=True, path='path/to/your/json')
person1 = JsonObject(name='Maik', age=15)
driver.insert_one(person1) # method 1
driver.insert_one(person1.to_json()) #method 2
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
from friendlydb import Friendly
driver = Friendly()
driver.file = 'path/to/your/json'
result = driver.select(name='Maik', age=15)
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