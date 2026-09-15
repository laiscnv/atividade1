def buscar_binario(lista, num):
    inicio = 0
    fim = len(lista) - 1
    tentativas = 0
    
    while inicio <= fim:
        tentativas += 1
        meio = (inicio + fim) // 2
        numero_atual = lista[meio][0]
        
        if numero_atual == num:
            nome = lista[meio][1]     
            return nome, tentativas
        elif numero_atual < num:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return None, tentativas

def buscar_sequencial(lista, num):
    tentativas = 0
    for numero, nome in lista:
        tentativas += 1
        if numero == num:
            return nome, tentativas
    return None, tentativas

lista = [
    (3, 'Ana'), (10, 'Bruno'), (15, 'Carlos'), (18, 'Daniela'), (19, 'Eduardo'),
    (28, 'Fernanda'), (33, 'Gustavo'), (35, 'Helena'), (43, 'Igor'), (48, 'Juliana'),
    (58, 'Kleber'), (83, 'Larissa'), (84, 'Marcos'), (86, 'Natália'), (97, 'Otávio'),
    (104, 'Patrícia'), (106, 'Rafael'), (115, 'Sabrina'), (120, 'Tiago'), (122, 'Vanessa'),
    (127, 'Amanda'), (143, 'Breno'), (147, 'Camila'), (149, 'Diego'), (151, 'Eliane'),
    (175, 'Fabiano'), (179, 'Gabriela'), (184, 'Henrique'), (187, 'Isabela'), (194, 'João'),
    (199, 'Karen'), (201, 'Leonardo'), (211, 'Mirela'), (213, 'Nicolas'), (232, 'Olívia'),
    (241, 'Pedro'), (244, 'Queila'), (246, 'Rodrigo'), (256, 'Simone'), (258, 'Túlio'),
    (259, 'Ursula'), (261, 'Victor'), (269, 'Wesley'), (273, 'Xênia'), (278, 'Yasmin'),
    (280, 'Zeca'), (288, 'Alana'), (291, 'Caio'), (292, 'Diana'), (294, 'Fábio')
]

nome_bin, tent_bin = buscar_binario(lista, 256)
nome_seq, tent_seq = buscar_sequencial(lista, 256)

print(f"Busca Binária:   Nome = {nome_bin} | Tentativas = {tent_bin}")
print(f"Busca Sequencial: Nome = {nome_seq} | Tentativas = {tent_seq}")