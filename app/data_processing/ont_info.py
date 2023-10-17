from app.data_processing.ssh_prompt_handler.dictionary_converter import get_ont_info_dictionaries
from app.data_processing.db_handler.query_history import find_query_in_range, new_query
from datetime import datetime
from pytz import timezone


# def get_ont_info_to_show(olt_ip_introduced, ont_sn_introduced, items_to_show=None, debug_mode=False):
#     ont_info_dic, ont_optical_info_dic = get_ont_info_dictionaries(olt_ip_introduced, ont_sn_introduced, debug_mode)
#     dictionary_to_show = {**ont_info_dic, **ont_optical_info_dic}
#     if items_to_show is not None:
#         dictionary_to_show = dict(filter(lambda item: item[0] in items_to_show, dictionary_to_show.items()))
#     return dictionary_to_show

# 2023-10-14 19:35:23.120220+00:00

def format_time(date_time):
    bsas_timezone = timezone("America/Argentina/Buenos_Aires")
    date_time_with_tz = date_time.astimezone(bsas_timezone)
    time = date_time_with_tz.strftime("%H:%M")
    parts = time.split(":")
    hour = int(parts[0]) + int(date_time.strftime("%z"))
    time_formatted = str(hour) + ":" + parts[1]
    return time_formatted


def convert_query_to_show(query, items_to_show):
    date_time = query['date_time']
    date = date_time.strftime("%d/%m/%Y")
    time = format_time(date_time)
    dictionary_to_show = {**query['ont_info'][0], **query['ont_info'][1]}
    if items_to_show is not None:
        dictionary_to_show = dict(filter(lambda item: item[0] in items_to_show, dictionary_to_show.items()))
    return date, time, dictionary_to_show


def new_request(olt_ip_introduced, ont_sn_introduced, items_to_show=None, debug_mode=False):
    data_to_show = None

    old_query_in_range = find_query_in_range(olt_ip_introduced, ont_sn_introduced)
    if old_query_in_range is None:
        query = new_query(olt_ip_introduced, ont_sn_introduced, debug_mode)
        data_to_show = convert_query_to_show(query, items_to_show)
    else:
        pass

    return data_to_show
