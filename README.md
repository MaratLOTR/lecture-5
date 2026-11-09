# Поведенческие паттерны: умный дом

Структура повторяет проект лекции 3: четыре независимых папки паттернов,
демонстрации, задания, тесты, локальные схемы и HTML-шпаргалки.

| Паттерн | Материалы |
|---|---|
| Strategy — Стратегия | [patterns/strategy](patterns/strategy/README.md) |
| State — Состояние и автомат турникета | [patterns/state](patterns/state/README.md) |
| Observer — Наблюдатель | [patterns/observer](patterns/observer/README.md) |
| Memento — Снимок, самостоятельно | [patterns/memento](patterns/memento/README.md) |

## Быстрый запуск из корня

```bash
python3 -m patterns.strategy
python3 -m patterns.state
python3 -m patterns.observer
python3 -m patterns.memento
python3 -m pytest patterns/*/tests/test_example.py
```

Из любой папки паттерна: `python3 __main__.py`.
Её можно скопировать отдельно, сохранив имя папки и __init__.py.
Условия и команды проверок внутри каждой папки описаны в README.md и TASK.md.

Готовые примеры работают сразу. Основные задания FrostProtection, Arming,
HeatWarning и History оставлены студенту. Дополнительные задания находятся
в отдельных файлах с префиксом паттерна. Тесты заданий намеренно завершаются
ошибками до реализации, без skip и ожидаемых провалов. После выполнения заданий
все проверки должны проходить, включая исходные тесты примеров.

## Окружение и тесты

Нужен Python 3.10+ и pytest из requirements.txt. Основной способ проверки — pytest.
Классы unittest.TestCase распознаются pytest, как в проекте лекции 3.
Примеры используют стандартную библиотеку Python.

Проверка готовых примеров из корня:

```bash
python3 -m pytest patterns/*/tests/test_example.py
```

Из папки паттерна:

```bash
python3 -m pytest tests/test_example.py
python3 -m pytest tests/test_task.py
```

Для дополнительных заданий: `python3 -m pytest tests/test_extra.py`.
`python3 -m pytest` запускает все проверки. До выполнения заданий часть тестов
намеренно завершается FAILED. Готовые примеры должны проходить сразу.
Настройки VS Code и pytest.ini уже включены. Dev Container не устанавливает
пакеты автоматически.
