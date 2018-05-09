from datetime import datetime

from .base import BaseParser
from bank_diary.common.models import Transaction


class DbsParser(BaseParser):

    _name = 'dbs'

    def __init__(self):
        pass

    def parse_file(self, path):
        with open(path, 'rt') as f:
            in_data_area = False
            for line in f:
                if "Transaction Date" in line:
                    in_data_area = True
                    continue

                if not in_data_area:
                    continue

                tokens = line.replace('\n', '').split(",")
                if len(tokens) < 10:
                    continue

                yield self.parse_line(tokens)

    def parse_line(self, tokens):
        t = Transaction(
            "",
            datetime.strptime(tokens[0], "%d %b %Y"),
            tokens[2],
            tokens[3],
            - float(tokens[4]) if tokens[4] != " " else float(tokens[5]),
            tokens[6]
        )

        return t
