import json
def isjson_data(data):
    try:
        p_data = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid
