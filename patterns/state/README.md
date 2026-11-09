# State — Состояние

## Пример из лекции

SecuritySystem хранит текущее состояние и делегирует ему handle(context, event).
Disarmed, Armed и Alarm задают разные реакции на arm, motion и disarm.
В Disarmed движение игнорируется, в Armed вызывает Alarm. В Alarm сирена работает
до disarm. transition_to() синхронизирует состояние и сирену. Повторные команды
сохраняют состояние. Неизвестное событие вызывает ValueError без изменений.

Роли: SecuritySystem — Context, SecurityState — базовый контракт (метод вызывает
NotImplementedError), Disarmed/Armed/Alarm — ConcreteState. Правила переходов здесь
находятся в самих состояниях. Новые экземпляры создаются при переходе.
Прямое присваивание state обходит синхронизацию сирены: используйте transition_to().

Turnstile — простой конечный автомат из лекции: locked/unlocked и события coin/passage.
coin открывает заблокированный турникет, passage после оплаты пропускает и закрывает.
Попытка без оплаты блокируется, повторная монета при открытом проходе возвращается.
Результаты handle(): open, blocked, pass_and_close, return_coin.
Это отдельная реализация через условия: машина состояний — модель, State — способ
организовать её код. Наличие автомата не обязывает создавать классы состояний.

## Материалы

- [security.py](security.py) — готовый пример и место основного задания.
- [__main__.py](__main__.py) — демонстрация.
- [TASK.md](TASK.md) — условия учебного задания.
- [tests/test_example.py](tests/test_example.py) — тесты готового примера.
- [tests/test_task.py](tests/test_task.py) — тесты основного задания.
- [state_entry_log.py](state_entry_log.py) — дополнительная практика.
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
