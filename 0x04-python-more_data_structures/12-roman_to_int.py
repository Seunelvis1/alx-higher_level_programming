#!/usr/bin/python3

def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for m in list_num:
        if max_list > m:
            to_sub += m

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_m.keys())

    num = 0
    last_rmom = 0
    list_numb = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_m.get(ch) <= last_rmom:
                    num += to_subtract(list_numb)
                    list_numb = [rom_m.get(ch)]
                else:
                    list_numb.append(rom_m.get(ch))

                last_rmom = rom_nm.get(ch)

    num += to_subtract(list_numb)

    return (num)
