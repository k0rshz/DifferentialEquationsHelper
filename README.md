# Помощник в решении дифференциальных уравнений

Этот проект предоставляет веб-приложение для решения дифференциальных уравнений. Приложение позволяет пользователю загружать изображение, после чего уравнение на изображении распознаётся (временно отсутствует в этом репозитории). Пользователь может модифицировать уравнение, а затем получить его решение.

## Структура проекта

- **Frontend (Gradio)**: Интерфейс для взаимодействия с пользователем, через который можно загружать изображения и отправлять их на решение.
- **Backend (Flask)**: Серверная часть, которая обрабатывает запросы от фронтенда, взаимодействует с API Wolfram Alpha и выполняет распознавание уравнений (в этом репозитории последнее временно не предоставлено).
