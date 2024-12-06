import logging

def function_cicd(request):
    # Log the incoming request details for debugging
    logging.info('Request received: %s', request)
    logging.info('Request Headers: %s', request.headers)
    
    # Check for query parameters (GET request)
    if request.args and 'message' in request.args:
        logging.info('Found "message" in query parameters: %s', request.args.get('message'))
        return request.args.get('message')

    # Log the raw request data to see the body of POST requests
    logging.info('Raw Request Data: %s', request.get_data())

    # Try to parse the JSON body (POST request)
    request_json = request.get_json()
    if request_json:
        logging.info('Parsed JSON Body: %s', request_json)
        if 'message' in request_json:
            logging.info('Found "message" in JSON body: %s', request_json['message'])
            return request_json['message']
        else:
            logging.warning('No "message" key found in JSON body')
    else:
        logging.warning('No JSON body found or failed to parse')

    # If no "message" in either query parameters or JSON body, return a default response
    logging.info('Returning default response')
    return 'Function - 1 with V1.0 with CICD'

