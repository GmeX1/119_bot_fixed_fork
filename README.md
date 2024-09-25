
# 📚 Бот для бронирование 119 аудитории

Добро пожаловать в проект "Бот для бронирования 119 аудитории"! Этот бот предназначен для упрощения процесса бронирования 119 аудитории в вузе. Используя возможности библиотеки [Aiogram](https://docs.aiogram.dev/), мы создали удобный интерфейс для студентов.

## 📦 Установка

### Запуск с помощью Docker Compose

1. **Убедитесь, что у вас установлен Docker и Docker Compose.** Если они не установлены, следуйте [официальной документации](https://docs.docker.com/get-docker/) для установки.

2. **Клонируйте репозиторий:**
   
   `git clone https://github.com/username/repo-name.git`
   `cd repo-name`
   
3. **Настройте переменные окружения:**
   Создайте файл .env в корневой директории проекта и добавьте следующие строки:
   
   `BOT_TOKEN=your_bot_token_here`
   `DATABASE_URL=your_database_url_here`
   
4. **Запустите проект:**
   
   `docker-compose up -d --build`
   
5. **Остановите проект:**
   Чтобы остановить работающие контейнеры, используйте:
   
   `docker-compose down`
   
### Запуск без Docker

Если вы предпочитаете запускать проект без Docker, выполните следующие шаги:

1. Установите зависимости:
   
   `pip install -r requirements.txt`
   
2. Запустите бота:
   
   `python bot.py`


## 🚀 Описание проекта

Бот позволяет пользователям:
- Проверять доступное время для бронировния аудитории.
- Бронировать аудиторию на определенное время.
- Отменять бронирования.

## ⚙️ Технологии

- **Язык программирования**: Python
- **Библиотека для Telegram**: [Aiogram](https://docs.aiogram.dev/)
- **База данных**: SQLite

## 📱 Использование

1. Найдите бота в Telegram по имени, указанному при создании.
2. Начните диалог с ботом и следуйте инструкциям.
3. Бот предложит вам выбрать доступную аудиторию и время для бронирования.

## 🛠️ Функциональность

- **Бронирование**: Легко забронируйте нужную аудиторию с помощью простых команд.
- **Отмена бронирования**: Отмените бронирование в любое время.
- **Статус**: Получите актуальную информацию о свободных аудиториях.


## 🤝 Вклад

Если вы хотите внести свой вклад в проект, пожалуйста, создайте Pull Request или откройте Issue для обсуждения новых идей!

## 📞 Связь

Если у вас есть вопросы или предложения, не стесняйтесь обращаться:
- Email: lev.stremilov@gmail.com
- Telegram: @stremilovv

---

Спасибо за внимание! Надеемся, что наш бот поможет вам удобно и быстро бронировать аудитории!
