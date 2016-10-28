import json
from log_error import create_error
#
# DecimalEncoder = DecimalEncoder()

# return DecimalEncoder.run

try:
    # Raise an exception with argument
    # print 'DecimalEndoder: ', DecimalEncoder()
    raise ValueError('Scary value error')
except Exception, arg:
    #catch exeption
    create_error(arg)
    # print 'Error: ', arg
