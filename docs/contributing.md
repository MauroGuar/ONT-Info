# Contributing

## read [The program structure](./program-structure.md)

## read the [glossary](./glossary.md) to understand technical concepts

## Good practices

### Always comment the code

the comments must be oriented to devs, not devs familiarized with the specific tools such as pexpect or specific terms as OLT, but to python devs in general, as the following example:

``` python
# Define a function for making a new request and retrieving data
def new_request(
    olt_ip_introduced, ont_sn_introduced, items_to_show=None, debug_mode=False
):
    """
    Make a new request and retrieve data for a specific OLT IP and ONT serial number.

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
        query = new_qry(olt_ip_introduced, ont_sn_introduced, debug_mode)
        data_to_show = convert_query_to_show(query, items_to_show, True)
    else:
        data_to_show = convert_query_to_show(old_query_in_range, items_to_show)

    return data_to_show
```

>Taken from [ont_info.py](../app/data_processing/ont_info.py)

### Variable naming

#### Snake case

Snake case means that words are separated by an underscore, and everything is lowercase, for example:

* banana_seeds
* cave_hanging_stalactites

the only exception to this are the [enviromental variables](../.env.example) , which follow the Screaming case with underscore separation:

* BANANA_SEEDS
* CAVE_STALACTITES

#### Verbosity

**common/small abbreviations** are allowed but shall be added to the [glossary](./glossary.md):

* authentication => auth
* coopeartion => coop
* error => err

normal variables should be **self-explanatory** and fairly detailed, if there is a commonly known acronym (such as IP, MAC, URL) or the acronym will be used in all or much of the code (such as URI, SN, or OLT), then use it and add it to the [glossary](./glossary.md) if it's not there already , otherwise , do not use acronyms and use the self-explanatory full name like the following example:

>I have to create a new variable that will contain a string describing the Optical Node Tetminal use case, this is a term used throughout the code and has the acronym ont/ONT (and is already being used as the acronym), so the name shall be:

```python 
ont_use_case = "drink pineapples"
# short and simple
```

>I have to create a new variable which will contain a string that tell's us the result of a challenge handshake authentication protocol(CHAP) attempt, this is the only part of the code in which it will be used, and is a really specific acronym not many people know, so the name shall be:

```python
challenge_handshake_authentication_protocol_result = ""
# quite long isn't it? but now most people will understand it. 
```

#### Function's variable naming

Optimally, Variables that are part of a function should have a name related to their task within the function before their name, take the next function for example:

```python
def useless_function(input_ip_mask):
    print(input_ip_mask)
    return_ip_mask = "255.255.255.255"
    return_ip_address = "8.8.8.8"
    return return_ip_mask, return_ip_address
# return and input are the important parts here, also the distinction between ip mask and address.
```