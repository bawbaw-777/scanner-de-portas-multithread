# Port Scanner

Ferramenta de linha de comando para escanear portas abertas em um host, desenvolvida em Python. Utiliza threads para realizar varreduras de forma rápida e eficiente.

---

## Sobre o projeto

Este projeto foi desenvolvido para fins de estudo em redes e segurança da informação. O scanner verifica quais portas TCP estão abertas em um determinado host dentro de um intervalo definido pelo usuário, usando múltiplas threads para acelerar o processo.

---

## Tecnologias utilizadas

- Python 3
- `socket` — comunicação TCP com o host alvo
- `threading` — varredura paralela das portas
- `argparse` — interface de linha de comando
- `logging` — exibição organizada dos resultados

---

## Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/bawbaw-777/scanner-de-portas-multithread.git
cd scanner-de-portas-multithread
```

### 2. Execute o scanner

```bash
python port_scanner.py --host <endereço> --start_port <porta_inicial> --end_port <porta_final>
```

### Exemplo

```bash
python port_scanner.py --host 192.168.1.1 --start_port 1 --end_port 1024
```

### Saída esperada

```
INFO:root:esta conexão deu certo. 80
INFO:root:esta conexão deu certo. 443
```

---

## Parâmetros

| Parâmetro | Descrição |
|---|---|
| `--host` | Endereço IP ou domínio do alvo |
| `--start_port` | Porta inicial do intervalo |
| `--end_port` | Porta final do intervalo |

---

## Aviso legal

Esta ferramenta foi desenvolvida exclusivamente para fins educacionais e testes em redes próprias ou com autorização explícita. O uso não autorizado em redes de terceiros é ilegal.

---

## Autor

Feito por [bawbaw-777](https://github.com/bawbaw-777)
