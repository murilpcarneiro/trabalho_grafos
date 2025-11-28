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

Este repositório contém a implementação completa do trabalho proposto pela disciplina de Grafos do CESUPA, focando em **quatro estruturas de dados fundamentais para ciência da computação moderna**:

1. **Árvore k-D** - Para buscas em espaços multidimensionais
2. **Árvore Rubro-Negra** - Para operações balanceadas eficientes
3. **Árvore 2-3-4** - Para indexação com menos rotações
4. **Árvore Splay** - Para acesso adaptativo com reestruturação dinâmica

Cada implementação segue rigorosamente os requisitos técnicos, com nós implementados manualmente e operações críticas de inserção, exclusão e busca totalmente funcionais.

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- Bibliotecas necessárias:
  ```bash
  pip install matplotlib networkx
  ```

### Instalação e Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/murilpcarneiro/trabalho_grafos.git
   cd trabalho_grafos
   ```

2. Execute o programa principal:

   ```bash
   python src/main.py
   ```

3. O programa irá:
   - Criar as árvores (k-D, Rubro-Negra e 2-3-4)
   - Inserir 25 elementos aleatórios
   - Realizar operações de busca e exclusão
   - Visualizar as árvores em formato gráfico

### Testes

Para executar os testes automatizados:

```bash
python -m pytest testes/
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

### 1. **Árvore k-D (k-Dimensional)**

- **Status:** ✅ Explicação Detalhada + Exemplo
- **Descrição:** Estrutura de dados para indexação espacial multidimensional
- **Casos de Uso:** Busca espacial, sistemas de recomendação, compressão de dados
- **Características:** Particiona o espaço recursivamente alternando dimensões

**Arquivo:** `src/arvore_kd/kd_tree.py`

---

### 2. **Árvore Rubro-Negra (Red-Black Tree)**

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

### 3. **Árvore 2-3-4**

- **Status:** ✅ Explicação Detalhada + Exemplo + **Implementação Completa**
- **Descrição:** Árvore n-ária equilibrada onde cada nó pode ter 2, 3 ou 4 filhos
- **Operações:** Inserção, exclusão e busca em O(log n)
- **Vantagens:**
  - Inserção "top-down" simplifica o algoritmo
  - Menos rotações que árvores vermelha-preta
  - Melhor cache locality

**Arquivo:** `src/arvore_2_3_4/tree_234.py`

**Operações Implementadas:**

- ✅ Inserção com split de nós
- ✅ Exclusão com mesclagem de nós
- ✅ Busca por valor
- ✅ Visualização da árvore

---

### 4. **Árvore Splay**

- **Status:** ✅ Explicação Detalhada + Exemplo + **Implementação Completa**
- **Descrição:** Árvore de busca binária auto-equilibrada que reorganiza elementos acessados para raiz
- **Operações:** Inserção, exclusão e busca em O(log n) amortizado
- **Propriedades:**
  - Não mantém informações de cor ou altura
  - Nó acessado é movido para raiz via operações splay
  - Dados recentemente acessados ficam perto da raiz
  - Excelente para dados com padrões de acesso variáveis

**Arquivo:** `src/arvore_splay/splay_tree.py`

**Operações Implementadas:**

- ✅ Inserção com reestruturação automática
- ✅ Exclusão com rebalanceamento
- ✅ Busca por valor
- ✅ Operação splay (zig, zig-zig, zig-zag)
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
├── requirements.txt                    # Dependências Python
├── artigo_ieee.pdf                     # Artigo em formato IEEE
│
├── src/
│   ├── main.py                         # Programa principal - demonstração
│   │
│   ├── arvore_kd/
│   │   ├── __init__.py
│   │   ├── kd_tree.py                 # Implementação Árvore k-D
│   │   └── exemplo_kd.py              # Exemplo de uso
│   │
│   ├── arvore_rubro_negra/
│   │   ├── __init__.py
│   │   ├── red_black_tree.py          # Implementação Árvore Rubro-Negra
│   │   ├── node.py                    # Classe do nó
│   │   └── rotacoes.py                # Operações de rotação
│   │
│   ├── arvore_2_3_4/
│   │   ├── __init__.py
│   │   ├── tree_234.py                # Implementação Árvore 2-3-4
│   │   ├── node_234.py                # Classe do nó
│   │   └── operacoes.py               # Inserção, exclusão, busca
│   │
│   ├── arvore_splay/
│   │   ├── __init__.py
│   │   ├── splay_tree.py              # Implementação Árvore Splay
│   │   ├── node_splay.py              # Classe do nó
│   │   └── operacoes_splay.py         # Operações splay e rotações
│   │
│   └── utils/
│       ├── visualizacao.py            # Plotagem e visualização
│       └── testes.py                  # Funções de teste
│
├── testes/
│   ├── test_red_black_tree.py         # Testes Árvore Rubro-Negra
│   ├── test_tree_234.py               # Testes Árvore 2-3-4
│   ├── test_kd_tree.py                # Testes Árvore k-D
│   ├── test_splay_tree.py             # Testes Árvore Splay
│   └── test_integracao.py             # Testes de integração
│
├── visualizacao/
│   ├── graficos_comparacao.py         # Comparação entre árvores
│   └── saida_grafos/                  # Imagens das árvores geradas
│
└── docs/
    ├── CONCEITOS.md                   # Explicação dos conceitos
    ├── BALANCEAMENTO.md               # Detalhes do balanceamento
    └── ANALISE_DESEMPENHO.md          # Análise O(n) e comparações
```

---

## 🔬 Análise Comparativa dos Algoritmos

| Aspecto         | Rubro-Negra    | 2-3-4              | k-D            | Splay           |
| --------------- | -------------- | ------------------ | -------------- | --------------- |
| **Tipo**        | Árvore Binária | Árvore N-ária      | Árvore Binária | Árvore Binária  |
| **Inserção**    | O(log n)       | O(log n)           | O(log n)       | O(log n)\*      |
| **Busca**       | O(log n)       | O(log n)           | O(log n)       | O(log n)\*      |
| **Exclusão**    | O(log n)       | O(log n)           | O(log n)       | O(log n)\*      |
| **Rotações**    | Múltiplas      | Poucas (split)     | N/A            | Múltiplas       |
| **Dimensão**    | 1D             | 1D                 | n-D            | 1D              |
| **Caso de Uso** | Dados gerais   | Indexação de disco | Busca espacial | Acesso variável |

\*Complexidade amortizada

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
- [x] Explicação da árvore k-D com exemplo
- [x] Operações obrigatórias: inserção, exclusão, busca
- [x] Mínimo de 21 nós em cada árvore
- [x] Definição explícita de manipulação de elementos repetidos
- [x] Visualização gráfica das árvores
- [x] Código bem documentado no GitHub
- [x] Testes automatizados
- [x] Artigo IEEE
- [x] Vídeo de apresentação (20 minutos com todos os integrantes)

---

## 📝 Notas Importantes

**Originalidade:** Este trabalho foi desenvolvido com 100% de originalidade. Toda a implementação, pesquisa e análise foram realizadas pela equipe.

**Entrega:** Repositório entregue em única oportunidade no dia 29/11/2025, respeitando o prazo estabelecido.

---

**Trabalho submetido em:** 29 de Novembro de 2025
**Última atualização:** 29 de Novembro de 2025
**Status de Entrega:** ✅ COMPLETO
