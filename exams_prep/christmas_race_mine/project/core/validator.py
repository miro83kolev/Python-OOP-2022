class Validator:
    @staticmethod
    def check_value_min_length(value, min_length, message):
        if len(value) < min_length:
            raise ValueError(message)

    @staticmethod
    def check_value_in_min_max_range(value, min_value, max_value, message):
        if not min_value <= value <= max_value:
            raise ValueError(message)

    @staticmethod
    def check_if_no_whitespace_or_empty_string(value, message):
        if value.strip() == '':
            raise ValueError(message)

    @staticmethod
    def check_if_valid_car_type(car_type):
        valid_car_types = ["MuscleCar", "SportsCar"]
        if car_type not in valid_car_types:
            return False
        return True

    @staticmethod
    def raise_if_car_model_exists(cars, car_model, message):
        for car in cars:
            if car.model == car_model:
                raise Exception(message)

    @staticmethod
    def raise_if_driver_name_exists(drivers, driver_name, message):
        for driver in drivers:
            if driver.name == driver_name:
                raise Exception(message)

    @staticmethod
    def raise_if_race_name_exists(races, name, message):
        for race in races:
            if race.name == name:
                raise Exception(message)

    @staticmethod
    def find_available_car(cars, car_type, message):
        for index in range(len(cars) - 1, -1, -1):
            car = cars[index]
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        raise Exception(message)

    @staticmethod
    def find_driver_by_name(drivers, driver_name, message):
        for driver in drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(message)

    @staticmethod
    def find_race_by_name(races, name, message):
        for race in races:
            if race.name == name:
                return race
        raise Exception(message)

    @staticmethod
    def raise_if_driver_doesnt_have_a_car(driver, message):
        if driver.car is None:
            raise Exception(message)

    @staticmethod
    def raise_if_not_enough_drivers_in_race(race, min_drivers, message):
        if len(race.drivers) < min_drivers:
            raise Exception(message)


