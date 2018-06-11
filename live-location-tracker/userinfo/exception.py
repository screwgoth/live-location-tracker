from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    response = exception_handler(exc, context)
    print(response,"<--------")
    message = "Error Occurred"
    if response:
        error_fields = list(response.data.keys())
        if error_fields:
            message = response.data[error_fields[0]]
        # Now add the HTTP status code to the response.
        if response is not None:
            response = delete_response(response)
            response.data['status_code'] = response.status_code
            response.data["message"] = message
    return response


def delete_response(response):
    """ This  method delete response data that genretes by DRF because we are creating custom response.
        It only deletes the data attribute of the response
    """
    for i in list(response.data.keys()):
        del response.data[i]

    return response
