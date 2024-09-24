def format_response(data, message=None, success=True):
    response = {
        "success": success,
        "data": data,
    }
    if message:
        response["message"] = message
    return response

def handle_error(message):
    return format_response(None, message, success=False)
