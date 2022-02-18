def get_options_ratio(options, total):
    return options / total

def get_faculty_rating(get_options_ratio):
    if get_options_ratio > .9 and get_options_ratio < 1:
        return "Excellent"
    if get_options_ratio > .8 and get_options_ratio < .9:
        return "Very Good"
    if get_options_ratio > .7 and get_options_ratio < .8:
        return "Good"
    if get_options_ratio > .6 and get_options_ratio < .7:
        return "Needs Improvement"
    if get_options_ratio > 0 and get_options_ratio < .6:
        return "Unacceptable"