import json
import traceback
import jsonpickle
import models
import time
import databasehandler
import ttn
import decoder

# Toggles between using a text-file or the database
use_database = True
enable_logging = True

log_path = 'measurements_log.txt'
collection_file_path = 'message_collection.txt'

app_id = 'watermeter-test01'
access_key = 'ttn-account-v2.S6_w-wpG19AvLeUNjorYMhx4uctru7dmed_fcTwyvlQ'


def save_to_textfile(msg, filename):
    with open(filename, 'w') as file:
        file.write(msg + '\n')


def save_as_json(msg, filename):
    json_string = jsonpickle.encode(msg)
    save_to_textfile(json_string, filename)


def log_message(entry):
    if enable_logging:
        print(entry)
        time_now = time.strftime("[%d-%m-%Y %H:%M:%S] ", time.gmtime())
        with open(log_path, 'a') as log_file:
            log_file.write(time_now + entry + '\n')


def parse_messages():
    if use_database:
        collection = []
        records = databasehandler.get_records()
        for record in records:
            collection.append(jsonpickle.decode(record.Json_value))
        return collection
    else:
        with open(collection_file_path, 'r') as collection_file:
            return jsonpickle.decode(collection_file.read())


def handle_message(msg):
    try:
        message = models.serialize_message(msg)
        message_collection.append(message)
        try:
            if use_database:
                databasehandler.save_record(jsonpickle.encode(message))
            else:
                save_to_textfile(jsonpickle.encode(message_collection, collection_file_path))
        except Exception:
            log_message('Exception thrown whilst trying to save the collection as json.')
            traceback.print_exc()
        log_message('Message successfully handled.')
        decoder.update_house_dict(house_dict, msg)

    except Exception:
        log_message('Exception thrown whilst trying to parse the message.')
        traceback.print_exc()


def uplink_callback(msg, client):
    log_message(f'Received uplink from: {msg.dev_id}. \n{msg}')
    handle_message(msg)


def connect_callback(res, client):
    if res:
        log_message('Successfully connected to network.')
    else:
        log_message('Failed connecting to the network')


def downlink_callback(mid, client):
    log_message(f'Id of down_link request {mid}')


def close_callback(res, client):
    log_message('close_callback - Entered')
    if res:
        log_message('Connection closed.')
    else:
        log_message('Failed closing connection.')
    log_message('close_callback - Exited')


message_collection = parse_messages()
house_dict = decoder.parse_house_dict(message_collection)

handler = ttn.HandlerClient(app_id, access_key)
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.set_connect_callback(connect_callback)
mqtt_client.set_close_callback(close_callback)
mqtt_client.set_downlink_callback(downlink_callback)

mqtt_client.connect()
time.sleep(4000)
mqtt_client.close()
