def main():

    time_input = input("Enter a time (HH:MM): ")
    time_as_float = convert(time_input)

    if 7.0 <= time_as_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_as_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_as_float <= 19.0:
        print("dinner time")
    # No output if it's not a meal time

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
