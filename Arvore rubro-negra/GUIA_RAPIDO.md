# 🚀 GUIA RÁPIDO - ÁRVORE RUBRO-NEGRA

## Arquivos do Projeto

```
📁 Grafos Arvores/
├── 📄 main.py                    # Programa principal (interface interativa)
├── 📄 testes.py                  # Suite de testes automatizados
├── 📄 requirements.txt           # Dependências Python
├── 📄 README.md                  # Documentação completa
├── 📄 ROTEIRO_APRESENTACAO.md   # Roteiro detalhado para apresentação
└── 📄 GUIA_RAPIDO.md            # Este arquivo
```

## ⚡ Início Rápido

### 1. Instalar dependências (já feito! ✅)
```bash
pip install matplotlib networkx
```

### 2. Executar programa principal
```bash
python main.py
```

### 3. Executar testes
```bash
python testes.py
```

## 🎮 Comandos Principais

### No programa principal (`main.py`):

| Opção | Função | Exemplo |
|-------|--------|---------|
| **1** | Inserir valor | Digite: `42` |
| **2** | Excluir valor | Digite: `25` |
| **3** | Buscar valor | Digite: `75` |
| **4** | **Visualizar árvore** 🌳 | Abre janela gráfica |
| **5** | Imprimir estrutura | Mostra no terminal |
| **6** | Percursos | In/pre/pós-ordem |
| **7** | Informações | Altura, tamanho, etc |
| **8** | Inserir múltiplos | Digite: `10 20 30 40` |
| **9** | Resetar árvore | Cria nova com 21+ nós |
| **0** | Sair | Encerra programa |

### No arquivo de testes (`testes.py`):

| Opção | Teste |
|-------|-------|
| **1** | Todos os testes |
| **2** | Inserção básica |
| **3** | Inserção sequencial |
| **4** | Elementos repetidos |
| **5** | Exclusão |
| **6** | Busca |
| **7** | Árvore grande (30 nós) |
| **8** | Comparação de altura |

## 📋 Checklist Pré-Apresentação

### ✅ Preparação (5 minutos antes):
- [ ] Abrir terminal no diretório do projeto
- [ ] Executar `python main.py` para verificar funcionamento
- [ ] Executar `python testes.py` opção 1 (confirmar que todos passam)
- [ ] Abrir `ROTEIRO_APRESENTACAO.md` em outra janela
- [ ] Testar projetor/compartilhamento de tela
- [ ] Fechar abas desnecessárias do navegador

### ✅ Durante apresentação:
- [ ] Mostrar árvore inicial (já vem com 21+ nós)
- [ ] Visualizar com opção 4
- [ ] Demonstrar inserção (opção 1): valores 100, 200, 300
- [ ] Visualizar novamente para mostrar balanceamento
- [ ] Demonstrar exclusão (opção 2): remover um nó
- [ ] Tentar inserir duplicata para mostrar tratamento
- [ ] Executar testes.py opção 1 (todos os testes)

## 🎯 Demonstrações Sugeridas

### Demonstração 1: Balanceamento na Inserção (2 min)
```
1. Executar: python main.py
2. Opção 9: Criar nova árvore vazia
3. Opção 8: Inserir múltiplos: 10 5 15 3 7 12 17
4. Opção 4: Visualizar
5. Opção 1: Inserir 20
6. Opção 4: Visualizar novamente (mostrar mudança)
```

### Demonstração 2: Elementos Repetidos (1 min)
```
1. Opção 1: Inserir 50
2. Opção 1: Inserir 50 novamente
3. Mostrar mensagem: "Valor 50 já existe. Inserção ignorada."
4. Opção 7: Confirmar que tamanho não aumentou
```

### Demonstração 3: Exclusão (2 min)
```
1. Opção 5: Imprimir estrutura atual
2. Opção 2: Excluir 50 (raiz)
3. Opção 5: Imprimir estrutura novamente
4. Opção 4: Visualizar (mostrar nova raiz)
```

### Demonstração 4: Testes Automatizados (2 min)
```
1. Executar: python testes.py
2. Opção 1: Executar todos os testes
3. Aguardar conclusão (30-60 segundos)
4. Mostrar que todos passaram ✅
5. Destacar verificação de propriedades
```

## 🔑 Conceitos-Chave para Explicar

### 1. As 5 Propriedades (MEMORIZAR!)
1. Todo nó é vermelho ou preto
2. Raiz é sempre preta
3. Folhas (NIL) são pretas
4. Vermelho → filhos pretos (sem vermelhos consecutivos)
5. Mesma quantidade de pretos em todos os caminhos

### 2. Tratamento de Duplicatas
- **Política**: Não inserir valores repetidos
- **Por quê?**: Mantém simplicidade e eficiência O(log n)
- **Como**: Verifica existência antes de inserir

### 3. Balanceamento vs AVL
| | Rubro-Negra | AVL |
|---|-------------|-----|
| Rotações inserção | ≤ 2 | ≤ log(n) |
| Altura | ~2·log(n) | ~1.44·log(n) |
| Melhor para | Modificações | Buscas |

### 4. Aplicações Reais
- Java: `TreeMap`, `TreeSet`
- C++: `std::map`, `std::set`
- Linux: Agendador de processos (CFS)

## 💡 Respostas Rápidas para Perguntas Comuns

**P: Por que cores?**
R: Simplificam balanceamento. Vermelho = nível extra permitido, Preto = estrutura obrigatória.

**P: Por que não AVL?**
R: RB tem menos rotações em modificações. AVL melhor só para muitas buscas.

**P: Como garantir O(log n)?**
R: Propriedade 5 garante altura ≤ 2·log(n+1).

**P: Novos nós são sempre vermelhos?**
R: Sim! Não viola altura preta. Só pode violar "sem vermelhos consecutivos" (mais fácil corrigir).

**P: Quantas rotações são necessárias?**
R: Inserção: máximo 2. Exclusão: máximo 3.

## 📞 Comandos Python Úteis

### Usar árvore programaticamente:
```python
from main import ArvoreRubroNegra

# Criar árvore
arvore = ArvoreRubroNegra()

# Inserir valores
arvore.inserir(50)
arvore.inserir(25)
arvore.inserir(75)

# Buscar
no = arvore.buscar(25)
if no:
    print(f"Encontrado: {no.valor}")

# Excluir
arvore.excluir(25)

# Percursos
print(arvore.em_ordem())      # Lista ordenada
print(arvore.pre_ordem())     # Pré-ordem
print(arvore.pos_ordem())     # Pós-ordem

# Informações
print(f"Tamanho: {len(arvore)}")
print(f"Altura: {arvore.altura()}")
print(f"Altura preta: {arvore.altura_preta()}")

# Visualizar
arvore.visualizar()

# Imprimir estrutura
arvore.imprimir_estrutura()
```

## 🎨 Interpretando a Visualização

### Cores dos Nós:
- 🔴 **Vermelho**: Nó vermelho
- ⚫ **Preto**: Nó preto

### Estrutura:
- Círculos = nós
- Linhas = conexões pai-filho
- Números = valores armazenados

### Legenda:
- Canto superior direito: cores
- Rodapé: informações (nós, altura, altura preta)

## ⚠️ Troubleshooting

### Problema: Visualização não abre
**Solução**: 
```bash
pip install --upgrade matplotlib
```

### Problema: "ModuleNotFoundError: No module named 'networkx'"
**Solução**:
```bash
pip install networkx
```

### Problema: Gráfico aparece mas fecha imediatamente
**Solução**: Normal! Feche a janela para continuar o programa.

### Problema: Texto cortado na visualização
**Solução**: Maximize a janela ou aumente resolução.

## 📊 Valores de Exemplo para Demonstração

### Conjunto 1: Balanceamento básico
```
50, 25, 75, 12, 37, 62, 87
```

### Conjunto 2: Inserção sequencial (mostra poder do balanceamento)
```
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

### Conjunto 3: Árore grande e interessante
```
50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93, 3, 9, 15, 21, 28, 34, 40, 46, 53, 59
```

## ⏱️ Timing da Apresentação

| Atividade | Tempo | Total |
|-----------|-------|-------|
| Introdução + Conceitos | 5 min | 5 min |
| Explicar propriedades | 3 min | 8 min |
| Demo inserção | 2 min | 10 min |
| Demo exclusão | 2 min | 12 min |
| Demo duplicatas | 1 min | 13 min |
| Testes automatizados | 2 min | 15 min |
| Comparação AVL | 2 min | 17 min |
| Perguntas | 3 min | 20 min |

## 🏆 Últimas Dicas

1. ✅ **Pratique pelo menos 2x antes** de apresentar
2. ✅ **Tenha screenshots prontos** como backup
3. ✅ **Feche outros programas** para evitar notificações
4. ✅ **Aumente tamanho da fonte** do terminal
5. ✅ **Teste projetor antes** da apresentação
6. ✅ **Respire fundo** - você sabe o conteúdo!

## 📞 Atalhos de Teclado

No terminal Windows:
- `Ctrl + C`: Interromper programa
- `Seta ↑`: Comando anterior
- `Tab`: Autocompletar
- `Ctrl + L` ou `cls`: Limpar tela

## ✨ Bônus: Comandos Rápidos

### Criar árvore com valores específicos:
```bash
python -c "from main import ArvoreRubroNegra; a = ArvoreRubroNegra(); [a.inserir(x) for x in [50,25,75,12,37]]; a.visualizar()"
```

### Ver apenas percursos:
```bash
python -c "from main import ArvoreRubroNegra; a = ArvoreRubroNegra(); [a.inserir(x) for x in range(1,16)]; print('Em ordem:', a.em_ordem())"
```

---

**BOA APRESENTAÇÃO! 🎉**

Lembre-se: Você implementou uma estrutura de dados complexa do zero. Isso é impressionante! 🚀
