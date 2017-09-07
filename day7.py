import json
def myfuct():
# Encoding dicttionary as a JSON
data = [ {'a':'A', 'b':(2, 4), 'c':3.0}]
data_json = json.dumps(data)

print ('json string:',data_json)

# Decoding a JSON string into a python dict
python_dic = json.loads((data_json))

print('python dict:',python_dic)

# Sorting the JSON data
data_json = json.dumps(data,sort_keys=True)
print('JSON string, sorted:', data_json)

# Read adble

data_json_readable = json.dumps(data, sort_keys=True, indent=4)

print("JSON string, sorted , readable:", data_json_readable)

return


