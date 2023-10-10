from re import findall


def get_dictionary_from_table(table_prompt):
    REGEX_PATTERN = r"\s{2}([^\s][^:\n]*\S)\s*:\s*([^\n]*\S)[^\n]*"

    dictionary = {}

    matches = findall(REGEX_PATTERN, table_prompt)

    for name, value in matches:
        dictionary[name.strip()] = value.strip()

    return dictionary