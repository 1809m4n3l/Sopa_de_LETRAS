# Función para buscar una palabra en la sopa de letras
def find_word(letter_soup, word):
    """
    Busca una palabra dentro de la sopa de letras en todas las direcciones posibles.

    Args:
        letter_soup (list): Matriz de caracteres representando la sopa de letras.
        word (str): Palabra a buscar en la sopa de letras.

    Returns:
        bool: True si la palabra fue encontrada, False en caso contrario.
    """
    rows = len(letter_soup)
    cols = len(letter_soup[0])
    word_len = len(word)

   
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    # Verificar desde cada posición de la matriz
    for i in range(rows):
        for j in range(cols):
            for direction in directions:
                dx, dy = direction
                count = 0
                for k in range(word_len):
                    ni, nj = i + k * dx, j + k * dy
                    # Verificar si la posición está fuera de los límites o no coincide
                    if 0 <= ni < rows and 0 <= nj < cols and letter_soup[ni][nj] == word[k]:
                        count += 1
                    else:
                        break
                
                if count == word_len:
                    return True

    return False  


def find_words(letter_soup, words):
    """
    Busca varias palabras en la sopa de letras.

    Args:
        letter_soup (list): Matriz de caracteres representando la sopa de letras.
        words (list): Lista de palabras a buscar.

    Returns:
        dict: Diccionario con las palabras como claves y un valor booleano indicando si se encontraron.
    """
    result = {}
    for word in words:
        result[word] = find_word(letter_soup, word)
    return result



def generate_report(letter_soup, words, output_path):
    """
    Genera un reporte en formato JSON indicando las palabras encontradas y no encontradas.

    Args:
        letter_soup (list): Matriz de caracteres representando la sopa de letras.
        words (list): Lista de palabras a buscar.
        output_path (str): Ruta donde se guardará el reporte en formato JSON.

    Returns:
        None
    """
    import json

    
    report = find_words(letter_soup, words)

    
    with open(output_path, "w") as file:
        json.dump(report, file, indent=4)

    print(f"Reporte generado en: {output_path}")



if __name__ == "__main__":
   
    letter_soup = [
        ['A', 'M', 'A', 'R', 'S'],
        ['S', 'T', 'E', 'R', 'I'],
        ['O', 'M', 'A', 'Z', 'C'],
        ['A', 'L', 'C', 'R', 'H'],
        ['P', 'O', 'L', 'O', 'S']
    ]

   
    words = ["AMAR", "OSA", "ATAR", "SOLO", "MEZCLAR", "PALO"]

    output_path = "reporte_sopa_de_letras.json"

    generate_report(letter_soup, words, output_path)
