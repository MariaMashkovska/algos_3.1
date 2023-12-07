def bad_characters(pattern):
    if not pattern:
        return "No data"

    M = len(pattern)
    map = [-1] * 256

    for j in range(M):
        map[ord(pattern[j])] = j

    return map


def boyer_moore(string, pattern, bad_char_map):
    M = len(pattern)
    N = len(string)
    res = []

    if not pattern or not string:
        return "Put some letters"

    i = 0
    while i <= N - M:
        skip = 0
        j = M - 1

        while j >= 0:
            if pattern[j] != string[i + j]:
                skip = max(1, j - bad_char_map[ord(string[i + j])])
                break
            j -= 1

        if skip == 0:
            res.append(i)
            skip = 1

        i += skip

    return res


string = "Hello Victoria Secret"
pattern = "Victoria"

bad_char_map = bad_characters(pattern)
result = boyer_moore(string, pattern, bad_char_map)

print(result)
