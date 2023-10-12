from re import findall, sub, split


def get_dictionary_from_prompt(table_prompt):
    REGEX_PATTERN = r"\s{2}([^\s][^:\n]*\S)\s*:\s*([^\n]*\S)[^\n]*"

    dictionary = {}

    matches = findall(REGEX_PATTERN, table_prompt)

    for name, value in matches:
        parts = name.lower().split('\x1b[37d', 1)
        key = parts[-1].lstrip()
        dictionary[key.strip().lower()] = value.strip().lower()

    return dictionary
