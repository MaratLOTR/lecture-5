# Strategy — Стратегия

## Пример из лекции

Термостат хранит стратегию HeatingStrategy и делегирует ей power(current, target).
HeatingStrategy — абстрактный класс ABC с abstractmethod. Eco и Comfort наследуют его.
Eco возвращает 40%, когда температура ниже цели, иначе 0%. Comfort возвращает разницу
температур, умноженную на 30, с ограничением от 0 до 100%. set_strategy() меняет
алгоритм у существующего Thermostat. При 19 и 22 °C результаты: 40 и 90%.

Роли: Thermostat — Context, HeatingStrategy — Strategy, Eco/Comfort — ConcreteStrategy,
код демонстрации — Client. Контекст работает через общий интерфейс и не перечисляет
конкретные алгоритмы. Стратегии нужны для независимого изменения алгоритмов.
Для двух стабильных веток обычная функция с if может быть проще.
Алгоритмы учебные и не являются физической моделью отопления.

## Материалы

- [heating.py](heating.py) — готовый пример и место основного задания.
- [__main__.py](__main__.py) — демонстрация.
- [TASK.md](TASK.md) — условия учебного задания.
- [tests/test_example.py](tests/test_example.py) — тесты готового примера.
- [tests/test_task.py](tests/test_task.py) — тесты основного задания.

- [docs/diagrams.md](docs/diagrams.md) — схемы.
- [docs/cheatsheet.html](docs/cheatsheet.html) — шпаргалка с кодом и тестами.

## Запуск из этой папки

```bash
python3 __main__.py
python3 -m pytest tests/test_example.py
python3 -m pytest tests/test_task.py
```

Нужен Python 3.10+ и pytest из requirements.txt. Тесты запускаются через pytest.
Классы unittest.TestCase совместимы с pytest, как в проекте лекции 3.
Готовый пример проходит сразу. Задания намеренно не реализованы: сначала прочитайте
TASK.md, затем добейтесь прохождения тестов без пропусков.
