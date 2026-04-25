

# Запуск проекта

## Установка и настройка вирртуального окружения
```bash
python3 -m venv .venv # Mac OS
python -m venv venv   # Windows
```

**Что делает:**
- Создает виртуальное окружение Python в папке `venv`. Это изолирует зависимости проекта от глобавльных пакетов.

## Активация окружения
```bash
Linux
source .venv/bin/activate
Windows
source venv/Scripts/activate
```
**Что делает**
- Активирует виртуальное окружение. После активации в терминале появится ``(.venv)

## Установка зависимостей
```bash
pip install -r requirements.txt
```

**Что делает:**
- Устанавливает все пакеты из файла requirements.txt (Django и др.)