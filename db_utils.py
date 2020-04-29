def fix_marks(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
        school_grades = [4, 5]
        for mark in marks:
            mark.points = random.choise(school_grades)
            mark.save(update_fields['points'])
    except ObjectDoesNotExist:
        print("Can`t find this schoolboy")


def remove_chastisements(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
        for chastisement in chastisement:
            chastisement.delete()
    except ObjectDoesNotExist:
        print("Can`t find this schoolboy")


def create_commendation(subject, schoolkid_name):
    compliments = [
        'Молодец!',
        'Отлично!',
        'Самый лучший ученик!',
        'Очень хороший ответ!',
        'Ты сегодня прыгнул выше головы!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!'
    ]
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        lessons = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter,
                                        subject__title__contains=subject)
        commendations = Commendation.objects.filter(schoolkid=child, subject__title__contains=subject)
        commendations.create(text=random.choice(compliments), created=lessons[0].date, schoolkid=child,
                             subject=lessons[0].subject, teacher=lessons[0].teacher)
    except ObjectDoesNotExist:
        print("Can`t find this schoolboy")