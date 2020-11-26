#!/usr/bin/env python3
# Created by: Roman Cernetchi
# Created on: November 2020
# This program calculates total cost of a pizza

import constant_p


def main():
    # This function calculates total cost of a pizza

    # Input
    diameter = int(input("Enter the diameter of the pizza (Inch): "))

    # process
    sub_total = constant_p.Labor + constant_p.Rent + \
        (diameter*constant_p.Cost_per_inch)
    total = sub_total*(constant_p.HST)

    # Output
    print("")
    print("Total cost is ${}".format(total))


if __name__ == "__main__":
    main()
