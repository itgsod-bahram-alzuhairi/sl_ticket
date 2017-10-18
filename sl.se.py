def fares(age, student=False, senior=False):
    if student or senior:
        return 'halv'
    else:
        if age < 20 or age> 65:
            return 'halv'
        else:
            return 'hel'



print 'barn 10',fares(10)
print 'pensionar 65',fares(65)
print 'sjukpensionar 47',fares(47,senior=True)
print 'student 20',fares(25,student=True)
print 'vuxen 45',fares(45)



