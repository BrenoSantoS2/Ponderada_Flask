import ctypes
import sys

def run_as_admin(command):
    try:
        # Chama a função ShellExecute do Windows para executar o comando como administrador
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, command, None, 1)
    except Exception as e:
        print(f"Erro ao executar como administrador: {e}")

if __name__ == "__main__":
    # Substitua 'server.py' pelo nome do script Python que você deseja executar como administrador
    script_name = "server.py"
    run_as_admin(script_name)