def classify_mark(mark):
    if not isinstance(mark, int):
        raise TypeError("Invalid type")
    if mark < 0 or mark > 100:
        raise ValueError
    if mark<=39:
         return"Fail"
    if mark>=40 and mark<=69:
         return"Pass"
    if mark>=70 & mark<=100:
            return"Distinction"
    else:
        print("Error")
        return int(mark)
#-------------------------------#


fail_count=0
distinction_count=0

def calculate_summary(marks):
    if len(marks) == 0:
        return [0, 0.0, 0, 0]

    total=0
    fail_count = 0
    distinction_count = 0

    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError
        total+= mark
        if mark < 40:
            fail_count += 1
        if mark >= 70:
            distinction_count += 1

    average=0.0
    average = total / len(marks)


    return [total, average, fail_count, distinction_count]











#------------------------#














