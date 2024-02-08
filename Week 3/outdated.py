""" Problem
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order,
which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that
format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order,
no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or
September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
 Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days. """

def main():
    # List of month names for reference
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        # Prompt user for a date
        user_input = input("Enter a date (MM/DD/YYYY or Month DD, YYYY): ")

        # Try to parse and convert the date
        try:
            # Check if the input is in the MM/DD/YYYY format
            if '/' in user_input:
                month, day, year = map(int, user_input.split('/'))
            else:
                # Assume the input is in the Month DD, YYYY format
                month_str, day, year = user_input.replace(',', '').split()
                month = months.index(month_str) + 1  # Convert month name to number
                day = int(day)
                year = int(year)

            # Validate if the month and day are within valid ranges
            if 1 <= month <= 12 and 1 <= day <= 31:
                # Output in YYYY-MM-DD format with zero padding for month and day
                print(f"{year}-{month:02}-{day:02}")
                break  # Exit the loop after successful conversion
            else:
                raise ValueError  # Raise an error if the date is not valid

        except (ValueError, IndexError):
            # Handle any errors during parsing and conversion
            print("Invalid date format. Please try again.")

main()
