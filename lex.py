import argparse
import socket as s
import logging
import threading as t

logging.basicConfig(level= logging.INFO)

def socketin(host, port):
    sock= s.socket(s.AF_INET, s.SOCK_STREAM)
    conexao= sock.connect_ex((host, port))

    if conexao == 0:
        logging.info(f"esta conexão deu certo. {port}")
            
    sock.close()

if __name__ == "__main__":
    parse= argparse.ArgumentParser()
    
    parse.add_argument("--host", help="permite voce escrever o host")
    parse.add_argument("--start_port", type= int, help="começo da porta")
    parse.add_argument("--end_port", type= int, help="fim da porta da porta")

    argumento= parse.parse_args()

    lista= []

    for loop in range(int(argumento.start_port), int(argumento.end_port)):

        thread= t.Thread(target= socketin, args= (argumento.host, loop))

        thread.start()

        lista.append(thread)

    for itera in lista:
        itera.join()