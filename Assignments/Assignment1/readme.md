# Assignment 1

## Overview
In this assignment, you will practice writing code that uses variables, functions, if statements, and string operations. You will also practice documenting, coding, and testing your functions using the Function Design Recipe.

## Introduction: Airplane Tickets
The typical airplane boarding pass contains many different pieces of information, including passenger information, seat, flight number, flight time, and so on. In this assignment, we'll work with our own version of the information you might find on a boarding pass. We'll refer to the data we work with as a "ticket". A ticket is a string, where different parts of the string represent different kinds of information. Our ticket will include the following information:

- The date the ticket is for, including year, month, and day.
- "From" and "to" airports of the flight the ticket is for.
- The seat assigned to the ticket.
- The passenger's flyer number, if applicable.

A valid ticket will have either 17 or 21 characters (from indexes 0 to 16 or 20 respectively). Below, we describe what the different index ranges mean in a ticket.

- Indexes 0 to 7 represent the date the ticket is for. More specifically, indexes 0 to 3 represent the year, indexes 4 and 5 the month, and indexes 6 and 7 the day. For example, a ticket might have the value `'20230901'` in indexes 0 to 7, representing September 1, 2023.
- Indexes 8 to 10 and 11 to 13 represent the From and To airports, respectively. A ticket for a flight from YYZ (Toronto) to YEG (Edmonton) would have `'YYZYEG'` at these indexes.
- Indexes 14 to 16 represent the seat the ticket is for. The first two characters here are the row the seat is in. Rows are limited to 1 to 30 for this assignment. The third character is the seat, which can be one of ABCDEF. For example, a ticket for seat C in row 9 would have `'09C'` at these indexes. Seats A and F are window seats, seats B and E are middle seats, and seats C and D are aisle seats.
- Index 17 and on represents the flyer number for the passenger this ticket belongs to, if they have one.

Here are some examples of tickets:

- This ticket is for December 21, 2023, for a flight from YYZ to YEG in seat 25F. The passenger's flyer number is 4442.
  ```
  20231221YYZYEG25F4442
  ```
  
- This ticket is for April 24, 2024, for a flight from YTZ to YUL in seat 4B. The passenger does not have a flyer number.
  ```
  20240424YTZYUL04B
  ```

## Required Functions

### Task 1: Getting Ticket Information

#### `get_flyer_info`
- **Parameters**: `(str) -> str`
- **Description**: The parameter represents a valid ticket. This function should return the flyer number from the ticket.

#### `visits_airport`
- **Parameters**: `(str, str) -> bool`
- **Description**: The first parameter represents a valid ticket. The second is a three-character string representing an airport. This function should return True if and only if the given airport is either the From or To airport on this ticket, and False otherwise. This function is case-sensitive. ('YYZ' and 'yyz'" are considered differnet)

#### `get_seat_type`
- **Parameters**: `(str) -> str`
- **Description**: The parameter represents a ticket. This function should return 'window', 'aisle', or 'middle' depending on the seat type. If the seat type is invalid, return the empty string. This function should make use of the provided constants in its return statements.

### Task 2: Checking Ticket Information is Valid

#### `is_valid_seat`
- **Parameters**: `(str) -> bool`
- **Description**: The parameter represents a ticket that is properly formed, although the data in the seat indexes may not be correct. This function should return True if and only if the seat in this ticket is valid, and False otherwise. A seat is considered valid if it is in a row between 1 and 30, and has a seat letter A, B, C, D, E, or F.

#### `is_valid_flyer`
- **Parameters**: `(str) -> bool`
- **Description**: The parameter represents a ticket that is properly formed. However, the data in the flyer number indexes may not be correct (although all characters at index 17 and up will be digits). This function should return True if and only if the given flyer number is valid, and False otherwise. A non-empty flyer number is valid if it consists of exactly four digits, and the sum of the first three digits taken modulo 10 is equal to the fourth digit. An empty flyer number is also valid.

#### `is_valid_ticket`
- **Parameters**: `(str) -> bool`
- **Description**: The parameter represents a ticket. It has an appropriate number of characters and has digits in all positions except the airport and seat letter indexes. This function should return True if and only if the ticket has a valid seat, a valid flyer number, and has different From and To airports.

### Task 3: Days Between Today

The first parameter represents a valid ticket. The second represents a date, made up of digits, and of the format YYYYMMDD. This function should return the number of days from the second parameter until the ticket date. The number of days returned can be negative if the ticket date comes before the given date.

We'll make some simplifications in our day-counting process. First, all years have 365 days (we'll ignore leap years). Second, we'll assume all months have 30 days.

#### `days_until`
- **Parameters**: `(str, str) -> int`
- **Description**: The first parameter represents a valid ticket. The second represents a date, made up of digits, and of the format YYYYMMDD. This function should return the number of days from the second parameter until the ticket date. The number of days returned can be negative if the ticket date comes before the given date. Some simplifications are made in the day-counting process: all years have 365 days (ignoring leap years), and all months have 30 days.

Here are some examples:

- if the arguments to the function are `'20230908YULYYZ07C2349'`, `'20230901'`, then the expected result is `7`.
- if the arguments to the function are `'20240430YYCYEG11E'`, `'20230901'`, then the expected result is `244`.
- if the arguments to the function are `'20220101YQUYEG03D6411'`, `'20230901'`, then the expected result is `-605`.

## Additional Notes
- Throughout your code, you must make use of the constants provided in `Assignment 1.py`, rather than explicitly writing out the numbers. Your code should work correctly even if additional information is added at the beginning of the ticket string, changing the current values of the constants. Using the provided constants ensures the code's robustness.