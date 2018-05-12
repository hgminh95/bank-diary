import re


class Tokenizer:

    TOKEN_REGEXS = '|'.join([
        '[A-Za-z0-9]+',
        ',',
        '='
    ])

    def tokenize(self, line):
        return re.findall(self.TOKEN_REGEXS, line)


class Parser:

    def parse_line(self, tokens):
        self.tokens = tokens
        self.pos = 0

        try:
            cmd = self.next_str()
            if cmd == 'get':
                return True, self.parse_get_command()
            elif cmd == 'list':
                return True, self.parse_list_command()
        except Exception as e:
            return False, e

    def parse_list_command(self):
        period = ''
        conds = []
        while True:
            if self.peek() is None:
                break
            keyword = self.next_str()

            if keyword == 'at':
                period = self.next_str()
            elif keyword == 'where':
                conds = self.parse_list_cond()
            else:
                raise Exception('unknown keyword in list: "{}"'.format(keyword))

        return "LIST", (conds, period)

    def parse_get_command(self):
        target = self.next_str()
        self.expect_str('by')
        group_by = self.parse_list_string()
        period = ''
        if self.peek() is not None:
            self.expect_str('at')
            period = self.next_str()

        return "GET", (target, group_by, period)

    def parse_list_string(self):
        res = []
        while True:
            res.append(self.next_str())
            if self.peek() != ',':
                break
            else:
                self.pos += 1
        return res

    def parse_list_cond(self):
        res = []
        while True:
            field = self.next_str()
            self.expect_str('=')
            value = self.next_str()
            res.append((field, value))
            if self.peek() != ',':
                break
            else:
                self.pos += 1
        return res

    def next_str(self):
        res = self.pop()
        if res is None:
            raise Exception('expect string, but found nothing')
        return res

    def expect_str(self, expect):
        real = self.pop()

        if expect != real:
            raise Exception('expect "{}", but found "{}"'.format(expect, real))

    def peek(self):
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]

    def pop(self):
        if self.pos >= len(self.tokens):
            return None
        self.pos += 1
        return self.tokens[self.pos - 1]
