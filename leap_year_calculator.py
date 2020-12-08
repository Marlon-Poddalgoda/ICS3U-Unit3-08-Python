#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program determines if a year is a leap year

import constants


def main():
    # this function will calculate if a year is a leap year

    print("This program determines if a given year "
          "is a leap year.")

    # input
    input_year = input("Enter a year: ")
    print("")

    # process
    try:
        input_year_int = int(input_year)

        if input_year_int % constants.QUADRENNIAL == 0:
            if input_year_int % constants.CENTENNIAL == 0:
                if input_year_int % constants.QUADRICENTENNIAL == 0:
                    # output
                    print("{} is a leap year!"
                          .format(input_year_int))
                else:
                    # output
                    print("{} is not a leap year."
                          .format(input_year_int))
            else:
                # output
                print("{} is a leap year!"
                      .format(input_year_int))
        else:
            # output
            print("{} is not a leap year."
                  .format(input_year_int))
    except Exception:
        # output
        print("That's not a Year! Try again.")
    finally:
        # output
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
