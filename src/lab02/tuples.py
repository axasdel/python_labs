rec = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)


def fio(rec):
    if len(rec[0]) > 0:
        fio = rec[0].split()
        initials = "".join(l[0] for l in fio).upper()
        if len(initials) == 3:
            return (
                fio[0][0].upper()
                + fio[0][1:]
                + " "
                + initials[1]
                + "."
                + initials[2]
                + "."
            )
        elif len(initials) == 2:
            return fio[0][0].upper() + fio[0][1:] + " " + initials[1] + "."
        else:
            return fio[0][0].upper() + fio[0][1:]
    else:
        raise ValueError


def gpa(rec):
    if len(str(rec[2])) > 0:
        return round(rec[2], 2)
    else:
        raise ValueError


def format_record(rec):
    if tuple(rec) == rec:
        if len(str(rec[1])) > 0:
            res = (
                fio(rec)
                + ","
                + " "
                + "гр."
                + rec[1]
                + ","
                + " "
                + "GPA"
                + " "
                + str(gpa(rec))
            )
            print(res)
        else:
            raise ValueError


format_record(rec)
