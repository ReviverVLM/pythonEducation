def all_variants(text):
    def path_string(string, start, end):
        return string[start:end]

    for first in range(len(text) + 1):
        for second in range(len(text) + 1):
            if second > first:
                yield path_string(text, first, second)
