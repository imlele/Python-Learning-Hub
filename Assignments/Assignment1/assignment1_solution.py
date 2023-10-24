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


# Task 1
def get_flyer_info(ticket: str) -> str:
    """Return the flyer number of the flyer for this ticket, if present. 
    Otherwise, return the empty string.
    
    >>> get_flyer_info('20230915YYZYEG12F')
    ''
    >>> get_flyer_info('20230915YYZYEG12F1236')
    '1236'
    """
    return ticket[FLYER:]


def visits_airport(ticket: str, airport: str) -> bool:
    """Return True if the given airport is either the 'From' or 'To'
    airport in the ticket, False otherwise.

    >>> visits_airport('20230915YYZYEG12F', 'YYZ')
    True
    >>> visits_airport('20230915YYZYEG12F', 'yyz')
    False
    >>> visits_airport('20230915YYZYEG12F', 'YEG')
    True
    >>> visits_airport('20230915YYZYEG12F', 'YUL')
    False
    """
    first_airport = ticket[FROM:FROM+3]
    second_airport = ticket[TO:TO+3]
    return airport == first_airport or airport == second_airport


def get_seat_type(ticket:str) -> str:
    """Return the type of seat ('window', 'aisle', or 'middle') for a given ticket.
    If the seat type is invalid, return an empty string.

    >>> get_seat_type('20230915YYZYEG12A')
    'window'
    >>> get_seat_type('20230915YYZYEG12B')
    'middle'
    >>> get_seat_type('20230915YYZYEG12C')
    'aisle'
    >>> get_seat_type('20230915YYZYEG12G')
    ''
    """
    seat_number = ticket[SEAT+2]
    if seat_number == "A" or seat_number == "F":
        return WINDOW
    elif seat_number == "B" or seat_number == "E":
        return MIDDLE
    elif seat_number == "C" or seat_number == "D":
        return AISLE
    return ''


# Task 2
def is_valid_seat(ticket:str) -> bool:
    """Return True if the seat in the ticket is valid, and False otherwise.

    Any seat with a row between 1 and 30, inclusive, and a seat letter
    of A, B, C, D, E, or F is considered to be valid.

    Precondition: ticket is properly formed

    >>> is_valid_seat('20230915YYZYEG15A')
    True
    >>> is_valid_seat('20230915YYZYEG31A')
    False
    >>> is_valid_seat('20230915YYZYEG15G')
    False
    >>> is_valid_seat('20230915YYZYEG00A')
    False
    """
    row = int(ticket[SEAT:SEAT+2])
    # print(row)
    seat = ticket[SEAT+2] # error 1
    # print(seat)
    return 1 <= row <= 30 and seat in "ABCDEF"


def is_valid_flyer(ticket:str) -> bool:
    """
    Return True if the flyer number in the ticket is valid, and False otherwise.

    If a flyer number has exactly four digits and the fourth digit equals the
    sum of the first three digits determined modulo 10, it is considered to
    be valid. An empty flyer number is also valid.

    Precondition: ticket is properly formed

    >>> is_valid_flyer('20230915YYZYEG12F')
    True
    >>> is_valid_flyer('20230915YYZYEG12F1236') # error 2
    True
    >>> is_valid_flyer('20230915YYZYEG12F1235')
    False
    >>> is_valid_flyer('20230915YYZYEG12F12345')
    False
    """
    if not (len(ticket) == 17 or len(ticket) == 21):
        return False
    # print('here')
    flyer = ticket[FLYER:]
    if flyer == '':
        return True
    else:
        first = int(flyer[0])
        second = int(flyer[1])
        third = int(flyer[2])
        fourth = int(flyer[3])
        return (first + second + third) % 10 == fourth


def is_valid_ticket(ticket:str) -> bool:
    """Return True if the ticket has a valid seat, a valid flyer number, and
    different From and To airports. Otherwise, return False.

    >>> is_valid_ticket('20230915YYZYEG12F1236')
    True
    >>> is_valid_ticket('20230915YYZYYZ12F1236')
    False
    >>> is_valid_ticket('20230915YYZYEG12G1236')
    False
    >>> is_valid_ticket('20230915YYZYEG12F1235')
    False
    """
    if is_valid_flyer(ticket) and is_valid_seat(ticket):
        first_airport = ticket[FROM:FROM+3]
        second_airport = ticket[TO:TO+3]
        return first_airport != second_airport
    return False


def days_until(ticket:str, date: str) -> int:
    """Return the number of days from the given date until the ticket date.

    >>> days_until('20230908YULYYZ07C2349', '20230901')
    -1
    >>> days_until('20240430YYCYEG11E', '20230901')
    217
    >>> days_until('20220101YQUYEG03D6411', '20230901')
    -606
    """
    ticket_year = int(ticket[YEAR:MONTH])
    ticket_month = int(ticket[MONTH:DAY])
    ticket_day = int(ticket[DAY])

    date_year = int(date[:4])
    date_month = int(date[4:6])
    date_day = int(date[6:])

    ticket_total_days = ticket_year * 365 + ticket_month * 30 + ticket_day
    date_total_days = date_year * 365 + date_month * 30 + date_day

    return ticket_total_days - date_total_days


if '__name__' == "__main__":
    import doctest
    doctest.testmod()

