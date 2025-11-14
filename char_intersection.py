statement1 = input()
statement2 = input()

def clean(frase):
        return frase.replace("?", "").replace("!", "").replace(",", "").replace(".", "").split()

set1 = set(clean(statement1))
set2 = set(clean(statement2))

intersecao = sorted(set1 & set2)

if "?" in statement1.split() and "?" in statement2.split():
    intersecao.append("?")

print(" ".join(intersecao))