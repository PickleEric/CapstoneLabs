import unittest
from unittest import TestCase

import sqlite3


from sqlite_db.config import db

from model import *

test_db = 'test_catalog.sqlite'

db = test_db


class TestDB(TestCase):

    def test_setup(self):

        db.create_table()

        with sqlite3.connect('test_catalog.sqlite') as conn:
            conn.execute('DELETE FROM artist')
        conn.close()
    
    def test_add_artist(self):
        fake_artist = Artist('Jon Louis', 'Jlouis@gmail.com')
        added = db.create_new_artist(fake_artist)

        self.assertTrue(added)

        expected_row = [('Jon Louis', 'Jlouis@gmail.com')]
        actual_row = self.get_all_data()

        self.assertCountEqual(expected_row, actual_row)

        fake_artist0 = Artist('Lisa Truely', 'Ltruely@gmail.com')
        added0 = db.create_new_artist(fake_artist0)

        self.assertTrue(added0)

        expected_row = [('Lisa Truely', 'Ltruely@gmail.com')]
        actual_row = self.get_all_data()

        self.assertCountEqual(expected_row, actual_row)

    def test_add_artwork(self):
        fake_artwork = Artwork('Jon Louis', 'The Mask', 400, True)
        added = db.create_new_artwork(fake_artwork)

        self.assertTrue(added)

        expected_row = [('Jon Louis', 'The Mask', 400, True)]
        actual_row = self.get_all_data()

        self.assertCountEqual(expected_row, actual_row)

        fake_artist0 = Artwork('Lisa Truely', 'The Fountain', 250, False)
        added0 = db.create_new_artwork(fake_artist0)

        self.assertTrue(added0)

        expected_row = [('Lisa Truely', 'The Fountain', 250, False)]
        actual_row = self.get_all_data()

        self.assertCountEqual(expected_row, actual_row)

    def get_all_data(self):
        with sqlite3.connect('test_catalog.sqlite') as conn:
            rows = conn.execute('SELECT * FROM artists').fetchall()
        conn.close()
        return rows

if __name__ == '__main__':
    unittest.main()
