#!/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: April 5, 2025
# The code determines the air quality level based on the user input AQI value


def main():
    # Intro message for the user to understand what the program does
    print("Welcome to the Air Quality Index (AQI) Checker!")
    print("Please enter a number between 0 and 500 to check the air quality.\n")

    # Get user input for their air quality as a string
    aqi_num = input("Enter the AQI number: ")


    # Try catch statement to make sure the input from the user is a valid number
    try:
        # It converts the user input to a float, and then rounds the decimals to the nearest number converting it to a string 
        aqi_float = float(aqi_num)
        aqi_int = round(aqi_float)

        # Checks if the number is between 0 and 500 With an OR statement
        if aqi_int < 0 or aqi_int > 500:
            print("Error: The AQI needs to be between 0 and 500")

        # Nested if statement if AQI is between (0-50)
        else:
            if aqi_int <= 50:
                print("Air Quality: Good")

            # Nested if nested statement if AQI is between (51-100)
            else:
                if aqi_int <= 100:
                    print("Air Quality: Moderate")

                # Nested if statement if AQI is between (101-200)
                else:
                    if aqi_int <= 200:
                        print("Air quality: Unhealthy")

                        # Extra Nested if for an extra warning after 175 (AQI)
                        if aqi_int > 175:
                            print("Warning!: Consider staying indoors due to high pollution.")

                    # Nested if statement if AQi is between (201-300)
                    else:
                        if aqi_int <= 300:
                            print("Air Quality: Very Unhealthy")

                        # Nested if statement if AQI is between (301-500)
                        else:
                            if aqi_int <= 500:
                                print("Air quality: Hazardous")

    # Exception if user input is not a valid input
    except Exception:
        print("Error: Invalid input. Please enter an integer.")


# Main function call
if __name__ == "__main__":
    main()
