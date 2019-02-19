class Message:
    def __init__(self, app_id, dev_id, hardware_serial, port, counter, payload_raw, metadata):
        self.app_id = app_id
        self.dev_id = dev_id
        self.hardware_serial = hardware_serial
        self.port = port
        self.counter = counter
        self.payload_raw = payload_raw
        self.metadata = MetaData(metadata.time,
                                 metadata.frequency,
                                 metadata.modulation,
                                 metadata.data_rate,
                                 metadata.coding_rate,
                                 metadata.gateways)


class MetaData:
    def __init__(self, time, frequency, modulation, data_rate, coding_rate, gateways):
        self.time = time
        self.frequency = frequency
        self.modulation = modulation
        self.data_rate = data_rate
        self.coding_rate = coding_rate
        gateway_array = []
        for gateway in gateways:
            gateway_array.append(GateWay(gateway.gtw_id,
                                         gateway.timestamp,
                                         gateway.time,
                                         gateway.channel,
                                         gateway.rssi,
                                         gateway.snr,
                                         gateway.rf_chain,
                                         gateway.latitude,
                                         gateway.longitude,
                                         gateway.altitude))
        self.gateways = gateway_array


class GateWay:
    def __init__(self, gtw_id, timestamp, time, channel, rssi, snr, rf_chain, latitude, longitude, altitude):
        self.gtw_id = gtw_id
        self.timestamp = timestamp
        self.time = time
        self.channel = channel
        self.rssi = rssi
        self.snr = snr
        self.rf_chain = rf_chain
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude


class House:
    def __init__(self, name, value):
        self.name = name
        self.value = value


def serialize_message(msg):
    return Message(msg.app_id,
                   msg.dev_id,
                   msg.hardware_serial,
                   msg.port,
                   msg.counter,
                   msg.payload_raw,
                   msg.metadata)
