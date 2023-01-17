import db


class DynamoDbInterface:
    @staticmethod
    def add_passenger(passenger: dict, passenger_id: int) -> dict:
        return db.add_passenger(passenger, passenger_id)

    @staticmethod
    def get_passenger(passenger_id: str) -> dict:
        return db.get_passenger(passenger_id)

    @staticmethod
    def get_passengers() -> dict:
        return db.get_passengers()

    @staticmethod
    def update_passenger(passenger: dict, passenger_id: int) -> None:
        return db.update_passenger(passenger, passenger_id)

    @staticmethod
    def delete_passenger(passenger_id: int) -> None:
        return db.delete_passenger(passenger_id)

    @staticmethod
    def create_table():
        return db.create_table()

    @staticmethod
    def delete_table():
        return db.delete_table()
