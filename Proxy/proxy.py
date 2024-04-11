from subject import Subject

class Proxy(Subject):
    def __init__(self, real_subject: Subject, user_permissions: dict):
        self._real_subject = real_subject
        self._user_permissions = user_permissions

    def perform_action(self) -> None:
        user_permission = self._user_permissions.get("current_user")
        if user_permission and user_permission == 1:  # Aqui damos permissão somente para o usuário 1
            print("Accesso permitido.")
            self._real_subject.perform_action()
            self._log_access()
        else:
            print("Accesso negado.")

    def _log_access(self) -> None:
        print("Registrando acesso...")
