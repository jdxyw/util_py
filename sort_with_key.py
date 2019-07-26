# Sometime, we need sort a list whose item type is a class.

import operator

# sort in place
spec_list.sort(key=operator.attrgetter('attr'))

# sort a dictionay and not in place
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
