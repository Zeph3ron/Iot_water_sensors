import models
import jsonpickle
import base64

collection_file_path = 'message_collection.txt'


def parse_collection():
    with open(collection_file_path, 'r') as collection_file:
        return jsonpickle.decode(collection_file.read())

messages = parse_collection()

def assing_values(message):
    decoded = base64.b64decode(message.payload_raw).hex()
    ba = bytearray(decoded,'utf-8')
    houses_dict = {
        "House_0" : ba[0],
        "House_1" : ba[1],
        "House_2" : ba[2],
        "House_3" : ba[3],
            }
    return houses_dict



print(assing_values(messages[3]))
