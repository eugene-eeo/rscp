def _rotate(s):
    return s[-1] + s[:-1]


def _construct_lookup(s):
    """
    Constructs a lookup table t from a sorted string s,
    s.t. t[x] == s.index(x), but in linear time.
    """
    n = len(s)
    t = {}
    for i, ch in enumerate(s):
        if i > 0 and s[i-1] == ch:
            continue
        t[ch] = i
    return t


def transform(s):
    M = []
    r = s
    for _ in range(len(s)):
        M.append(r)
        r = _rotate(r)
    M.sort()
    i = M.index(s)
    l = "".join(x[-1] for x in M)
    return l, i


def untransform(l, i):
    f = "".join(sorted(l))
    T = []
    last = _construct_lookup(f)
    for ch in l:
        T.append(last[ch])
        # upon seeing ch again, we can look at previous index and
        # increment by 1 because f is sorted.
        last[ch] += 1

    r = []
    j = i
    for _ in range(len(l)):
        r.append(l[j])
        j = T[j]  # iterative T^{n+1}[x] = T[T^n[x]], avoid O(n^2) lookups.

    r.reverse()
    return "".join(r)
