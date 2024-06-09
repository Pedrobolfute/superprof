import subprocess
import shutil
import os
import time
import threading

home_dir = os.getenv('HOME')

def check_and_install_pv():
    if shutil.which("pv") is None:
        print("pv não está instalado. Instalando...")
        try:
            subprocess.run(["sudo", "yum", "install", "-y", "pv"], check=True)
            print("pv instalado com sucesso.")
        except subprocess.CalledProcessError as e:
            print("Falha ao instalar o pv:", e)
            exit(1)
    else:
        print("pv já está instalado.")

def get_available_space(path="/"):
    try:
        result = subprocess.run(["df", "-k", "--output=avail", path], capture_output=True, text=True, check=True)
        lines = result.stdout.splitlines()
        if len(lines) > 1:
            available_kb = int(lines[1])
            return available_kb
        else:
            raise Exception("Erro ao obter espaço disponível")
    except subprocess.CalledProcessError as e:
        print("Erro ao obter informações sobre o espaço disponível:", e)
        return None

def fill_disk_slowly(file_path, duration_seconds):
    check_and_install_pv()
    
    available_kb = get_available_space("/")
    if available_kb is None:
        return
    
    # Calcular a taxa de preenchimento em KB/s
    rate_kb = available_kb // duration_seconds

    try:
        command = f"(timeout {duration_seconds}s pv -L {rate_kb}k /dev/zero > {file_path}; rm {file_path})"
        print(f"Executando comando: {command}")
        subprocess.run(command, shell=True, check=True)
        print("Espaço preenchido e arquivo removido com sucesso.")
    except subprocess.CalledProcessError as e:
        print("Falha ao preencher o espaço em disco:", e)

def get_disk_usage(path="/"):
    try:
        result = subprocess.run(["df", "-h", path], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Erro ao obter informações sobre o uso do disco:", e)
        return None

def monitor_disk_usage(interval=5, duration=60, path="/"):
    end_time = time.time() + duration
    while time.time() < end_time:
        usage = get_disk_usage(path)
        if usage:
            os.system('clear')  # Limpa o terminal para melhor visualização
            print(usage)
        else:
            print("Erro ao obter informações sobre o uso do disco.")
        time.sleep(interval)

def fill_and_monitor(file_path, fill_duration_seconds, monitor_path="/home", monitor_interval=5):
    monitor_thread = threading.Thread(target=monitor_disk_usage, args=(monitor_interval, fill_duration_seconds, monitor_path))
    
    # Inicia a thread de monitoramento
    monitor_thread.start()
    
    # Executa a função de preenchimento
    fill_disk_slowly(file_path, fill_duration_seconds)
    
    # Espera a thread de monitoramento terminar
    monitor_thread.join()

# Exemplo de uso
fill_and_monitor(f"{home_dir}/evento.txt", fill_duration_seconds=1800, monitor_path="/home", monitor_interval=5)
