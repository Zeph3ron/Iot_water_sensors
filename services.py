from datetime import datetime
import models


def get_total_bill(house_info, rate):
    return house_info.total * rate


def get_monthly_bill(house_array, rate, from_date, to_date):
    relevant_entries = get_entries(house_array, from_date, to_date)
    return get_total_bill(get_house_info(relevant_entries), rate)


def get_entries(house_array, from_date, to_date):
    relevant_entries = []
    for entry in house_array:
        entry_datetime = get_datetime(entry)
        if from_date < entry_datetime < to_date:
            relevant_entries.append(entry)
    return relevant_entries


def get_datetime(entry):
    return datetime.strptime(entry[0][0:26], '%Y-%m-%dT%X.%f')


def detect_leak(house_array, threshold):
    house_info = get_house_info(house_array)
    if house_info.current > threshold:
        if is_real_leak(house_array, house_info.current, get_datetime(house_array[0])):
            send_notification_email('email@email.com')


def is_real_leak(house_array, current_flow, leak_datetime):
    entries = get_entries(house_array, leak_datetime - (datetime.hour * 25), (leak_datetime - (datetime.hour * 23)))
    for entry in entries:
        if entry[1] <= current_flow:
            return True
        else:
            return False


def get_house_info(house_array):
    values = []
    for house_values in house_array:
        values.append(house_values[1])
    total = sum(values)
    return models.HouseInfo(min(values), max(values), total / len(values), values[0], total)


def send_notification_email(email_address):
    print('TODO: Implement')
