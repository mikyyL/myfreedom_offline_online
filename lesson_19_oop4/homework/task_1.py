class Car:
    def __init__(self):
        object_id_collector = self.id


class CarCommander:
    def __init__(self):
        object_id_collector = self.id


class CarGunner:
    def __init__(self):
        object_id_collector = self.id


def check_object_id_collector():
    expected_ids = (1, 2, 3, 4, 5)
    actual_ids = (CarGunner().id, CarGunner().id, Car().id, CarCommander().id, Car().id)
    assert actual_ids == expected_ids, 'Expected_ids: {}. Actual_ids: {}.'.format(expected_ids, actual_ids)
    print('Test passed. Amazing job!')


check_object_id_collector()
