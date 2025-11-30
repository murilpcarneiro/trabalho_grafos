# 🌳 Árvore Rubro-Negra (Red-Black Tree)

## 📋 Descrição do Projeto

Implementação completa de uma **Árvore Rubro-Negra** (Red-Black Tree) em Python, desenvolvida como parte do trabalho acadêmico sobre estruturas de dados de árvores binárias balanceadas.

## 🎯 Requisitos Atendidos

✅ **Implementação usando nós** - A árvore é implementada usando a classe `No`, similar a listas duplamente encadeadas  
✅ **Sem uso de bibliotecas prontas** - Toda a lógica de árvore foi desenvolvida manualmente  
✅ **Inserção com balanceamento** - Implementada com rotações e recoloração automática  
✅ **Exclusão com balanceamento** - Implementada mantendo as propriedades rubro-negras  
✅ **Busca de dados** - Busca binária eficiente (O(log n))  
✅ **Mínimo de 21 nós** - Árvore inicial criada com 25 nós  
✅ **Visualização gráfica** - Usando matplotlib e networkx  

## 🔴⚫ O que é uma Árvore Rubro-Negra?

Uma Árvore Rubro-Negra é uma **árvore binária de busca auto-balanceada** onde cada nó possui uma cor (vermelho ou preto) e deve seguir propriedades específicas que garantem o balanceamento.

### Propriedades Fundamentais:

1. **Todo nó é vermelho ou preto**
2. **A raiz é sempre preta**
3. **Todas as folhas (NIL) são pretas**
4. **Se um nó é vermelho, ambos os filhos são pretos** (não pode haver dois nós vermelhos consecutivos)
5. **Todos os caminhos da raiz até as folhas contêm o mesmo número de nós pretos** (altura preta)

## 🔄 Método de Balanceamento

### Inserção:
1. **Novo nó sempre começa VERMELHO**
2. Insere como BST normal
3. Corrige violações usando:
   - **Recoloração**: Muda cores de nós para manter propriedades
   - **Rotações**: Esquerda e direita para reorganizar estrutura

### Casos de Correção na Inserção:
- **Caso 1**: Tio é vermelho → Recolore pai, tio e avô
- **Caso 2**: Tio é preto + nó é filho interno → Rotação dupla
- **Caso 3**: Tio é preto + nó é filho externo → Rotação simples + recoloração

### Exclusão:
1. Remove como BST normal
2. Se nó removido era preto, pode violar propriedades
3. Corrige usando rotações e recolorações complexas

## 🔁 Tratamento de Elementos Repetidos

**Política implementada**: **Valores duplicados NÃO são inseridos**

- A árvore mantém apenas valores únicos
- Ao tentar inserir um valor já existente, a operação é ignorada
- Uma mensagem de aviso é exibida ao usuário

**Justificativa**: Esta é a abordagem mais comum em implementações de árvores de busca, pois:
- Mantém a eficiência de busca O(log n)
- Evita complexidade adicional no balanceamento
- É adequada para uso como índice ou conjunto

## 🚀 Como Executar

### 1. Instalar dependências:
```bash
pip install -r requirements.txt
```

### 2. Executar o programa:
```bash
python main.py
```

## 📊 Funcionalidades

### Menu Interativo:
1. **Inserir valor** - Adiciona um novo nó com balanceamento automático
2. **Excluir valor** - Remove um nó mantendo propriedades rubro-negras
3. **Buscar valor** - Procura um valor na árvore
4. **Visualizar árvore** - Gera gráfico colorido da estrutura
5. **Imprimir estrutura** - Mostra árvore em formato texto hierárquico
6. **Percursos** - Exibe em ordem, pré-ordem e pós-ordem
7. **Informações** - Mostra altura, altura preta e número de nós
8. **Inserir múltiplos** - Insere vários valores de uma vez
9. **Resetar árvore** - Cria nova árvore com 21+ nós

## 🎨 Visualização

A árvore é visualizada com:
- **Nós vermelhos**: Círculos vermelhos
- **Nós pretos**: Círculos pretos
- **Arestas**: Linhas conectando pais e filhos
- **Legenda**: Explicação das cores
- **Informações**: Número de nós, altura total e altura preta

## 📈 Complexidade

| Operação | Complexidade |
|----------|-------------|
| Busca    | O(log n)    |
| Inserção | O(log n)    |
| Exclusão | O(log n)    |
| Espaço   | O(n)        |

## 🔄 Diferenças entre Métodos de Balanceamento

### Árvore Rubro-Negra vs AVL:

| Característica | Rubro-Negra | AVL |
|---------------|-------------|-----|
| **Balanceamento** | Menos rígido | Mais rígido |
| **Altura máxima** | ~2·log(n+1) | ~1.44·log(n+2) |
| **Rotações na inserção** | Máximo 2 | Até log(n) |
| **Uso ideal** | Muitas inserções/exclusões | Muitas buscas |
| **Complexidade** | Mais simples | Mais complexa |

**Vantagens da Rubro-Negra**:
- ✅ Menos rotações em inserções e exclusões
- ✅ Melhor desempenho em operações de modificação
- ✅ Usado em bibliotecas padrão (Java TreeMap, C++ map)

**Vantagens da AVL**:
- ✅ Árvore mais balanceada
- ✅ Buscas ligeiramente mais rápidas
- ✅ Garantia de altura mínima

## 📚 Conceitos para Apresentação

### Pontos-chave para explicar:

1. **Por que usar cores?**
   - As cores representam "níveis lógicos" na árvore
   - Permitem balanceamento mais flexível que AVL
   - Simplificam a análise da altura

2. **Como funciona o balanceamento?**
   - Combinação de rotações (como AVL) e recoloração (único)
   - Recoloração é mais rápida que rotação
   - No máximo 2 rotações por inserção

3. **Quando usar Rubro-Negra?**
   - Aplicações com muitas inserções/exclusões
   - Quando busca não é a operação dominante
   - Estruturas de dados do sistema operacional

4. **Aplicações reais**:
   - Java: `TreeMap`, `TreeSet`
   - C++: `std::map`, `std::set`
   - Linux: Agendador de processos (CFS)

## 👨‍💻 Estrutura do Código

```
main.py
├── Classe Cor          # Enum para cores
├── Classe No           # Nó da árvore
└── Classe ArvoreRubroNegra
    ├── Rotações        # rotacao_esquerda, rotacao_direita
    ├── Inserção        # inserir, _corrigir_insercao
    ├── Exclusão        # excluir, _corrigir_exclusao
    ├── Busca           # buscar
    ├── Traversal       # em_ordem, pre_ordem, pos_ordem
    └── Visualização    # visualizar, imprimir_estrutura
```

## 🎓 Dicas para Apresentação

1. **Demonstre visualmente**: Use a visualização gráfica para mostrar as operações
2. **Explique as propriedades**: Mostre como elas garantem O(log n)
3. **Compare com AVL**: Destaque as diferenças de balanceamento
4. **Mostre casos práticos**: Insira e remova valores mostrando recolorações e rotações
5. **Explique elementos repetidos**: Justifique a política de não inserção

## 📝 Exemplo de Uso

```python
# Criar árvore
arvore = ArvoreRubroNegra()

# Inserir valores
arvore.inserir(50)
arvore.inserir(25)
arvore.inserir(75)

# Buscar
no = arvore.buscar(25)  # Retorna o nó

# Excluir
arvore.excluir(25)

# Visualizar
arvore.visualizar()
```

## 🏆 Autor

Desenvolvido para o trabalho de Grafos e Árvores - Implementação de Árvore Rubro-Negra

---

**Nota**: Esta implementação é educacional e demonstra todos os conceitos fundamentais de Árvores Rubro-Negras de forma clara e didática.
