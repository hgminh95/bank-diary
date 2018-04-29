from collections import defaultdict


def getAggFunc(name):
    return {
        'sum': lambda l: sum([r.amount for r in l]),
        'count': lambda l: len(l)
    }.get(name, None)


def aggregate(recs, target='sum', group_by='category'):
    sets = defaultdict(lambda: [])

    for rec in recs:
        if hasattr(rec, group_by):
            key = getattr(rec, group_by)
        else:
            raise Exception("unknown attribute: '{}'".format(group_by))
        sets[key].append(rec)

    func = getAggFunc(target)
    if func is None:
        raise Exception("unknown aggregate function: '{}'".format(target))

    res = {}
    for key, recs in sets.items():
        res[key] = func(recs)

    return res
