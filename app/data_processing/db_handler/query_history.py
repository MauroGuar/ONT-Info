# Import necessary modules and functions
from flask_pymongo import DESCENDING
from datetime import datetime, timedelta, timezone
from app.database.connection import MongoConnection
from app.data_processing.ssh_prompt_handler.dictionary_converter import get_ont_info_dictionaries


# Define a function to create an example JSON object
def example_json():
    """
    Create and return an example JSON object containing ONT information.

    Returns:
        dict: Example JSON object.
    """
    json = {
        "olt_ip": "172.17.254.45",
        "ont_sn": "48575443655C13A0",
        "date_time": datetime.datetime.now(tz=datetime.timezone.utc),
        "ont_info": [
            {
                "f/s/p": "0/3/0",
                "ont-id": "1",
                "control flag": "active",
                "run state": "online",
                "config state": "normal",
                "match state": "match",
                "dba type": "sr",
                "ont distance(m)": "12",
                "ont last distance(m)": "-",
                "ont battery state": "not support",
                "memory occupation": "29%",
                "cpu occupation": "1%",
                "temperature": "59(c)",
                "authentic type": "sn-auth",
                "sn": "48575443655c13a0 (hwtc-655c13a0)",
                "management mode": "omci",
                "software work mode": "normal",
                "isolation state": "normal",
                "ont ip 0 address/mask": "-",
                "description": "ont_no_description",
                "last down cause": "-",
                "last up time": "2023-10-05 03:06:37+08:00",
                "last down time": "-",
                "last dying gasp time": "-",
                "ont online duration": "6 day(s), 1 hour(s), 22 minute(s), 3 second(s)"
            },
            {
                "onu nni port id": "0",
                "module type": "10g gpon",
                "module sub-type": "n1/n2a/e1/e2a",
                "used type": "onu",
                "encapsulation type": "bosa on board",
                "optical power precision(dbm)": "3.0",
                "vendor name": "huawei",
                "vendor rev": "-",
                "vendor pn": "hw-bob-0004",
                "vendor sn": "1817e0052872u",
                "date code": "19-05-14",
                "rx optical power(dbm)": "-15.14",
                "rx power current warning threshold(dbm)": "[-,-]",
                "rx power current alarm threshold(dbm)": "[-29.0,-8.0]",
                "tx optical power(dbm)": "3.74",
                "tx power current warning threshold(dbm)": "[-,-]",
                "tx power current alarm threshold(dbm)": "[0.0,6.0]",
                "laser bias current(ma)": "11",
                "tx bias current warning threshold(ma)": "[-,-]",
                "tx bias current alarm threshold(ma)": "[0.000,90.000]",
                "temperature(c)": "48",
                "temperature warning threshold(c)": "[-,-]",
                "temperature alarm threshold(c)": "[-10,80]",
                "voltage(v)": "3.240",
                "supply voltage warning threshold(v)": "[-,-]",
                "supply voltage alarm threshold(v)": "[3.000,3.600]",
                "olt rx ont optical power(dbm)": "-15.63"
            }
        ]
    }
    return json


# Define a function to calculate the maximum date-time range
def maximum_date_time_range(hours_range=24):
    """
    Calculate the maximum date-time range.

    Args:
        hours_range (int): Number of hours to subtract from the current date and time.

    Returns:
        datetime: Maximum date-time within the specified range.
    """
    return datetime.now() - timedelta(hours=hours_range)


# Define a function to create and save a new query document
def new_query(olt_ip, ont_sn, debug_mode):
    """
    Create a new query document and save it in the queries MongoDB collection.

    Args:
        olt_ip (str): OLT IP address.
        ont_sn (str): ONT serial number.
        debug_mode (bool): Debug mode flag.

    Returns:
        dict: JSON object representing the saved query document.
    """
    qry_col = MongoConnection().get_queries_collection()
    ont_info_dic, ont_optical_info_dic = get_ont_info_dictionaries(olt_ip, ont_sn, debug_mode)
    json_to_save = {
        "olt_ip": olt_ip,
        "ont_sn": ont_sn,
        "date_time": datetime.now(tz=timezone.utc),
        "ont_info": [ont_info_dic, ont_optical_info_dic]
    }
    qry_col.insert_one(json_to_save)
    return json_to_save


# Define a function to find the most recent query document within a date-time range
def find_query_in_range(olt_ip, ont_sn):
    """
    Find the most recent query document for a specific OLT IP and ONT serial number within a date-time range.

    Args:
        olt_ip (str): OLT IP address.
        ont_sn (str): ONT serial number.

    Returns:
        dict or None: The most recent query document if found, or None if no document matches the criteria.
    """
    qry_col = MongoConnection().get_queries_collection()
    doc_matches = list(qry_col.find(
        {"olt_ip": olt_ip, "ont_sn": ont_sn, "date_time": {"$gte": maximum_date_time_range()}}).sort(
        [("date_time", DESCENDING)]).limit(1))
    if len(doc_matches) > 0:
        return doc_matches[0]
    return None
