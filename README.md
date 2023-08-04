# Скрипт для исправления оценок в электронном дневнике

ВАЖНО! Проект разработан в рамках обучения и предназначен только для обучающих целей.

Этот репозиторий содержит скрипт, который позволяет исправлять оценки в школе, удалять замечания и добавлять похвальные комментарии учителей для указанного ученика и предмета в электронном дневнике школы.

## Краткое описание проекта

Этот проект создан для того, чтобы помочь ученику исправить свои оценки в электронном дневнике, убрать замечания учителей и добавить похвальные комментарии.

Для этого используется Python-скрипт, который можно запустить в консоли.

## Требования к окружению

* Python версии не ниже 3.7.
* Доступ к серверу с предварительно установленным сайтом электронного дневника.
* Файл базы данных от этого сайта.

## Подготовка к работе

1. Скачайте код из этого репозитория или выполните команду:

```bash
git clone https://github.com/StableBig/fix_diary.git
```

2. Положите скачанный файл `fix_diary.py` в ту же папку, где находится файл `manage.py` вашего сайта.

3. Запустите интерактивную Python-консоль следующей командой:

```bash
python3 manage.py shell
```

## Как использовать

В интерактивной консоли выполните следующие команды:

```bash
>>> from scripts.fix_diary import main
>>> main("Имя ученика", "Название предмета")
```

* Замените "Имя ученика" и "Название предмета" на нужные вам. (Эти данные хранятся в вашей базе данных.)

* Регистр важен, поэтому указываем имя ученика и предмета так, как они указаны в базе данных.

Например в базе данных содержится запись "Фролов Иван Геннадьевич" (имя ученика) и "Математика" (предмет).

Неверно:

```bash
>>> from scripts.fix_diary import main
>>> main("фролов иван геннадьевич", "математика")
```

Верно:

```bash
>>> from scripts.fix_diary import main
>>> main("Фролов Иван Геннадьевич", "Математика")
```

* Пишите имя так, как это указано в базе данных.

Например в базе данных содержится запись "Голубев Феофан Владленович" (имя ученика) и "Изобразительное искусство" (предмет).

Неверно:

```bash
>>> from scripts.fix_diary import main
>>> main("Феофан Владленович Голубев", "искусство Изобразительное")
```

Верно:

```bash
>>> from scripts.fix_diary import main
>>> main("Голубев Феофан Владленович", "Изобразительное искусство")
```

## Возможные ошибки и их решения

* Если вы не укажите имя ученика, вы получите сообщение об ошибке и предложение указать имя ученика. РЕШЕНИЕ: выполните команду снова с верными данными.
* Если вы введете имя ученика, которого нет в базе, вы получите сообщение об ошибке и предложение ввести другое имя. РЕШЕНИЕ: выполните команду снова с верными данными.
* Если вы не укажете предмет, вы получите сообщение об ошибке и предложение указать предмет. РЕШЕНИЕ: выполните команду снова с верными данными.
* Если вы введете название предмета, которого нет в базе, вы получите сообщение об ошибке и предложение ввести другое название предмета. РЕШЕНИЕ: выполните команду снова с верными данными.

## Ссылки

[Ссылка на сайт с репозиторием электронного дневника.](https://github.com/devmanorg/e-diary)

Используйте этот проекта с сайтом электронного дневника для подключения настоящего скрипта.

## Цели проекта

Код написан в учебных целях.
