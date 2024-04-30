from typing import List

def usar_la_fuerza(objeto: str, mochila: List[str],contador=0 ) -> str:
    
    if not mochila:
        return {
            f"no encontraste {objeto} en la mochila"
        }

    elif mochila[0] == "sable de luz":
        return f"el sable de luz fue encontrado: {contador}"

    else:
        return usar_la_fuerza(objeto, mochila[1:], contador + 1)

mochila_jedi = ["ropa", "comida", "herramientas", "sable de luz", "botiquín"]

print(usar_la_fuerza("sable de luz", mochila_jedi))
