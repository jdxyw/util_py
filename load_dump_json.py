# Just small example for json load and dump
import json

with open("a.json", "w") as f:
    json.dump(json_object, f)

with open("a.json", "r") as f:
    json_object = json.load(f)
