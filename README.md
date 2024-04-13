# Тестовое задание Авито QA

| ВАЖНО: ИСПОЛЬЗУЙТЕ PYTHON 3.12.x |
| -------------------------------- |

## Подготовка среды для тестирования

1. Склонируйте к себе репозиторий

```
git clone https://github.com/diananek/qa-tests.git
```

2. Установите виртуальное окружение

```
python -m venv venv
```

3. Активируйте виртуальное окружение

- **_На ОС Windows_**:

```Windows
.\venv\Scripts\activate
```

- **_На ОС Linux, MacOS_**:

```Linux, MacOS
source venv/bin/activate
```

4. Обновите pip

```
python.exe -m pip install --upgrade pip
```

5. Установите зависимости для запуска тестов

```
pip install -r requirements.txt
```

## Запуск тестов

**Запустите тесты** в консоли командой `pytest` или `pytest --headed`

## Структура проекта

**TASK1.md** — файл задания №1  
**TESTCASES.md** - тест-кейсы для задания №2  
**test_avito-page.py** - тесты для задания №2  
**test_data_base.json** - базовые тестовые данные для задания №2  
**BUGREPORT.md** - баг-репорт для задания №2  
**output** - папка для скриншотов тестов
