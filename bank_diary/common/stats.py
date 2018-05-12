from collections import defaultdict


def getAggFunc(name):
    return {
        'sum': lambda l: sum([r.amount for r in l]),
        'income': lambda l: sum([r.amount if r.amount > 0 else 0 for r in l]),
        'expense': lambda l: sum([-r.amount if r.amount < 0 else 0 for r in l]),
        'count': lambda l: len(l)
    }.get(name, None)


def aggregate(recs, target='sum', group_by=['category']):
    sets = defaultdict(lambda: [])

    for rec in recs:
        key = ""
        for elem in group_by:
            if hasattr(rec, elem):
                key += "-{}".format(getattr(rec, elem))
            else:
                raise Exception("unknown attribute: '{}'".format(group_by))

        sets[key[1:]].append(rec)

    func = getAggFunc(target)
    if func is None:
        raise Exception("unknown aggregate function: '{}'".format(target))

    res = ""
    for key, recs in sets.items():
        res += "{}: {:.2f}\n".format(key, func(recs))

    return res
