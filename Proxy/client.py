from real_subject import RealSubject
from proxy import Proxy

if __name__ == "__main__":
    real_subject = RealSubject()

    proxy = Proxy(real_subject, {"current_user": 1})  # Esperamos que este usuário seja aceito
    print("Tentando fazer ação confidencial...")
    proxy.perform_action()

    proxy = Proxy(real_subject, {"current_user": 2})
    print("\nTentando fazer ação confidencial...")
    proxy.perform_action()  # Esperamos que este usuário seja negado
