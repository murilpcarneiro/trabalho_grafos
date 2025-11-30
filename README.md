# Árvores Binárias com Balanceamento: Implementação e Análise

**Trabalho de Segundo Bimestre - Disciplina de Grafos**
**CESUPA - Centro de Ensino Superior do Pará**

---

## 📋 Informações do Trabalho

- **Data de Entrega:** 29/11/2025
- **Disciplina:** Teoria dos Grafos
- **Professor:** Daniel Leal Souza
- **Equipe:** 5 integrantes
- **Status:** ✅ Entregue

---

## 🎯 Resumo Executivo

Este repositório contém a implementação completa do trabalho proposto pela disciplina de Grafos do CESUPA, focando em **duas estruturas de dados fundamentais para ciência da computação moderna**:

1. **Árvore Rubro-Negra** - Para operações balanceadas eficientes
2. **Árvore 2-3-4** - Para indexação com menos rotações

Cada implementação segue rigorosamente os requisitos técnicos, com nós implementados manualmente e operações críticas de inserção, exclusão e busca totalmente funcionais.

## 🚀 Como Executar

### Pré-requisitos

**Para Árvore Rubro-Negra (Python):**

- Python 3.8 ou superior
- Bibliotecas necessárias:
  ```bash
  pip install matplotlib networkx
  ```

**Para Árvore 2-3-4 (C):**

- Compilador GCC ou Clang

### Instalação e Execução

**Árvore Rubro-Negra:**

1. Acesse o diretório:

   ```bash
   cd "Arvore rubro-negra"
   ```

2. Execute o programa:

   ```bash
   python main.py
   ```

3. Execute os testes:
   ```bash
   python testes.py
   ```

**Árvore 2-3-4:**

1. Acesse o diretório:

   ```bash
   cd "Arvore 2-3-4"
   ```

2. Compile o programa:

   ```bash
   gcc main.c -o arvore_234
   ```

3. Execute o programa compilado:
   ```bash
   ./arvore_234
   ```

---

## 👥 Integrantes da Equipe

| Nome
| ----------------------------
| João Pedro Silva da Silva
| Murilo Pantoja Carneiro
| Pedro Lyra
| Vithor dos Santos
| João Felipe da Rocha Soares

---

## 📚 Implementações Realizadas

### 1. **Árvore Rubro-Negra (Red-Black Tree)**

- **Status:** ✅ Explicação Detalhada + Exemplo + **Implementação Completa**
- **Descrição:** Árvore de busca binária auto-equilibrada com propriedades de coloração
- **Operações:** Inserção, exclusão e busca em O(log n)
- **Propriedades:**
  - Todo nó é vermelho ou preto
  - Raiz sempre é preta
  - Folhas (NIL) são pretas
  - Nós vermelhos têm filhos pretos
  - Todos os caminhos raiz-folha têm mesmo número de nós pretos

**Arquivo:** `src/arvore_rubro_negra/red_black_tree.py`

**Operações Implementadas:**

- ✅ Inserção com rebalanceamento automático
- ✅ Exclusão com restauração de propriedades
- ✅ Busca por valor
- ✅ Visualização da árvore

---

### 2. **Árvore 2-3-4**

- **Status:** ✅ Explicação Detalhada + Exemplo + **Implementação Completa**
- **Linguagem:** C
- **Descrição:** Árvore n-ária equilibrada onde cada nó pode ter 2, 3 ou 4 filhos
- **Operações:** Inserção, exclusão e busca em O(log n)
- **Vantagens:**
  - Inserção "top-down" simplifica o algoritmo
  - Menos rotações que árvores vermelha-preta
  - Melhor cache locality

**Arquivo:** `Arvore 2-3-4/main.c`

**Operações Implementadas:**

- ✅ Inserção com split de nós
- ✅ Exclusão com mesclagem de nós
- ✅ Busca por valor
- ✅ Visualização da árvore

---

## 🧪 Testes e Demonstrações

O programa de demonstração realiza:

- **Inserção de 25 elementos aleatórios** em cada árvore
- **Testes de busca** para validar estrutura
- **Operações de exclusão** com rebalanceamento
- **Geração de gráficos** mostrando a estrutura das árvores
- **Análise de desempenho** (tempo de operações)

---

## 📊 Estrutura de Dados: Manipulação de Elementos Repetidos

**Decisão da Equipe:** Elementos repetidos são **ignorados** (não inseridos)

- Se um valor já existe na árvore, a operação de inserção retorna `False`
- A árvore mantém apenas um exemplar de cada valor
- Operações de busca funcionam normalmente
- Operações de exclusão removem exatamente um nó

---

## 📁 Estrutura do Repositório

```
trabalho_grafos/
├── README.md                           # Este arquivo
│
├── Arvore rubro-negra/                 # Implementação em Python
│   ├── main.py                         # Programa principal - demonstração
│   ├── testes.py                       # Testes da árvore rubro-negra
│   ├── requirements.txt                # Dependências
│   └── README.md                       # Documentação específica
│
└── Arvore 2-3-4/                       # Implementação em C
    ├── main.c                          # Programa principal em C
    └── README.md                       # Documentação específica
```

---

## 🔬 Análise Comparativa dos Algoritmos

| Aspecto         | Rubro-Negra    | 2-3-4              |
| --------------- | -------------- | ------------------ |
| **Tipo**        | Árvore Binária | Árvore N-ária      |
| **Inserção**    | O(log n)       | O(log n)           |
| **Busca**       | O(log n)       | O(log n)           |
| **Exclusão**    | O(log n)       | O(log n)           |
| **Rotações**    | Múltiplas      | Poucas (split)     |
| **Caso de Uso** | Dados gerais   | Indexação de disco |

---

## 🎥 Vídeo de Apresentação

A gravação em vídeo está disponível em: [Link do vídeo no Google Classroom/YouTube]

**Conteúdo do vídeo (20 minutos):**

- Conceitos fundamentais de árvores binárias
- Explicação detalhada de cada algoritmo de balanceamento
- Comparação entre os métodos
- Demonstração prática: inserção, busca e exclusão
- Análise de performance e visualização gráfica

**Participantes:** Todos os 5 integrantes da equipe

---

## 📄 Artigo IEEE

Arquivo: `artigo_ieee.pdf`

**Seções incluídas:**

- Introdução
- Fundamentação Teórica
- Descrição Técnica da Implementação
- Resultados e Discussões
- Conclusão
- Referências

---

## 📚 Referências Bibliográficas

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). _Introduction to algorithms_ (3rd ed.). MIT Press.

2. Sedgewick, R., & Wayne, K. (2011). _Algorithms_ (4th ed.). Addison-Wesley Professional.

3. Bayer, R., & McCreight, E. (1970). Organization and Maintenance of Large Ordered Indices. _Acta Informatica_, 1(3), 173-189.

4. Bentley, J. L. (1975). Multidimensional binary search trees used for associative searching. _Communications of the ACM_, 18(9), 509-517.

5. Weiss, M. A. (2012). _Data structures and algorithm analysis in Java_ (3rd ed.). Pearson.

---

## ✅ Checklist de Entrega

- [x] Implementação das árvores binárias (Rubro-Negra e 2-3-4)
- [x] Operações obrigatórias: inserção, exclusão, busca
- [x] Mínimo de 21 nós em cada árvore
- [x] Definição explícita de manipulação de elementos repetidos
- [x] Visualização gráfica das árvores
- [x] Código bem documentado no GitHub
- [x] Testes automatizados

---

## 📝 Notas Importantes

**Originalidade:** Este trabalho foi desenvolvido com 100% de originalidade. Toda a implementação, pesquisa e análise foram realizadas pela equipe.

**Entrega:** Repositório entregue em única oportunidade no dia 29/11/2025, respeitando o prazo estabelecido.

---

**Trabalho submetido em:** 29 de Novembro de 2025
**Última atualização:** 29 de Novembro de 2025
**Status de Entrega:** ✅ COMPLETO
