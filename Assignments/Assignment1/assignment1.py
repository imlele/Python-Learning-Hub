# Constants
YEAR = 0
MONTH = 4
DAY = 6
FROM = 8
TO = 11
SEAT = 14
FLYER = 17

WINDOW = 'window'
AISLE = 'aisle'
MIDDLE = 'middle'


def get_flyer_info(ticket: str) -> str:
    """Return the flyer number of the flyer for this ticket, if present. 
    Otherwise, return the empty string.
    
    >>> get_flyer_info('20230915YYZYEG12F')
    ''
    >>> get_flyer_info('20230915YYZYEG12F1236')
    '1236'
    """
    # Write the body of the function here


# Write the rest of your Assignment 1 functions here
