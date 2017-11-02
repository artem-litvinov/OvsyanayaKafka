from aioprometheus import Summary

MAKE_USER_REQUEST_TIME = Summary('make_user_request_processing_seconds', 'Time spent processing user making request')
USER_CREATING_TIME = Summary('make_user_operation_processing_seconds', 'Time spent processing user making operation')
PRODUCING_TIME = Summary('make_message_produce_processing_seconds', 'Time spent processing making message producing')
MESSAGE_CREATING_TIME = Summary('make_message_operation_processing_seconds', 'Time spent processing making message operation')
SEND_MESAGE_REQUEST_TIME = Summary('make_send_message_request_processing_seconds', 'Time spent processing send message request')

METRICS = (
    PRODUCING_TIME,
    USER_CREATING_TIME,
    MESSAGE_CREATING_TIME,
    MAKE_USER_REQUEST_TIME,
    SEND_MESAGE_REQUEST_TIME,
    )
