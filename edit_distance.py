def edit_distance(str1, str2):
    """
    case 1: the same length 
    case 2: they are not the same length 

    """

    # if the strings are the same, edit distance = 0
    if str1 == str2:
        return 0

    # the case if the strings are the same length
    # ben, hen
    if len(str1) == len(str2):
        counter = 0
        for idx, ch_ in enumerate(str1):
            if ch_ != str2[idx]:
                counter += 1

        return counter

    if len(str1) != len(str2):
        counter = 0
        # add the difference
        # i.e. the then -> 4 - 3 =  1

        larger = None
        smaller = None

        if len(str1) > len(str2):
            larger = str1
            smaller = str2
        else:
            larger = str2
            smaller = str1

        offset = len(larger) - len(smaller)
        counter += offset

        for idx, ch_ in enumerate(smaller):
            if ch_ != larger[idx]:
                counter += 1

        return counter


if __name__ == '__main__':
    WD_1 = "the"
    WD_2 = "hen"
    WD_3 = "ben"
    WD_4 = "then"
    WD_5 = "again"
    print(
        f"The distance of '{WD_1}' and '{WD_1}' is { edit_distance(WD_1, WD_1)}")
    print(
        f"The distance of '{WD_2}' and '{WD_3}' is { edit_distance(WD_2, WD_3)}")
    print(
        f"The distance of '{WD_1}' and '{WD_4}' is { edit_distance(WD_1, WD_4)}")
    print(
        f"The distance of '{WD_1}' and '{WD_4}' is { edit_distance(WD_4, WD_1)}")
    print(
        f"The distance of '{WD_1}' and '{WD_5}' is { edit_distance(WD_1, WD_5)}")
