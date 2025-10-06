import re
with open("NOMBRE_ARCHIVO_MENSAJE_CIFRADO","r",encoding="utf-8") as m:
    texto = m.read()
D={}

def descifrar(txt, mapa):
    out=[]
    for ch in txt:
        if ch in mapa:
            out.append(mapa[ch])
        elif 'A'<=ch<='Z':
            out.append('_')
        else:
            out.append(ch)
    return ''.join(out)

print(descifrar(texto, D))
