from datetime import datetime

def convert_to_24hr(time_str: str):
    return datetime.strptime(time_str, "%I:%M %p").time()