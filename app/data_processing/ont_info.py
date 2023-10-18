from app.data_processing.ssh_prompt_handler.dictionary_converter import get_ont_info_dictionaries
from app.data_processing.db_handler.query_history import find_query_in_range, new_qry
from datetime import datetime
from pytz import timezone
from re import sub


def format_time(date_time, new_qry):
    bsas_timezone = timezone("America/Argentina/Buenos_Aires")
    date_time_with_tz = date_time.astimezone(bsas_timezone)
    if not new_qry:
        time_shift = int(sub(r'0+$', '', date_time_with_tz.strftime("%z")))
        time = date_time_with_tz.strftime("%H:%M")
        parts = time.split(":")
        hour = int(parts[0]) + time_shift
        time_formatted = str(hour) + ":" + parts[1]
    else:
        time_formatted = date_time_with_tz.strftime("%H:%M")
    return time_formatted


def convert_query_to_show(query, items_to_show, new_qry=False):
    date_time = query['date_time']
    date = date_time.strftime("%d/%m/%Y")
    time = format_time(date_time, new_qry)
    dictionary_to_show = {**query['ont_info'][0], **query['ont_info'][1]}
    if items_to_show is not None:
        dictionary_to_show = dict(filter(lambda item: item[0] in items_to_show, dictionary_to_show.items()))
    return date, time, dictionary_to_show


def query_refresh(olt_ip_introduced, ont_sn_introduced, items_to_show=None, debug_mode=False):
    query = new_qry(olt_ip_introduced, ont_sn_introduced, debug_mode)
    data_to_show = convert_query_to_show(query, items_to_show, True)
    return data_to_show


def new_request(olt_ip_introduced, ont_sn_introduced, items_to_show=None, debug_mode=False):
    data_to_show = None

    old_query_in_range = find_query_in_range(olt_ip_introduced, ont_sn_introduced)
    if old_query_in_range is None:
        query = new_qry(olt_ip_introduced, ont_sn_introduced, debug_mode)
        data_to_show = convert_query_to_show(query, items_to_show, True)
    else:
        data_to_show = convert_query_to_show(old_query_in_range, items_to_show)

    return data_to_show
