# **Персональний ВЕБ-Помічник**

## Застосунок на базі Веб-фреймворк Django:

дозволяє створювати контакти, додавати нотатки, працювати з файлами в локальному або хмарному сховищі, переглядати новини.

### Зміст проекту:

#### Загальна інформація

#### Технології

#### Встановлення та Налаштування

##### Загальна інформація

Це Ваш персональний веб-помічник, який допомагає:
- Переглядати Українські новини - тільки свіжі новини в категоріях: Спорт, IT-технології, Новини, курси валют
- Створювати Телефонну книгу - Телефонна книга контактів містить інформацію про контакт: телефон, електрону пошту, поштову адресу, день народження, тощо. 
- Дозволяє легко здійснювати пошук потрібного контакту, редагувати та видаляти контакт.
- Нагадує Вам про найближчі дні народження протягом тижня.
- Створювати Нотатки - додайте нотатку разом із заголовком і тегами. 
- Додаткові можливості: додавання нових тегів, швидкий пошук за тегами.
- Переглядати та сортувати файли в сховищі - додайте свій файл до галереї. Надає можливість простого та розширеного завантаження файлів, сортування всіх файлів за категоріями. Додаткові можливості: додавання книг з автором і обкладинками, а також додавання фотографій у фотогалерею.

#### Технології

Проект в основному базується на:

Веб-фреймворк: Django
Інтерфейс: HTML/CSS
Бекенд: Python і JavaScript
База данних: Postgres SQL

#### Встановлення та Налаштування

###### Перше, що потрібно зробити, це клонувати репозиторій:

`$ git clone git@github.com:lumi-ua/goit-project2-django-assistant.git`

###### Для успішної роботи із Веб-застосунком 

Створити базу данних PostgreSQL на локальному комп'ютері, або скориставшись безкоштовним веб-ресурсом (наприклад ElephantSQL).

Перевагу краще віддавати веб-ресурсам, це дозволить працювати із застосунком де завгодно.

Створити поштову скриньку на безкоштовних веб-ресурсах для відновлення паролю.

Створити обліковий запис на хмарному сховищі, для зберігання власних файлів. (наприклад Dropbox)

Отримати API_KEY з сайту [https://home.openweathermap.org/api_keys]() 

###### Після цього 

В теці застосунку personal_assistant необхідно необхідно створити файл .env, по аналогії з файлом .env.example, де необхідно 
заповнити персональну інформацію про підключення до всіх вище перерахованих ресурсів.

#### Запуск застосунку
Активуємо та запускаємо віртуальне середовище:

`$ poetry shell`

`(venv)$ poetry install`

Після встановлення всіх необхідних пакетів застосунок готовий до налаштування

Переходимо в теку застосунку

`$ cd personal_assistant`

`(venv)$ Base_dir\personal_assistant>`

Створюємо в нашій базі данних таблиці, де будуть зберігатися наші контакти, нотатки, користувачі, інформація про файли в сховищі.

`(venv)$ base_dir\personal_assistant\python manage.py migrate`

Запускаємо сервер 

`(venv)$ python manage.py runserver`

Переходимо за посиланням

[http://127.0.0.1:8000/]()

Застосунок працює.
