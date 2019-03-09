# A decorator to cache function results - implemented using LRU with
# a cyclic double-ended queue modelled using python lists.
# Cache hits and item removal both take O(1) time in this implementation.

types = [int, str, frozenset, type(None)]
def create_key(args):
    key = args
    if len(key) == 1 and type(key[0]) in types:
        return key[0]
    else:
        return hash(tuple(args))

stats = [0, 0]

def lru_cache(func):

    maxsize = 100
    cache = {}
    root = []
    HITS, MISSES = 0, 1
    root[:] = [root, root, None, None]
    nonlocal_root = [root]
    NEXT, PREV, KEY, RESULT = 0,1,2,3

    def wrapper(*args, **kwargs):
        key = create_key(args)
        node = cache.get(key)
        if node is not None:
            root, = nonlocal_root
            node_next, node_prev, key, result = node
            # Slice the node from its original position
            node_next[PREV] = node_prev
            node_prev[NEXT] = node_next
            last = root[PREV]
            # Put the node at the front
            last[NEXT] = root[PREV] = node
            node[NEXT] = root
            node[PREV] = last
            stats[HITS] += 1
            return result
        result = func(*args, **kwargs)
        root, = nonlocal_root
        if len(cache) >= maxsize:
            oldroot = root
            oldroot[KEY] = key
            oldroot[RESULT] = result
            root = nonlocal_root[0] = oldroot[NEXT]
            
            # Prepar root[NEXT] (last element) for deletion
            oldkey = root[KEY]
            oldval = root[RESULT]
            root[KEY] = root[RESULT] = None
            # Delete the last node in the queue
            del cache[oldkey]
            cache[key] = oldroot

        else:
            last = root[PREV]
            node = [root, last, key, result]
            last[NEXT] = root[PREV] = cache[key] = node
        stats[MISSES] += 1

        return result
    return wrapper

# Fib used as an example case for memoization with this lru decorator.
# Ideally it would be used for functions in need of memoization that are
# called often enough that a hashtable would be considered inefficient space-wise
# (e.g.) in large DB calls
@lru_cache
def fib(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

