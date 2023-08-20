# Converting 12-hour time to 24-hour time

def convert_to_24_hour():
    hour = int(input("Enter the hour (1-12): "))
    minute = int(input("Enter the minute (0-59): "))
    period = input("Enter 'am' or 'pm': ")

    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    result = f"{hour:02d}{minute:02d}"
    print(f"The time in 24-hour format is: {result}")

convert_to_24_hour()

