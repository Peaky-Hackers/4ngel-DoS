# Requests Attack (BETA)

Um simulador de ataques HTTP básico em Python, permitindo testes de carga com solicitações POST em múltiplas threads. Ideal para experimentação e testes em ambientes controlados.

## Introdução

Este script em Python permite realizar solicitações HTTP GET e POST em grande escala para um URL especificado, utilizando diferentes agentes de usuário para cada requisição. É uma ferramenta poderosa para simular cenários de ataque lento (Slow HTTP Attack) e testar a resiliência de servidores web sob diferentes condições.


            | $$  | $$| $$$ | $$ /$$$$$$$           | $$        
            | $$  | $$| $$$$| $$| $$  \\ _/  /$$$$$$ | $$        
            | $$$$$$$$| $$ $$ $$| $$ /$$$$ /$$__  $$| $$        
            |_____  $$| $$  $$$$| $$|_  $$| $$$$$$$$| $$        
                  | $$| $$\\  $$$| $$  \\ $$| $$_____/| $$        
                  | $$| $$ \\  $$|  $$$$$$/|  $$$$$$$| $$$$$$$$  
                  |__/|__/  \\__/ \\______/  \\_______/|________/ BETA



## Funcionalidades
Solicitações GET: Envia múltiplas requisições GET para o URL alvo.

Solicitações POST: Envia múltiplas requisições POST com dados variados para o URL alvo.

Agentes de Usuário Aleatórios: Cada requisição utiliza um agente de usuário aleatório para simular diferentes navegadores/dispositivos.

Threading: Suporta múltiplas threads para maximizar a eficiência do ataque.

Desativação de Avisos SSL: Ignora avisos de SSL inseguros.

## Como Usar
Pré-requisitos

Python 3.6 ou superior

Instale as dependências com o comando:
```
pip install -r requirements.txt
```

## Execução

Clone este repositório:

```
git clone https://github.com/Peaky-Hackers/4ngel-DoS.git
cd 4ngel-DoS
```

Execute o script:

```
python main.py
```

Siga as instruções na tela:

Insira a URL alvo.

Escolha o número de solicitações por thread.

Defina o número de threads.

Selecione o método HTTP (GET ou POST).

## Links para os Repositórios

- Acesse a [versão com interface gráfica (GUI)](https://github.com/Peaky-Hackers/4ngel-DoS-GUI).

## Atenção

⚠️ Este script é uma ferramenta poderosa e deve ser usado apenas em ambientes controlados ou em servidores que você tem permissão para testar. O uso indevido desta ferramenta pode ser ilegal e levar a consequências graves. O autor não se responsabiliza por qualquer uso inadequado.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
