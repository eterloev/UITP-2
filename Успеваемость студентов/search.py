import os

class Examdata:
    def __init__(self, studentid, subjectname, examiner, date, result):
        self.studentid = studentid
        self.subjectname = subjectname
        self.examiner = examiner
        self.date = date
        self.result = result

class Student:
    def __init__(self, studentid, name, birthdate, examdata):
        self.studentid = studentid
        self.name = name
        self.birthdate = birthdate
        self.examdata = examdata

def collect_data():
    studentlist = []
    examdatamap = {}

    with open(os.getcwd()+'\\examdata', 'r', encoding='UTF8') as read:
        datalines = read.readlines()
        for i in range(len(datalines)):
            if (i > 0):
                splitted = datalines[i].split('";"')
                studentid_exam = splitted[0].replace('"','')
                subjectname = splitted[1].replace('"','')
                examiner = splitted[2].replace('"','')
                date = splitted[3].replace('"','')
                result = splitted[4].replace('"','')
                examdata = Examdata(studentid_exam, subjectname, examiner, date, result)

                if (examdatamap.get(studentid_exam) == None):
                    examdatamap.update({studentid_exam:[]})
                examlist = examdatamap[studentid_exam]
                examlist.append(examdata)
                examdatamap.update({studentid_exam:examlist})
    
    with open(os.getcwd()+'\\studentdata', 'r', encoding='UTF8') as read:
        datalines = read.readlines()
        for i in range(len(datalines)):
            if (i > 0):
                splitted = datalines[i].split('";"')
                studentid = splitted[0].replace('"','')
                name = splitted[1].replace('"','')
                birthdate = splitted[2].replace('"','')
                examdatalist = examdatamap[studentid]

                studentlist.append(Student(studentid, name, birthdate, examdatamap[studentid]))
                
    return studentlist


def get_best_student(studentlist):
    beststudent = None
    maxscore = 0
    for student in studentlist:
        totalscore = 0
        examcount = 0
        for exam in student.examdata:
            totalscore += int(exam.result)
            examcount += 1
        avgscore = totalscore/examcount
        if (maxscore < avgscore):
            maxscore = avgscore
            beststudent = student
    return beststudent


def printMenu():
    print("""Конвертер валют
1. Вывести ФИО студента с высшим баллом
2. Вывести инструкции снова
3. Выйти""")


command = '0'
studentdata = collect_data()

printMenu()

while command != '3':
    command = input("\n\nВведите номер команды: ")
    
    if command == '1':
        beststudent = get_best_student(studentdata)
        print("\nЛучший студент: "+beststudent.name)
        print("Оценки:")
        for exam in beststudent.examdata:
            print(exam.subjectname+" : "+exam.result)

    elif command == '2':
        printMenu()

    elif command == '3':
        print("Завершение работы...")

    else:
        print('Такой команды не существует')


