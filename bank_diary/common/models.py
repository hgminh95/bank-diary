class Transaction:

    def __init__(self):
        self.date = None
        self.statement_code = None
        self.reference = None
        self.amount = None
        self.client_ref = None

    def __str__(self):
        return "<Transaction,{},{},{},{},{}>".format(
            self.date.strftime("%Y%m%d"),
            self.statement_code,
            self.reference,
            self.amount,
            self.client_ref
        )
