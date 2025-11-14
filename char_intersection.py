statement1 = input()
statement2 = input()

def limpar(frase):
        return frase.replace("?", "").replace("!", "").replace(",", "").replace(".", "").split()

set1 = set(limpar(statement1))
set2 = set(limpar(statement2))

intersecao = sorted(set1 & set2)

if "?" in statement1.split() and "?" in statement2.split():
    intersecao.append("?")

print(" ".join(intersecao))