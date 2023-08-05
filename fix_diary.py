from random import choice
from datacenter.models import Schoolkid, Mark, Chastisement, Commendation, Lesson, Subject


COMMENDATION_TEXTS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
]


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points=2).update(points=4)
    Mark.objects.filter(schoolkid=schoolkid, points=3).update(points=5)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid, subject_title):
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                   group_letter=schoolkid.group_letter,
                                   subject__title=subject_title).order_by('-date').first()
    if lesson is None:
        print(f"Уроки по предмету {subject_title} не найдены")
        return

    commendation_text = choice(COMMENDATION_TEXTS)
    Commendation.objects.create(text=commendation_text,
                                created=lesson.date,
                                schoolkid=schoolkid,
                                subject=lesson.subject,
                                teacher=lesson.teacher)


def main(full_name, subject_title):
    if not full_name:
        print("Вы не указали имя ученика")
        return
    if not subject_title:
        print("Вы не указали предмет")
        return

    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем {full_name} не найден")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено более одного ученика с именем {full_name}. Пожалуйста, укажите более полное имя.")
        return

    try:
        subject = Subject.objects.get(title=subject_title, year_of_study=schoolkid.year_of_study)
    except Subject.DoesNotExist:
        print(f"Предмет с названием {subject_title} не найден")
        return

    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendation(schoolkid, subject_title)
