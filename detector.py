import re

def detect_anomaly(line):
    if re.search(r"ERROR", line):
        return {"type": "ERROR", "message": line}
    elif re.search(r"FAILED LOGIN", line):
        return {"type": "FAILED_LOGIN", "message": line}
    elif re.search(r"WARNING High memory", line):
        return {"type": "WARNING_HIGH_MEMORY", "message": line}
    else:
        return None