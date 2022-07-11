# CountDownSound
A Python Project Which Plays Sound When The CountDown Gets Over made By Blood
# Have Config For Path
```py
config = {
  "path": "Your Path"
}
```
# Works As An API
## Import
```py
from CountDownPlay import CDP
```
## creating
```py
time = int(input("......"))
var = CDP(time)

```
## Adding Sound
```py
var.play(config["path"])  # if you are not using config.py then u need to type path directly here i.e - var.play("path")
```
