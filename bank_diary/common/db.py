import os
import sqlite3

from .models import Transaction


class SQLiteDatabase(object):

    def __init__(self, path='example.db'):
        if os.path.exists(path):
            self.conn = sqlite3.connect('example.db')
        else:
            self.conn = sqlite3.connect('example.db')
            self.initialize_db()

    def initialize_db(self):
        c = self.conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS trans(
                date text,
                statement_code text,
                ref text,
                amount real,
                client_ref text)''')

        self.conn.commit()
        c.close()

    def insert_one(self, transaction):
        c = self.conn.cursor()

        c.execute(self._insert_one_cmd(transaction))

        self.conn.commit()
        c.close()

    def insert_bulk(self, transactions):
        c = self.conn.cursor()

        c.execute(self._insert_bulk_cmd(transactions))

        self.conn.commit()
        c.close()

    def select_all(self):
        return _select("SELECT * FROM trans")

    def select_period(self, prefix):
        return self._select("SELECT * FROM trans WHERE date LIKE '{}%'".format(prefix))

    def _select(self, cmd):
        c = self.conn.cursor()

        c.execute(cmd)

        return self._populate_all(c.fetchall())

    def _insert_one_cmd(self, transaction):
        return self._insert_bulk_cmd([transaction])

    def _insert_bulk_cmd(self, transactions):
        if len(transactions) == 0:
            return ""

        cmd = "INSERT INTO trans VALUES"
        cmd += self._values_of(transactions[0])

        for trans in transactions[1:]:
            cmd += ", " + self._values_of(trans)

        return cmd

    def _values_of(self, trans):
        return "('{}', '{}', '{}', {}, '{}')".format(
            trans.date.strftime('%Y%m%d'),
            self._escape(trans.statement_code),
            self._escape(trans.reference),
            trans.amount,
            self._escape(trans.client_ref))

    def _escape(self, s):
        return s.replace("'", "''")

    def _populate_one(self, record):
        return Transaction(*record)

    def _populate_all(self, records):
        return [self._populate_one(record) for record in records]
