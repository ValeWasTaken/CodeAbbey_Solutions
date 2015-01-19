import collections; print (' '.join(sorted([x for x, y in collections.Counter(raw_input().split()).items() if y > 1])))
