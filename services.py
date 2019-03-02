import models


def get_bill(house_info, rate):
    return house_info.total * rate


def detect_leak(house_dict, threshold):
    print("implement")


def get_house_info(house_dict, house_name):
    values = []
    for house_values in house_dict[house_name]:
        values.append(house_values[1])
    total = sum(values)
    return models.HouseInfo(house_name, min(values), max(values), total / len(values), values[0], total)
