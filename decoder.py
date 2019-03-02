import models
import jsonpickle
import base64


def parse_house_dict(message_collection):
    house_dict = {"House_0": [], "House_1": [], "House_2": [], "House_3": []}
    for msg in message_collection:
        decoded = base64.b64decode(msg.payload_raw).hex()
        ba = bytearray(decoded, 'utf-8')

        house_dict["House_0"].append({msg.metadata.time, ba[0]})
        house_dict["House_1"].append({msg.metadata.time, ba[1]})
        house_dict["House_2"].append({msg.metadata.time, ba[2]})
        house_dict["House_3"].append({msg.metadata.time, ba[3]})

    return house_dict


def update_house_dict(house_dict, msg):
    decoded = base64.b64decode(msg.payload_raw).hex()
    ba = bytearray(decoded, 'utf-8')

    house_dict["House_0"].append({msg.metadata.time, ba[0]})
    house_dict["House_1"].append({msg.metadata.time, ba[1]})
    house_dict["House_2"].append({msg.metadata.time, ba[2]})
    house_dict["House_3"].append({msg.metadata.time, ba[3]})