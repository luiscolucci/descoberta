import socket

def descobrir_hostname(ip):
    """
    Tenta descobrir o nome de host de um determinado endereço IP
    através de uma consulta DNS reversa.

    Args:
        ip (str): O endereço IP da máquina alvo.

    Returns:
        str: O nome do host se encontrado, ou uma mensagem de erro.
    """
    try:
        # socket.gethostbyaddr() faz a consulta DNS reversa.
        # Ele retorna uma tupla: (hostname, aliaslist, ipaddrlist)
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        # Esta exceção ocorre quando o host não é encontrado no DNS.
        return f"Não foi possível encontrar um nome de host para o IP {ip}. (Host não encontrado)"
    except socket.gaierror:
        # Esta exceção pode ocorrer para um endereço mal formatado.
        return f"Endereço IP inválido ou erro de resolução: {ip}"
    except Exception as e:
        # Captura outras exceções inesperadas.
        return f"Ocorreu um erro inesperado: {e}"

# --- Exemplo de Uso ---
if __name__ == "__main__":
    # Pede ao usuário para inserir o endereço IP
    ip_alvo = input("Digite o endereço IP que você deseja consultar: ")

    # Validação simples do input
    if not ip_alvo:
        print("Nenhum IP foi digitado. Encerrando.")
    else:
        print(f"\nBuscando nome de host para o IP: {ip_alvo}...")
        
        # Chama a função e imprime o resultado
        resultado = descobrir_hostname(ip_alvo)
        
        print(f"Resultado: {resultado}")