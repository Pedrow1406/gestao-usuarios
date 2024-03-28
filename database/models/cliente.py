from peewee import Model, CharField,DateField
from database.database import db
from datetime import date

class Cliente(Model):
    name = CharField(max_length=40)
    email = CharField(max_length=100, unique=True)
    data_registro = DateField(default=date.today())

    def __str__(self) -> str:
        return self.name
    class Meta:
        database = db