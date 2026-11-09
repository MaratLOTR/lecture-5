# Memento — Снимок (самостоятельно)

## Пример из лекции

SceneSettings хранит яркость, целевую температуру и список строк с именами устройств.
save() создаёт неизменяемый SceneSnapshot, restore() восстанавливает настройки.
Originator — SceneSettings, Memento — SceneSnapshot, Caretaker — History (задание).
История должна хранить снимки и управлять ими через save()/restore(), не читая поля снимка.

Список устройств превращается в tuple: последующее изменение исходного списка
не изменяет снимок. restore() создаёт новый список, поэтому повторное восстановление
тоже независимо. Для вложенных изменяемых объектов понадобился бы другой способ
копирования. Поля с подчёркиванием закрыты по соглашению Python, а не защищены от чтения.
restore() принимает SceneSnapshot, иначе TypeError; снимки совместимы между сценами.
Проверку диапазонов яркости и температуры пример не выполняет: используются корректные
настройки. Восстановление объекта не отменяет команды реальному оборудованию.

## Материалы

- [scene.py](scene.py) — готовый пример и место основного задания.
- [__main__.py](__main__.py) — демонстрация.
- [TASK.md](TASK.md) — условия учебного задания.
- [tests/test_example.py](tests/test_example.py) — тесты готового примера.
- [tests/test_task.py](tests/test_task.py) — тесты основного задания.
- [memento_limited_history.py](memento_limited_history.py) — дополнительная практика.
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
Дополнительная проверка: `python3 -m pytest tests/test_extra.py`.
