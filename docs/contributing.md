# Contributing

## Read the [Program Structure](./program-structure.md)

## Read the [Glossary](./glossary.md) to understand technical concepts

## Good Practices

### Always Comment the Code

Comments should be oriented towards developers who are not familiar with specific tools such as pexpect or specific terms like OLT, but to Python developers in general, as shown in the following example:

```python
# Define a function for making a new request
def new_request(
        olt_ip_introduced, ont_sn_introduced, items_to_show=None, debug_mode=False
):
    """
    Make a new request for a specific OLT IP and ONT serial number.

    Args:
        olt_ip_introduced (str): The OLT IP address.
        ont_sn_introduced (str): The ONT serial number.
        items_to_show (list): A list of specific items to display (optional).
        debug_mode (bool): A flag for debugging mode (optional).

    Returns:
        tuple: A tuple containing date (str), time (str), and a dictionary of relevant information.
    """
    data_to_show = None

    old_query_in_range = find_query_in_range(olt_ip_introduced, ont_sn_introduced)
    if old_query_in_range is None:
        query = new_query(olt_ip_introduced, ont_sn_introduced, debug_mode)
        data_to
        show = convert_query_to_show(query, items_to_show, True)
    else:
        data_to_show = convert_query_to_show(old_query_in_range, items_to_show)

    return data_to_show
```

> Taken from [ont_info.py](../app/data_processing/ont_info.py)

### Naming

We are following the [PEP8 standards](https://peps.python.org/pep-0008/) for naming variables, functions, modules, etc.

### Variable Naming

#### Snake Case

Snake case means that words are separated by an underscore, and everything is lowercase, for example:

- `banana_seeds`
- `cave_hanging_stalactites`

The only exception to this rule is [environmental variables](../.env.example), which follow screaming case with
underscore separation:

- `BANANA_SEEDS`
- `CAVE_STALACTITES`

#### Verbosity

**Common/small abbreviations** are allowed but should be added to the [glossary](./glossary.md):

- `authentication` => `auth`
- `cooperation` => `coop`
- `error` => `err`

Normal variables should be **self-explanatory** and fairly detailed. If there is a commonly known acronym (such as IP,
MAC, URL) or the acronym will be used throughout the code (such as URI, SN, or OLT), then use it and add it to
the [glossary](./glossary.md) if it's not already there. Otherwise, do not use acronyms and use the self-explanatory
full name, like in the following examples:

> I have to create a new variable that will contain a string describing the Optical Node Terminal use case. This term is
> used throughout the code and has the acronym ont/ONT (and is already being used as the acronym), so the name should be:

```python
ont_use_case = "drink pineapples"
# Short and simple
```

> I have to create a new variable that will contain a string that tells us the result of a Challenge Handshake
> Authentication Protocol (CHAP) attempt. This is the only part of the code in which it will be used, and it is a specific
> acronym that not many people know, so the name should be:

```python
challenge_handshake_authentication_protocol_result = ""
# Quite long, but now most people will understand it.
```

#### Function Variable Naming

Ideally, variables that are part of a function should have a name related to their task within the function before their
name. Take the following function, for example:

```python
def useless_function(input_ip_mask):
    print(input_ip_mask)
    return_ip_mask = "255.255.255.255"
    return_ip_address = "8.8.8.8"
    return return_ip_mask, return_ip_address
# The important parts here are "return" and "input," as well as the distinction between IP mask and address.
```