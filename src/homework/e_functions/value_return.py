def get_hour(epoch_seconds):
    return epoch_seconds // 3600

def get_minutes(epoch_seconds):
    return (epoch_seconds // 60) % 60

def get_seconds(epoch_seconds):
    return epoch_seconds % 60

def time_from_utc(utc_offset, utc_zero):
    sum = utc_offset + utc_zero 
    return  sum % 24