from collections import namedtuple
from itertools import product

NUMS = map(str, range(1, 14))
COLS = 'ORBU'
VERS = 'ab'

Tile = namedtuple('Tile', 'num_s col ver')
Tile.num = property(lambda s: int(s.num_s) if s.num_s != 'J' else s.num_s)
Tile.__str__ = lambda s: ''.join(s)
Tile.__repr__ = lambda s: ''.join(s)

TILES = list(Tile(*parts) for parts in product(NUMS, COLS, VERS)) +\
        [Tile('J', 'J', ver) for ver in VERS]

def strs_to_tiles(*strs):
    return [Tile(s[:-2], s[-2], s[-1]) for s in strs]

def valid_group(group):
    return valid_set(group) or valid_run(group)

def valid_set(group):
    # Sets can only have 3 or 4 elements
    if len(group) not in (3, 4):
        return False
    # Cannot have more than one number in a set
    if len(set(t.num for t in group if t.num != 'J')) > 1:
        return False
    # Colours cannot be repeated
    cols = [t.col for t in group if t.col != 'J']
    if len(cols) != len(set(cols)):
        return False
    return group

def valid_run(group):
    # Runs must have at least 3 elements
    if len(group) < 3:
        return False
    # Cannot have more than one col in a run
    if len(set(t.col for t in group if t.col != 'J')) > 1:
        return False
    jokers = [t.num for t in group if t.num == 'J']
    nums = {t.num: t for t in group if t.num != 'J'}
    # Cannot have duplicate numbers in a run
    if len(group) != len(jokers) + len(nums):
        return False
    run = []
    for n, m in zip(nums.keys()[:-1], nums.keys()[1:]):
        run.append(nums[n])
        # If there are any gaps, plug holes with jokers
        for _ in range(m - n - 1):
            # If we have more gaps than jokers, invalid run
            if not jokers:
                return False
            run.append(jokers.pop())
    run.append(nums[m])
    # If we have jokers left over, tack onto the end if possible
    min_num, max_num = run[0].num, run[-1].num
    while jokers:
        if min_num > 1:
            min_num -= 1
            run.insert(0, jokers.pop())
            continue
        if max_num < 13:
            max_num += 1
            run.append(jokers.pop())
            continue
        return False
    return run
