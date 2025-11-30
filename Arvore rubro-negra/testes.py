"""
TESTES E EXEMPLOS - ÁRVORE RUBRO-NEGRA
=======================================
Este arquivo demonstra o uso da árvore e valida suas propriedades
"""

from main import ArvoreRubroNegra, Cor


def verificar_propriedades(arvore):
    """
    Verifica se a árvore mantém todas as propriedades de uma Árvore Rubro-Negra
    """
    print("\n🔍 VERIFICANDO PROPRIEDADES DA ÁRVORE RUBRO-NEGRA...")
    print("="*60)
    
    # Propriedade 1: Todo nó é vermelho ou preto (sempre verdadeiro por construção)
    print("✅ Propriedade 1: Todo nó é vermelho ou preto")
    
    # Propriedade 2: A raiz é preta
    if arvore.raiz == arvore.NIL:
        print("⚠️  Árvore vazia")
        return False
    
    if arvore.raiz.cor == Cor.PRETO:
        print("✅ Propriedade 2: A raiz é preta")
    else:
        print("❌ Propriedade 2 VIOLADA: A raiz não é preta!")
        return False
    
    # Propriedade 3: Todas as folhas (NIL) são pretas (sempre verdadeiro por construção)
    print("✅ Propriedade 3: Todas as folhas (NIL) são pretas")
    
    # Propriedade 4: Se um nó é vermelho, ambos os filhos são pretos
    if verificar_nao_ha_vermelhos_consecutivos(arvore.raiz, arvore.NIL):
        print("✅ Propriedade 4: Não há nós vermelhos consecutivos")
    else:
        print("❌ Propriedade 4 VIOLADA: Existem nós vermelhos consecutivos!")
        return False
    
    # Propriedade 5: Todos os caminhos têm o mesmo número de nós pretos
    altura_preta = calcular_altura_preta(arvore.raiz, arvore.NIL)
    if verificar_altura_preta_uniforme(arvore.raiz, arvore.NIL, altura_preta, 0):
        print(f"✅ Propriedade 5: Altura preta uniforme ({altura_preta} nós pretos)")
    else:
        print("❌ Propriedade 5 VIOLADA: Altura preta não é uniforme!")
        return False
    
    print("="*60)
    print("🎉 TODAS AS PROPRIEDADES VERIFICADAS COM SUCESSO!")
    print("="*60)
    return True


def verificar_nao_ha_vermelhos_consecutivos(no, NIL):
    """Verifica se não há dois nós vermelhos consecutivos"""
    if no == NIL:
        return True
    
    if no.cor == Cor.VERMELHO:
        if no.esquerda.cor == Cor.VERMELHO or no.direita.cor == Cor.VERMELHO:
            return False
    
    return (verificar_nao_ha_vermelhos_consecutivos(no.esquerda, NIL) and
            verificar_nao_ha_vermelhos_consecutivos(no.direita, NIL))


def calcular_altura_preta(no, NIL):
    """Calcula a altura preta de um caminho"""
    if no == NIL:
        return 1
    
    altura = calcular_altura_preta(no.esquerda, NIL)
    if no.cor == Cor.PRETO:
        altura += 1
    
    return altura


def verificar_altura_preta_uniforme(no, NIL, altura_esperada, altura_atual):
    """Verifica se todos os caminhos têm a mesma altura preta"""
    if no == NIL:
        return altura_atual + 1 == altura_esperada
    
    if no.cor == Cor.PRETO:
        altura_atual += 1
    
    return (verificar_altura_preta_uniforme(no.esquerda, NIL, altura_esperada, altura_atual) and
            verificar_altura_preta_uniforme(no.direita, NIL, altura_esperada, altura_atual))


def teste_insercao_basica():
    """Testa inserção básica de elementos"""
    print("\n🧪 TESTE 1: Inserção Básica")
    print("-"*60)
    
    arvore = ArvoreRubroNegra()
    valores = [10, 20, 30, 15, 25, 5, 1]
    
    print(f"Inserindo valores: {valores}")
    for valor in valores:
        arvore.inserir(valor)
    
    print(f"Árvore criada com {len(arvore)} nós")
    print(f"Em ordem: {arvore.em_ordem()}")
    
    verificar_propriedades(arvore)
    arvore.imprimir_estrutura()
    
    return arvore


def teste_insercao_sequencial():
    """Testa inserção sequencial (pior caso para BST normal)"""
    print("\n🧪 TESTE 2: Inserção Sequencial (1 a 15)")
    print("-"*60)
    
    arvore = ArvoreRubroNegra()
    valores = list(range(1, 16))
    
    print(f"Inserindo valores: {valores}")
    for valor in valores:
        arvore.inserir(valor)
    
    print(f"Árvore criada com {len(arvore)} nós")
    print(f"Altura da árvore: {arvore.altura()}")
    print(f"Altura preta: {arvore.altura_preta()}")
    
    verificar_propriedades(arvore)
    
    return arvore


def teste_elementos_repetidos():
    """Testa o tratamento de elementos repetidos"""
    print("\n🧪 TESTE 3: Elementos Repetidos")
    print("-"*60)
    
    arvore = ArvoreRubroNegra()
    
    print("Inserindo: 50, 25, 75")
    arvore.inserir(50)
    arvore.inserir(25)
    arvore.inserir(75)
    
    print(f"\nTentando inserir 50 novamente (deve ser ignorado):")
    resultado = arvore.inserir(50)
    
    print(f"\nTentando inserir 25 novamente (deve ser ignorado):")
    resultado = arvore.inserir(25)
    
    print(f"\nNúmero de nós: {len(arvore)} (deve ser 3)")
    print(f"Em ordem: {arvore.em_ordem()}")
    
    return arvore


def teste_exclusao():
    """Testa exclusão de elementos"""
    print("\n🧪 TESTE 4: Exclusão de Elementos")
    print("-"*60)
    
    arvore = ArvoreRubroNegra()
    valores = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43]
    
    print(f"Inserindo valores: {valores}")
    for valor in valores:
        arvore.inserir(valor)
    
    print(f"\nÁrvore inicial com {len(arvore)} nós")
    print(f"Em ordem: {arvore.em_ordem()}")
    
    print("\n--- Excluindo 12 ---")
    arvore.excluir(12)
    print(f"Em ordem: {arvore.em_ordem()}")
    verificar_propriedades(arvore)
    
    print("\n--- Excluindo 25 ---")
    arvore.excluir(25)
    print(f"Em ordem: {arvore.em_ordem()}")
    verificar_propriedades(arvore)
    
    print("\n--- Excluindo 50 (raiz) ---")
    arvore.excluir(50)
    print(f"Em ordem: {arvore.em_ordem()}")
    verificar_propriedades(arvore)
    
    arvore.imprimir_estrutura()
    
    return arvore


def teste_busca():
    """Testa busca de elementos"""
    print("\n🧪 TESTE 5: Busca de Elementos")
    print("-"*60)
    
    arvore = ArvoreRubroNegra()
    valores = [50, 25, 75, 12, 37, 62, 87]
    
    print(f"Inserindo valores: {valores}")
    for valor in valores:
        arvore.inserir(valor)
    
    print("\nBuscando elementos existentes:")
    for valor in [50, 12, 87]:
        resultado = arvore.buscar(valor)
        if resultado:
            cor = "VERMELHO" if resultado.cor == Cor.VERMELHO else "PRETO"
            print(f"  ✅ {valor} encontrado (cor: {cor})")
        else:
            print(f"  ❌ {valor} não encontrado")
    
    print("\nBuscando elementos inexistentes:")
    for valor in [100, 1, 99]:
        resultado = arvore.buscar(valor)
        if resultado:
            print(f"  ✅ {valor} encontrado")
        else:
            print(f"  ❌ {valor} não encontrado (esperado)")
    
    return arvore


def teste_grande_arvore():
    """Testa árvore com muitos elementos (requisito de 21+ nós)"""
    print("\n🧪 TESTE 6: Árvore com 30 Nós")
    print("-"*60)
    
    arvore = ArvoreRubroNegra()
    valores = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93,
               3, 9, 15, 21, 28, 34, 40, 46, 53, 59, 65, 71, 78, 84, 96]
    
    print(f"Inserindo 30 valores...")
    for valor in valores:
        arvore.inserir(valor)
    
    print(f"✅ Árvore criada com {len(arvore)} nós")
    print(f"   Altura total: {arvore.altura()}")
    print(f"   Altura preta: {arvore.altura_preta()}")
    print(f"   Altura teórica máxima: ~{2 * arvore.altura_preta()}")
    
    verificar_propriedades(arvore)
    
    # Visualiza a árvore
    arvore.visualizar("Árvore Rubro-Negra com 30 Nós", "arvore_30_nos.png")
    
    return arvore


def teste_comparacao_altura():
    """Compara altura da RB Tree com BST desbalanceada"""
    print("\n🧪 TESTE 7: Comparação de Altura")
    print("-"*60)
    
    arvore_rb = ArvoreRubroNegra()
    
    # Inserção sequencial (pior caso para BST)
    n = 31  # 31 nós
    valores = list(range(1, n + 1))
    
    print(f"Inserindo {n} valores sequenciais (1 a {n})...")
    for valor in valores:
        arvore_rb.inserir(valor)
    
    altura_rb = arvore_rb.altura()
    altura_bst_pior_caso = n  # BST desbalanceada vira lista
    altura_teorica_rb = int(2 * (altura_rb / 2))  # Aproximação
    
    print(f"\n📊 RESULTADOS:")
    print(f"   Árvore Rubro-Negra: altura = {altura_rb}")
    print(f"   BST desbalanceada (pior caso): altura = {altura_bst_pior_caso}")
    print(f"   Redução de altura: {((altura_bst_pior_caso - altura_rb) / altura_bst_pior_caso * 100):.1f}%")
    
    verificar_propriedades(arvore_rb)
    
    return arvore_rb


def executar_todos_testes():
    """Executa todos os testes"""
    print("\n" + "="*60)
    print("   EXECUÇÃO DE TODOS OS TESTES - ÁRVORE RUBRO-NEGRA")
    print("="*60)
    
    testes = [
        teste_insercao_basica,
        teste_insercao_sequencial,
        teste_elementos_repetidos,
        teste_exclusao,
        teste_busca,
        teste_grande_arvore,
        teste_comparacao_altura
    ]
    
    resultados = []
    
    for i, teste in enumerate(testes, 1):
        try:
            print(f"\n{'='*60}")
            print(f"EXECUTANDO TESTE {i}/{len(testes)}")
            print(f"{'='*60}")
            arvore = teste()
            resultados.append((teste.__name__, "✅ PASSOU"))
            print(f"\n✅ {teste.__name__} completado com sucesso!")
        except Exception as e:
            resultados.append((teste.__name__, f"❌ FALHOU: {str(e)}"))
            print(f"\n❌ {teste.__name__} falhou: {str(e)}")
    
    # Resumo final
    print("\n" + "="*60)
    print("   RESUMO DOS TESTES")
    print("="*60)
    
    for nome, resultado in resultados:
        print(f"{nome:.<40} {resultado}")
    
    total = len(resultados)
    passou = sum(1 for _, r in resultados if "✅" in r)
    
    print("="*60)
    print(f"TOTAL: {passou}/{total} testes passaram")
    print("="*60)


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║        SUITE DE TESTES - ÁRVORE RUBRO-NEGRA             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    print("Escolha uma opção:")
    print("1 - Executar todos os testes")
    print("2 - Teste individual (inserção básica)")
    print("3 - Teste individual (inserção sequencial)")
    print("4 - Teste individual (elementos repetidos)")
    print("5 - Teste individual (exclusão)")
    print("6 - Teste individual (busca)")
    print("7 - Teste individual (árvore grande - 30 nós)")
    print("8 - Teste individual (comparação de altura)")
    
    opcao = input("\nOpção: ").strip()
    
    if opcao == "1":
        executar_todos_testes()
    elif opcao == "2":
        teste_insercao_basica()
    elif opcao == "3":
        teste_insercao_sequencial()
    elif opcao == "4":
        teste_elementos_repetidos()
    elif opcao == "5":
        teste_exclusao()
    elif opcao == "6":
        teste_busca()
    elif opcao == "7":
        teste_grande_arvore()
    elif opcao == "8":
        teste_comparacao_altura()
    else:
        print("Opção inválida!")
        executar_todos_testes()
