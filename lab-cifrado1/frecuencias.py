from collections import Counter
import re

ct = open("NOMBRE_ARCHIVO_CRIPTOGRAMA","r",encoding="utf-8").read()
solo = re.sub(r'[^A-Z]', '', ct)
print("Total letras:", len(solo))
print("\nLetras:", Counter(solo).most_common(12))

palabras = re.findall(r'[A-Z]+', ct)
cortas = [w for w in palabras if 1 < len(w) <= 3]
print("\nPalabras cortas:", Counter(cortas).most_common(10))
