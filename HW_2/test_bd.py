import sqlite3
from faker import Faker
import pytest

fake = Faker()


class TestExample:
    def setup_class(self):
        self.connection = sqlite3.connect("db.sqlite")
        self.cursor = self.connection.cursor()

    @pytest.mark.parametrize("name", [fake.first_name() for i in range(100)])
    def test_id_user_exists(self, name):

        users = self.cursor.execute("select * from users").fetchall()
        print(users)

        for user in users:
            if name in user:
                return "super good"
        else:
            raise Exception(f"user {name} not found")

    def teardown_class(self):
        self.connection.close()
