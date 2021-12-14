def timezone(hour,timezone):
    new_hour = (hour+timezone)
    if new_hour < 0: new_hour = new_hour+24
    elif new_hour > 23: new_hour = new_hour-24
    return new_hour
