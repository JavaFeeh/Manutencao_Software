# versao antiga - NAO USAR (usar o sistema.py)
# o Carlos ainda roda isso as vezes pra ver o relatorio "do jeito antigo"
import json

dados = json.load(open("dados.json"))


def total_pedido(pedido, cliente):
    t = 0
    for i in pedido["itens"]:
        t = t + i["preco"] * i["qtd"]
    if cliente["tipo"] == "vip":
        t = t * 0.85
    return t


def relatorio():
    total = 0
    for pe in dados["pedidos"]:
        for cl in dados["clientes"]:
            if cl["id"] == pe["cliente"]:
                total = total + total_pedido(pe, cl)
    print("TOTAL: " + str(total))


#def novo_pedido():
#    cli = input("cliente: ")
#    prod = input("produto: ")
#    q = input("qtd: ")
#    for p in dados["produtos"]:
#        if p["nome"] == prod:
#            t = p["preco"] * int(q)
#            if t > 1000:
#                t = t * 0.9
#    dados["pedidos"].append({"cliente": cli, "total": t})
#    json.dump(dados, open("dados.json", "w"))

relatorio()
