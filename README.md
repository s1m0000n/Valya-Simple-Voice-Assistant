# Валя - простой голосовой ассистент
Данный проект - часть доклада про построение простого голосового ассистента и в большей степени посвящён рассмотрению возможностей библиотек Python для распознавания речи и генерации речи по тексту на русском языке. Код обработки естественного языка - довольно медленный и не предоставляет гибких возможностей, но он лишь для примера.
Презентация: https://docs.google.com/presentation/d/1tCUSbKBlnvmMcx3yQhRrmCamL6jyi1VSseDhiBc17WI/edit?usp=sharing

## Установка и использование для Linux и macOS

Убедитесь, что у вас есть Python 3.7 и новее
Если его нет, то установите из системных репозиториев или согласно инструкциям на сайте

### Создайте виртуальное окружение и войдите в него(опционально, желательно)
```
python3 -m venv venv
source venv/bin/activate
```

### Установка зависимостей
`pip3 install -r requirements.txt`

### Запуск
`python3 main.py`

### Проблемы с работой
Скорее всего проблемы с `pyaudio`, поскольку ей нужна ещё одна системная зависимость
Попробуйте установить `portaudio` на macOS через brew или через ваш пакетный менеджер в Linux
https://pypi.org/project/PyAudio/
