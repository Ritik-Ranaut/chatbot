def compute_lps(pattern):
    """Computes the Longest Prefix Suffix (LPS) array for KMP algorithm."""
    lps = [0] * len(pattern)
    length, i = 0, 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps

def kmp_search(text, pattern):
    """Implements KMP Algorithm for pattern matching."""
    lps = compute_lps(pattern)
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return True
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return False
