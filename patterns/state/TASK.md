# Задание: ожидание постановки на охрану

В security.py добавьте Arming(SecurityState). Измените переход Disarmed по arm:
теперь он ведёт в Arming. В Arming timeout переводит в Armed, disarm — в Disarmed,
а arm и motion сохраняют Arming. Сирена в Arming выключена.
Разрешите timeout в SecuritySystem.handle(). В остальных состояниях timeout
игнорируется. После timeout и motion должна сработать тревога.
Не меняйте Turnstile и тесты. test_example.py учитывает появление Arming: после
выполнения задания готовые примеры и тесты заданий должны проходить вместе.

## Дополнительная практика

state_entry_log.py: реализуйте LoggedSecuritySystem.transition_to(). Родитель
поддерживает сирену, подкласс записывает имя состояния только при смене его типа.
Проверьте tests/test_extra.py. Задание независимо от Arming.

## Проверка из папки паттерна

```bash
python3 -m pytest tests/test_task.py
```

Тесты заданий должны завершаться ошибками до реализации и проходить после неё.
