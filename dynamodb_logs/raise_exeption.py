from import_error_log import default

try:
    # Raise an exception with argument
    raise ValueError('Scary value error')
except Exception, arg:
    #catch exeption
    print 'Error: ', arg
