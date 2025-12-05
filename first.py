#import standard library
# import math
# print(math.sqrt(25))

#import specific function
# from math import sqrt, pi
# print(sqrt(25))
# print(pi)

#alias
# import math as m
# print(m.sqrt(25))

# from datetime import datetime as dt
# print(dt.now())

# from pathlib import Path
# filepath = Path('first.py')
# if(filepath.exists()):
#     print(filepath.read_text())


import json

data = {"name": "Almaaz", "age": 25}
json_str = json.dumps(data)
parsed_data = json.loads(json_str)
print(type(json_str))
print(json_str)
print(parsed_data)
