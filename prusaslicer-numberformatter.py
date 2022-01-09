"""
    Reformat ALL the numbers.
    Example: replace .05 with 0.05

    Add that script to the post processing section of PrusaSlicer.
    Maybe so:
    "C:/Users/USERNAME/AppData/Local/Programs/Python/Python39/python.exe"
        "C:/dev/prusaslicer-numberformatter.py";
"""

import sys
import re
import decimal
from decimal import Decimal

SOURCEFILE = sys.argv[1]
REGEX = r"[+-]?\d*\.?\d+(?:[Ee][+-]?\d+)?"

def main(sourcefile):
    """
    Main.

    Args:
        sourcefile ([string]): [the source gcode file]
    """
    # Read the ENTIRE GCode file into memory
    lines = ""
    with open(sourcefile, "r", encoding='UTF-8') as readfile:
        lines = readfile.readlines()

    # Replace the gcode file.
    # Replace ALL(!!!) the numbers with format_number().
    with open(sourcefile, "w", newline='\n', encoding='UTF-8') as writefile:
        # loop over gcode file in memory
        for _, strline in enumerate(lines):
            # Find ALL numbers
            matches = re.finditer(REGEX, strline, re.MULTILINE)
            for _, match in enumerate(matches, start=1):
                # Replace each number with the correct formatted number
                strline = strline.replace(match.group(), format_number(match.group()))
            # Write line back to file
            writefile.write(strline)


def format_number(num):
    """
        https://stackoverflow.com/a/5808014/827526

    Args:
        sourcefile ([string]): [number to be formatted correctly]
    """
    try:
        dec = Decimal(num)
    except decimal.DecimalException as ex:
        print(str(ex))
        # return f'Bad number. Not a decimal: {num}'
        return "nan"
    tup = dec.as_tuple()
    delta = len(tup.digits) + tup.exponent
    digits = ''.join(str(d) for d in tup.digits)
    if delta <= 0:
        zeros = abs(tup.exponent) - len(tup.digits)
        val = '0.' + ('0'*zeros) + digits
    else:
        val = digits[:delta] + ('0'*tup.exponent) + '.' + digits[delta:]
    val = val.rstrip('0')
    if val[-1] == '.':
        val = val[:-1]
    if tup.sign:
        return '-' + val
    return val


main(SOURCEFILE)
