# Import necessary modules and functions from other modules
from app.data_processing.ssh_prompt_handler.dictionary_converter import (
    get_ont_info_dictionaries,
)
from app.data_processing.db_handler.query_history import find_query_in_range, new_query
from datetime import datetime
from pytz import timezone
from re import sub


# Define a function for formatting the time
def format_time(date_time, new_query):
    """
    Format the given date and time to a specific time zone (Buenos Aires) and optionally adjust the hour.

    Args:
        date_time (datetime): The date and time to format.
        new_query (bool): A flag indicating whether it's a new query.

    Returns:
        str: The formatted time in "HH:MM" format.
    """
    # Define the time zone for Buenos Aires
    bsas_timezone = timezone("America/Argentina/Buenos_Aires")

    # Convert the input date_time to the Buenos Aires time zone
    date_time_with_tz = date_time.astimezone(bsas_timezone)

    # Checks if it is not a new query since the new queries are already date-time formatted
    if not new_query:
        # Calculate the time shift and adjust the hour
        # Extract the time zone offset from the 'date_time_with_tz' and convert it to an integer.
        time_shift = int(sub(r"0+$", "", date_time_with_tz.strftime("%z")))

        # Get the time in "HH:MM" format from 'date_time_with_tz'.
        time = date_time_with_tz.strftime("%H:%M")

        # Split the 'time' into hours and minutes, creating a list called 'hours_minutes'.
        hours_minutes = time.split(":")

        # Calculate the adjusted hour by adding 'time_shift' to the original hour value.
        hour = int(hours_minutes[0]) + time_shift

        # Create a formatted time string by combining the adjusted hour and the original minutes.
        time_formatted = str(hour) + ":" + hours_minutes[1]

    else:
        # Get the time in "HH:MM" format
        time_formatted = date_time_with_tz.strftime("%H:%M")

    return time_formatted


# Define a function to convert a query into a dictionary for display
def convert_query_to_show(query, items_to_show, new_query):
    """
    Convert a query result into a dictionary with formatted date, time, and relevant information.

    Args:
        query (dict): The query result containing date_time and ont_info.
        items_to_show (list): A list of specific items to display.
        new_query (bool): A flag indicating whether it's a new query.

    Returns:
        str: The formatted date.
        str: The formatted time.
        dict: A dictionary containing relevant information based on items_to_show.
    """
    date_time = query["date_time"]
    date = date_time.strftime("%d/%m/%Y")
    time = format_time(date_time, new_query)
    dictionary_to_show = {**query["ont_info"][0], **query["ont_info"][1]}

    if items_to_show is not None:
        # Filter the dictionary to include only specified items to show
        dictionary_to_show = dict(
            filter(lambda item: item[0] in items_to_show, dictionary_to_show.items())
        )

    return date, time, dictionary_to_show


# Define a function to update the queries
def query_refresh(
        olt_ip_introduced, ont_sn_introduced, items_to_show=None, debug_mode=False
):
    """
    Update the queries by creating a new one for a specific OLT IP and ONT serial number.

    Args:
        olt_ip_introduced (str): The OLT IP address.
        ont_sn_introduced (str): The ONT serial number.
        items_to_show (list): A list of specific items to display (optional).
        debug_mode (bool): A flag for debugging mode (optional).

    Returns:
        tuple: A tuple containing date (str), time (str), and a dictionary of relevant information.
    """
    query = new_query(olt_ip_introduced, ont_sn_introduced, debug_mode)
    data_to_show = convert_query_to_show(query, items_to_show, True)
    return data_to_show


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
        data_to_show = convert_query_to_show(query, items_to_show, True)
    else:
        data_to_show = convert_query_to_show(old_query_in_range, items_to_show)

    return data_to_show
