# Friendlier Json
![CodeQL](https://github.com/py-alpha-woelfchen/friendlier-json/workflows/CodeQL/badge.svg)
![PyPI - License](https://img.shields.io/pypi/l/friendlier-json)
![PyPI](https://img.shields.io/pypi/v/friendlier-json)
![Discord](https://img.shields.io/discord/718571168403292251)

#### Why should you use it?
- It was made with ❤️ !
- It is comparatively fast ⏩ ! (more about this soon)
- It is easy to understand 🧠 !

Little Example:
```python
from friendlier_json import Friendly
driver = Friendly()
driver.path = 'path/to/your/json'
driver.select_one()# Limits the number of results to 2 👍
```
### "Advanced" Examples
–––
#### Inserting ✍️:
```python
from friendlier_json import Friendly, JsonObject
with Friendly() as driver:
    driver.insert({"name": "Leo", "age": 15})
```


Your .json will look like this:
```json
{
    "default": [
      {
        "name": "Leo",
        "age": 15
      }
    ]
}
```
#### Selecting  🔭:
```python
from friendlier_json import Friendly, JsonObject
with Friendly() as driver:
    human = driver.select_one(name="Leo", age="20")
    print(human.age)
# this will return a Document, see the Documentation
```
