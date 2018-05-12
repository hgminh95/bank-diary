# bank diary

## Requirements

- Python 3

## Install

```
$ python3 setup.py
```

## Usage

```
$ bdiary
Welcome to bdiary shell. Type help or ? to list commands.

(diary) import report.csv
Import 256 new transactions.

(diary) list 201804
Found 2 transactions.
> <Transaction, xxx, yyy, zzz, ...>
> <Transaction, xxx, yyy, zzz, ...>

(diary) get sum by category at 201804
food: xxx
housing: yyy
transport: zzz

(diary) get sum by year, month
2018-03: xxx
2018-04: yyy
2018-05: zzz
```

## Customization

### Write your own classifier

See `bank_diary/defaults.py` for more details.

## Limitation

Only work with DBS.

## License

MIT.
