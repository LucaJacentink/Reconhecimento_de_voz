from typing import Dict


def write_report( path: str, nome: str, acerto: "str", chute:"str", distancia:float, distancia_individual) -> None:
    """ escreve o arquivo de relatorio do experimento """
    relatorio = open(path, 'w')
    relatorio.write(f'Nome:{nome}\n'
                    f'Acertou? {acerto}\n'
                    f"Chute: {chute}\n"
                    f'Distancia: {distancia:.2f}\n'
                    f"Menor distancia individual: {distancia_individual}")