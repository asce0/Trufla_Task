import json
import xmltodict

# read the xml file and convert it into dict
with open(r"input_data\xml\customer1.xml") as xml_file:
      
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

# convert the dict  into a json string
json_data = json.dumps(data_dict)
# write the json string into json file
with open("parsing_result\Xml_result\customer1.json", "w") as json_file:
    json_file.write(json_data)
    json_file.close()