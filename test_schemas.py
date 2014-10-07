from jsonschema import validate
import json
import os
# for each file in schemas
# put it into the schemas list

schemas = []
for file in os.listdir("schemas"):
    if file.endswith('.json'):
        with open(os.path.join('schemas',file), 'r') as file_handle:
            print "Loading schema {}".format(file)
            json_obj = json.load(file_handle)
        file_handle.close()
        schemas.append((file,json_obj))

# for each file in objects
# put it into the objects list
objects = []
for file in os.listdir("objects"):
    if file.endswith('.json'):
        with open(os.path.join('objects',file), 'r') as file_handle:
            print "Loading object {}".format(file)
            json_obj = json.load(file_handle)
        file_handle.close()
        objects.append((file,json_obj))

print ""
print "------------------------------"
print ""

for schema in schemas:
    print "Validating objects against schema: {}".format(schema[0])
    for obj in objects:
        try:
            validate(obj[1],schema[1])
            print "  Valid - {}".format(obj[0])
        except:
            print "  Not valid - {}".format(obj[0])
