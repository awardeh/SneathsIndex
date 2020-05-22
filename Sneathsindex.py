import xlwt


def sneath_compare(a, b):
    return conversion_dict[(a, b)]


dna_set = {"G", "A", "L", "M", "F", "W", "K", "Q", "E", "S", "P", 'V', 'I', 'C', 'Y', 'H', 'R', 'N', 'D', 'T', '-'}

conversion_dict = {('L', 'L'): 0,
                   ('L', 'I'): 5,
                   ('L', 'V'): 9,
                   ('L', 'G'): 24,
                   ('L', 'A'): 15,
                   ('L', 'P'): 23,
                   ('L', 'Q'): 22,
                   ('L', 'N'): 20,
                   ('L', 'M'): 20,
                   ('L', 'T'): 23,
                   ('L', 'S'): 23,
                   ('L', 'C'): 24,
                   ('L', 'E'): 30,
                   ('L', 'D'): 25,
                   ('L', 'K'): 23,
                   ('L', 'R'): 33,
                   ('L', 'Y'): 30,
                   ('L', 'F'): 19,
                   ('L', 'W'): 30,
                   ('L', 'H'): 25,
                   #
                   ('I', 'L'): 0,
                   ('I', 'I'): 0,
                   ('I', 'V'): 7,
                   ('I', 'G'): 25,
                   ('I', 'A'): 17,
                   ('I', 'P'): 24,
                   ('I', 'Q'): 24,
                   ('I', 'N'): 23,
                   ('I', 'M'): 22,
                   ('I', 'T'): 21,
                   ('I', 'S'): 25,
                   ('I', 'C'): 26,
                   ('I', 'E'): 31,
                   ('I', 'D'): 28,
                   ('I', 'K'): 24,
                   ('I', 'R'): 34,
                   ('I', 'Y'): 34,
                   ('I', 'F'): 22,
                   ('I', 'W'): 34,
                   ('I', 'H'): 28,
                   ('I', 'V'): 7,
                   ('I', 'G'): 25,
                   ('I', 'A'): 17,
                   ('I', 'P'): 24,
                   ('I', 'Q'): 24,
                   ('I', 'N'): 23,
                   ('I', 'M'): 22,
                   ('I', 'T'): 21,
                   ('I', 'S'): 25,
                   ('I', 'C'): 26,
                   ('I', 'E'): 31,
                   ('I', 'D'): 28,
                   ('I', 'K'): 24,
                   ('I', 'R'): 34,
                   ('I', 'Y'): 34,
                   ('I', 'F'): 22,
                   ('I', 'W'): 34,
                   ('I', 'H'): 28,
                   #
                   ('V', 'L'): 0,
                   ('V', 'I'): 0,
                   ('V', 'V'): 0,
                   ('V', 'G'): 19,
                   ('V', 'A'): 12,
                   ('V', 'P'): 20,
                   ('V', 'Q'): 25,
                   ('V', 'N'): 23,
                   ('V', 'M'): 23,
                   ('V', 'T'): 17,
                   ('V', 'S'): 20,
                   ('V', 'C'): 21,
                   ('V', 'E'): 31,
                   ('V', 'D'): 28,
                   ('V', 'K'): 26,
                   ('V', 'R'): 36,
                   ('V', 'Y'): 36,
                   ('V', 'F'): 26,
                   ('V', 'W'): 37,
                   ('V', 'H'): 31,
                   #
                   ('G', 'L'): 0,
                   ('G', 'I'): 0,
                   ('G', 'V'): 0,
                   ('G', 'G'): 0,
                   ('G', 'A'): 9,
                   ('G', 'P'): 17,
                   ('G', 'Q'): 32,
                   ('G', 'N'): 26,
                   ('G', 'M'): 34,
                   ('G', 'T'): 20,
                   ('G', 'S'): 19,
                   ('G', 'C'): 21,
                   ('G', 'E'): 37,
                   ('G', 'D'): 33,
                   ('G', 'K'): 31,
                   ('G', 'R'): 43,
                   ('G', 'Y'): 36,
                   ('G', 'F'): 29,
                   ('G', 'W'): 39,
                   ('G', 'H'): 34,
                   #
                   ('A', 'L'): 0,
                   ('A', 'I'): 0,
                   ('A', 'V'): 0,
                   ('A', 'G'): 0,
                   ('A', 'A'): 0,
                   ('A', 'P'): 16,
                   ('A', 'Q'): 26,
                   ('A', 'N'): 25,
                   ('A', 'M'): 25,
                   ('A', 'T'): 20,
                   ('A', 'S'): 16,
                   ('A', 'C'): 13,
                   ('A', 'E'): 34,
                   ('A', 'D'): 30,
                   ('A', 'K'): 26,
                   ('A', 'R'): 37,
                   ('A', 'Y'): 34,
                   ('A', 'F'): 26,
                   ('A', 'W'): 36,
                   ('A', 'H'): 29,
                   #
                   ('P', 'L'): 0,
                   ('P', 'I'): 0,
                   ('P', 'V'): 0,
                   ('P', 'G'): 0,
                   ('P', 'A'): 0,
                   ('P', 'P'): 0,
                   ('P', 'Q'): 33,
                   ('P', 'N'): 31,
                   ('P', 'M'): 31,
                   ('P', 'T'): 25,
                   ('P', 'S'): 24,
                   ('P', 'C'): 25,
                   ('P', 'E'): 43,
                   ('P', 'D'): 40,
                   ('P', 'K'): 31,
                   ('P', 'R'): 43,
                   ('P', 'Y'): 37,
                   ('P', 'F'): 27,
                   ('P', 'W'): 37,
                   ('P', 'H'): 36,

                   #
                   ('Q', 'L'): 0,
                   ('Q', 'I'): 0,
                   ('Q', 'V'): 0,
                   ('Q', 'G'): 0,
                   ('Q', 'A'): 0,
                   ('Q', 'P'): 0,
                   ('Q', 'Q'): 0,
                   ('Q', 'N'): 31,
                   ('Q', 'M'): 31,
                   ('Q', 'T'): 25,
                   ('Q', 'S'): 24,
                   ('Q', 'C'): 25,
                   ('Q', 'E'): 43,
                   ('Q', 'D'): 40,
                   ('Q', 'K'): 31,
                   ('Q', 'R'): 43,
                   ('Q', 'Y'): 37,
                   ('Q', 'F'): 27,
                   ('Q', 'W'): 37,
                   ('Q', 'H'): 36,
                   #
                   ('N', 'L'): 0,
                   ('N', 'I'): 0,
                   ('N', 'V'): 0,
                   ('N', 'G'): 0,
                   ('N', 'A'): 0,
                   ('N', 'P'): 0,
                   ('N', 'Q'): 0,
                   ('N', 'N'): 0,
                   ('N', 'M'): 21,
                   ('N', 'T'): 19,
                   ('N', 'S'): 15,
                   ('N', 'C'): 19,
                   ('N', 'E'): 19,
                   ('N', 'D'): 14,
                   ('N', 'K'): 27,
                   ('N', 'R'): 31,
                   ('N', 'Y'): 28,
                   ('N', 'F'): 24,
                   ('N', 'W'): 32,
                   ('N', 'H'): 24,
                   #
                   ('M', 'L'): 0,
                   ('M', 'I'): 0,
                   ('M', 'V'): 0,
                   ('M', 'G'): 0,
                   ('M', 'A'): 0,
                   ('M', 'P'): 0,
                   ('M', 'Q'): 0,
                   ('M', 'N'): 0,
                   ('M', 'M'): 0,
                   ('M', 'T'): 25,
                   ('M', 'S'): 22,
                   ('M', 'C'): 17,
                   ('M', 'E'): 26,
                   ('M', 'D'): 31,
                   ('M', 'K'): 24,
                   ('M', 'R'): 28,
                   ('M', 'Y'): 32,
                   ('M', 'F'): 24,
                   ('M', 'W'): 31,
                   ('M', 'H'): 30,
                   #
                   ('M', 'L'): 0,
                   ('M', 'I'): 0,
                   ('M', 'V'): 0,
                   ('M', 'G'): 0,
                   ('M', 'A'): 0,
                   ('M', 'P'): 0,
                   ('M', 'Q'): 0,
                   ('M', 'N'): 0,
                   ('M', 'M'): 0,
                   ('M', 'T'): 25,
                   ('M', 'S'): 22,
                   ('M', 'C'): 17,
                   ('M', 'E'): 26,
                   ('M', 'D'): 31,
                   ('M', 'K'): 24,
                   ('M', 'R'): 28,
                   ('M', 'Y'): 32,
                   ('M', 'F'): 24,
                   ('M', 'W'): 31,
                   ('M', 'H'): 30,
                   #
                   ('T', 'L'): 0,
                   ('T', 'I'): 0,
                   ('T', 'V'): 0,
                   ('T', 'G'): 0,
                   ('T', 'A'): 0,
                   ('T', 'P'): 0,
                   ('T', 'Q'): 0,
                   ('T', 'N'): 0,
                   ('T', 'M'): 0,
                   ('T', 'T'): 0,
                   ('T', 'S'): 12,
                   ('T', 'C'): 19,
                   ('T', 'E'): 34,
                   ('T', 'D'): 29,
                   ('T', 'K'): 34,
                   ('T', 'R'): 38,
                   ('T', 'Y'): 32,
                   ('T', 'F'): 28,
                   ('T', 'W'): 38,
                   ('T', 'H'): 34,
                   #
                   ('S', 'L'): 0,
                   ('S', 'I'): 0,
                   ('S', 'V'): 0,
                   ('S', 'G'): 0,
                   ('S', 'A'): 0,
                   ('S', 'P'): 0,
                   ('S', 'Q'): 0,
                   ('S', 'N'): 0,
                   ('S', 'M'): 0,
                   ('S', 'T'): 0,
                   ('S', 'S'): 0,
                   ('S', 'C'): 13,
                   ('S', 'E'): 29,
                   ('S', 'D'): 25,
                   ('S', 'K'): 31,
                   ('S', 'R'): 37,
                   ('S', 'Y'): 29,
                   ('S', 'F'): 25,
                   ('S', 'W'): 35,
                   ('S', 'H'): 28,
                   #
                   ('C', 'L'): 0,
                   ('C', 'I'): 0,
                   ('C', 'V'): 0,
                   ('C', 'G'): 0,
                   ('C', 'A'): 0,
                   ('C', 'P'): 0,
                   ('C', 'Q'): 0,
                   ('C', 'N'): 0,
                   ('C', 'M'): 0,
                   ('C', 'T'): 0,
                   ('C', 'S'): 0,
                   ('C', 'C'): 0,
                   ('C', 'E'): 33,
                   ('C', 'D'): 28,
                   ('C', 'K'): 32,
                   ('C', 'R'): 36,
                   ('C', 'Y'): 34,
                   ('C', 'F'): 29,
                   ('C', 'W'): 37,
                   ('C', 'H'): 31,
                   #
                   ('E', 'L'): 0,
                   ('E', 'I'): 0,
                   ('E', 'V'): 0,
                   ('E', 'G'): 0,
                   ('E', 'A'): 0,
                   ('E', 'P'): 0,
                   ('E', 'Q'): 0,
                   ('E', 'N'): 0,
                   ('E', 'M'): 0,
                   ('E', 'T'): 0,
                   ('E', 'S'): 0,
                   ('E', 'C'): 0,
                   ('E', 'E'): 0,
                   ('E', 'D'): 7,
                   ('E', 'K'): 26,
                   ('E', 'R'): 31,
                   ('E', 'Y'): 34,
                   ('E', 'F'): 35,
                   ('E', 'W'): 43,
                   ('E', 'H'): 27,
                   #
                   ('D', 'L'): 0,
                   ('D', 'I'): 0,
                   ('D', 'V'): 0,
                   ('D', 'G'): 0,
                   ('D', 'A'): 0,
                   ('D', 'P'): 0,
                   ('D', 'Q'): 0,
                   ('D', 'N'): 0,
                   ('D', 'M'): 0,
                   ('D', 'T'): 0,
                   ('D', 'S'): 0,
                   ('D', 'C'): 0,
                   ('D', 'E'): 0,
                   ('D', 'D'): 0,
                   ('D', 'K'): 34,
                   ('D', 'R'): 39,
                   ('D', 'Y'): 34,
                   ('D', 'F'): 35,
                   ('D', 'W'): 45,
                   ('D', 'H'): 35,
                   #
                   ('K', 'L'): 0,
                   ('K', 'I'): 0,
                   ('K', 'V'): 0,
                   ('K', 'G'): 0,
                   ('K', 'A'): 0,
                   ('K', 'P'): 0,
                   ('K', 'Q'): 0,
                   ('K', 'N'): 0,
                   ('K', 'M'): 0,
                   ('K', 'T'): 0,
                   ('K', 'S'): 0,
                   ('K', 'C'): 0,
                   ('K', 'E'): 0,
                   ('K', 'D'): 0,
                   ('K', 'K'): 0,
                   ('K', 'R'): 14,
                   ('K', 'Y'): 34,
                   ('K', 'F'): 28,
                   ('K', 'W'): 34,
                   ('K', 'H'): 27,
                   #
                   ('R', 'L'): 0,
                   ('R', 'I'): 0,
                   ('R', 'V'): 0,
                   ('R', 'G'): 0,
                   ('R', 'A'): 0,
                   ('R', 'P'): 0,
                   ('R', 'Q'): 0,
                   ('R', 'N'): 0,
                   ('R', 'M'): 0,
                   ('R', 'T'): 0,
                   ('R', 'S'): 0,
                   ('R', 'C'): 0,
                   ('R', 'E'): 0,
                   ('R', 'D'): 0,
                   ('R', 'K'): 0,
                   ('R', 'R'): 0,
                   ('R', 'Y'): 36,
                   ('R', 'F'): 34,
                   ('R', 'W'): 36,
                   ('R', 'H'): 31,
                   #
                   ('Y', 'L'): 0,
                   ('Y', 'I'): 0,
                   ('Y', 'V'): 0,
                   ('Y', 'G'): 0,
                   ('Y', 'A'): 0,
                   ('Y', 'P'): 0,
                   ('Y', 'Q'): 0,
                   ('Y', 'N'): 0,
                   ('Y', 'M'): 0,
                   ('Y', 'T'): 0,
                   ('Y', 'S'): 0,
                   ('Y', 'C'): 0,
                   ('Y', 'E'): 0,
                   ('Y', 'D'): 0,
                   ('Y', 'K'): 0,
                   ('Y', 'R'): 0,
                   ('Y', 'Y'): 0,
                   ('Y', 'F'): 13,
                   ('Y', 'W'): 21,
                   ('Y', 'H'): 23,
                   #
                   ('F', 'L'): 0,
                   ('F', 'I'): 0,
                   ('F', 'V'): 0,
                   ('F', 'G'): 0,
                   ('F', 'A'): 0,
                   ('F', 'P'): 0,
                   ('F', 'Q'): 0,
                   ('F', 'N'): 0,
                   ('F', 'M'): 0,
                   ('F', 'T'): 0,
                   ('F', 'S'): 0,
                   ('F', 'C'): 0,
                   ('F', 'E'): 0,
                   ('F', 'D'): 0,
                   ('F', 'K'): 0,
                   ('F', 'R'): 0,
                   ('F', 'Y'): 0,
                   ('F', 'F'): 0,
                   ('F', 'W'): 13,
                   ('F', 'H'): 18,
                   #
                   ('W', 'L'): 0,
                   ('W', 'I'): 0,
                   ('W', 'V'): 0,
                   ('W', 'G'): 0,
                   ('W', 'A'): 0,
                   ('W', 'P'): 0,
                   ('W', 'Q'): 0,
                   ('W', 'N'): 0,
                   ('W', 'M'): 0,
                   ('W', 'T'): 0,
                   ('W', 'S'): 0,
                   ('W', 'C'): 0,
                   ('W', 'E'): 0,
                   ('W', 'D'): 0,
                   ('W', 'K'): 0,
                   ('W', 'R'): 0,
                   ('W', 'Y'): 0,
                   ('W', 'F'): 0,
                   ('W', 'W'): 0,
                   ('W', 'H'): 25,
                   #
                   ('H', 'L'): 0,
                   ('H', 'I'): 0,
                   ('H', 'V'): 0,
                   ('H', 'G'): 0,
                   ('H', 'A'): 0,
                   ('H', 'P'): 0,
                   ('H', 'Q'): 0,
                   ('H', 'N'): 0,
                   ('H', 'M'): 0,
                   ('H', 'T'): 0,
                   ('H', 'S'): 0,
                   ('H', 'C'): 0,
                   ('H', 'E'): 0,
                   ('H', 'D'): 0,
                   ('H', 'K'): 0,
                   ('H', 'R'): 0,
                   ('H', 'Y'): 0,
                   ('H', 'F'): 0,
                   ('H', 'W'): 0,
                   ('H', 'H'): 0,
                   }
while 1:
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    sheet1.write(0, 0, "column_number")
    sheet1.write(0, 1, "total_difference")
    sheet1.write(0, 2, "average_difference")
    col = 1
    status = True
    string1 = input("input the first sequence or type quit: ").strip().upper()
    if string1 == "QUIT":
        break
    other_strings = []
    string_in = ""
    length1 = len(string1)
    for i in set(string1):
        if i not in dna_set:
            print("input 1 is not correct")
            status = False
    if status is not True:
        continue
    while string_in != "QUIT":
        incorrect = False
        string_in = input('enter a row: ').upper()
        if string_in == "QUIT":
            continue
        if len(string_in) != length1:
            print("input is not of same length")
            incorrect = True
        for i in set(string_in):
            if i not in dna_set:
                print("input is not correct")
                incorrect = True
                break
        if incorrect:
            continue
        else:
            other_strings.append(string_in)

    for i in range(0, len(string1)):
        total_col = 1
        total_difference = 0
        k = i
        j = i
        if j == 0:
            while string1[j] == '-':
                j += 1

        if string1[j] == '-':
            continue

        for string2 in other_strings:
            if k == 0:
                while string2[k] == '-':
                    k += 1
            if string2[k] == '-':
                continue
            total_difference += sneath_compare(string1[j], string2[k])
            total_col += 1
            k += 1

            # current_difference = sneath_compare(string1[i], string2[i])
            # print("difference between ", string1[i], "and ", string2[i], "is", current_difference)
        print(
            "the total difference for column {} is {}, the total number of amino acids is {}, t"
            "he average is {}".format(
                i,
                total_difference, total_col, total_difference / total_col))
        sheet1.write(col, 0, k)
        sheet1.write(col, 1, total_difference)
        sheet1.write(col, 2, total_difference / total_col)
        col += 1
    book.save("trial.xls")
