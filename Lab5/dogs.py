from peewee import *

db = SqliteDatebase('cats.sqlite')

class Dog(model):
    name = CharField()
    color = CharField()
    