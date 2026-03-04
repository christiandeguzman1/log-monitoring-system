def print_alert(incident):
    """
    Print a formatted alert to the console.
    Expects a dictionary with keys: type, message, and optionally timestamp.
    """
    timestamp = incident.get("timestamp", "N/A")
    alert_type = incident.get("type", "UNKNOWN")
    message = incident.get("message", "")
    print(f"[{timestamp}] ALERT ({alert_type}): {message}")
