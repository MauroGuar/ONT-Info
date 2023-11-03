from re import findall, sub, split


def get_dictionary_from_prompt(table_prompt):
    """
    Extracts key-value pairs from a given table prompt and returns them as a dictionary.

    Args:
        table_prompt (str): Input string containing the table prompt.

    Returns:
        dict: A dictionary containing extracted key-value pairs.
    """
    # Regular expression pattern to match key-value pairs in the table prompt
    # Define a regular expression pattern to match pairs of key-value data.
    REGEX_PATTERN = r"\s{2}([^\s][^:\n]*\S)\s*:\s*([^\n]*\S)[^\n]*"

    # Explanation:
    # The pattern is used to extract key-value pairs from text where keys and values are separated by colons.

    # r: Denotes a raw string literal in Python, which is used for regular expressions.

    # \s{2}: Matches exactly two whitespace characters (spaces or tabs). These are often used as indentation.

    # ([^\s][^:\n]*\S): This part matches the key.
    #   - [^\s]: Matches any character that is not a whitespace character (the start of the key).
    #   - [^:\n]*: Matches zero or more characters that are not colons (':') or newline characters.
    #   - \S: Matches any non-whitespace character (the end of the key).

    # \s*:\s*: Matches the colon and any surrounding whitespace characters that separate the key and the value.

    # ([^\n]*\S): This part matches the value.
    #   - [^\n]*: Matches zero or more characters that are not newline characters (the start of the value).
    #   - \S: Matches any non-whitespace character (the end of the value).

    # [^\n]*: This part is used to skip any characters that follow the value until the end of the line (newline character).

    # Overall, the pattern is designed to capture key-value pairs in text, where the keys and values may contain non-whitespace characters and colons. It allows for flexibility in formatting and handles leading and trailing spaces or tabs.

    # Example Usage:
    # Given the text "  Key  :  Value data here\n   AnotherKey :AnotherValue\n", the pattern would match:
    # - "Key" and "Value data here"
    # - "AnotherKey" and "AnotherValue"

    # Initialize an empty dictionary to store key-value pairs
    dictionary = {}

    # Find all matches using the regular expression pattern
    matches = findall(REGEX_PATTERN, table_prompt)

    # Iterate through the matches and extract key-value pairs
    for name, value in matches:
        # Split the name based on a specific delimiter and extract the last part as the key
        parts = name.lower().split("\x1b[37d", 1)
        key = parts[-1].lstrip()
        # Add the key-value pair to the dictionary (lowercase the key and value)
        dictionary[key.strip().lower()] = value.strip().lower()

    # Return the extracted key-value pairs as a dictionary
    return dictionary
