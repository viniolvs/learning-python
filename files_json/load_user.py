import json
import _tkinter

filename = 'username.json'
with open(filename, 'r') as f_obj:
    username = json.load(f_obj)

print("Welcome back "+username+"!")