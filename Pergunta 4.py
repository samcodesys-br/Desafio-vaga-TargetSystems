

estados={67836.43,36678.66,29229.88,27165.48,19849.53}
soma=sum(estados)
percentual=[(uf/soma)*100 for uf in estados]
print("""Percentual de cada estado:
    SP – {:.2f}%
    RJ – {:.2f}%
    MG – {:.2f}%
    ES – {:.2f}%
    Outros – {:.2f}% 
""".format(percentual[0],percentual[1],percentual[2],percentual[3],percentual[4]))