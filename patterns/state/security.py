"""State: охрана и простой конечный автомат турникета."""

class SecuritySystem:
    def __init__(self):
        self.state = Disarmed()
        self.siren = False

    def transition_to(self, state):
        self.state = state
        self.siren = isinstance(state, Alarm)

    def handle(self, event):
        if event not in {"arm", "motion", "disarm"}:
            raise ValueError(event)
        self.state.handle(self, event)

class SecurityState:
    def handle(self, context, event):
        raise NotImplementedError

class Disarmed(SecurityState):
    def handle(self, context, event):
        if event == "arm":
            context.transition_to(Armed())
        # motion и disarm: без изменений

class Armed(SecurityState):
    def handle(self, context, event):
        if event == "motion":
            context.transition_to(Alarm())
        elif event == "disarm":
            context.transition_to(Disarmed())

class Alarm(SecurityState):
    def handle(self, context, event):
        if event == "disarm":
            context.transition_to(Disarmed())

class Turnstile:
    """Правила из лекции. Событие passage означает попытку пройти."""

    def __init__(self):
        self.state = "locked"

    def handle(self, event):
        if event not in {"coin", "passage"}:
            raise ValueError(event)
        if self.state == "locked":
            if event == "coin":
                self.state = "unlocked"
                return "open"
            return "blocked"
        if event == "passage":
            self.state = "locked"
            return "pass_and_close"
        return "return_coin"

# ЗАДАНИЕ: добавьте Arming и обработку timeout, см. TASK.md.
