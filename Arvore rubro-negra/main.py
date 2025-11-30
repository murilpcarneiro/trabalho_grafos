"""Implementação de Árvore Rubro-Negra (Red-Black Tree) com animações"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import networkx as nx
import time
from matplotlib.animation import FuncAnimation
import copy


class Cor:
    VERMELHO = 0
    PRETO = 1


class No:
    """Representa um nó da Árvore Rubro-Negra"""
    def __init__(self, valor):
        self.valor = valor
        self.cor = Cor.VERMELHO
        self.pai = None
        self.esquerda = None
        self.direita = None
    
    def __str__(self):
        cor_texto = "V" if self.cor == Cor.VERMELHO else "P"
        return f"{self.valor}({cor_texto})"


class ArvoreRubroNegra:
    """Árvore Rubro-Negra auto-balanceada com suporte a animações"""
    
    def __init__(self):
        self.NIL = No(None)
        self.NIL.cor = Cor.PRETO
        self.raiz = self.NIL
        self.tamanho = 0
        self.estados_animacao = []
        self.descricoes_animacao = []
    
    def rotacao_esquerda(self, x, capturar_estado=False):
        """Realiza rotação à esquerda no nó x"""
        if capturar_estado:
            self._capturar_estado(f"Rotação ESQUERDA em nó {x.valor}")
        
        y = x.direita
        x.direita = y.esquerda
        
        if y.esquerda != self.NIL:
            y.esquerda.pai = x
        
        y.pai = x.pai
        
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
        
        y.esquerda = x
        x.pai = y
        
        if capturar_estado:
            self._capturar_estado(f"Após rotação esquerda em {x.valor}")
    
    def rotacao_direita(self, y, capturar_estado=False):
        """Realiza rotação à direita no nó y"""
        if capturar_estado:
            self._capturar_estado(f"Rotação DIREITA em nó {y.valor}")
        
        x = y.esquerda
        y.esquerda = x.direita
        
        if x.direita != self.NIL:
            x.direita.pai = y
        
        x.pai = y.pai
        
        if y.pai is None:
            self.raiz = x
        elif y == y.pai.direita:
            y.pai.direita = x
        else:
            y.pai.esquerda = x
        
        x.direita = y
        y.pai = x
        
        if capturar_estado:
            self._capturar_estado(f"Após rotação direita em {y.valor}")
    
    def inserir(self, valor):
        """Insere um valor na árvore"""
        # Verifica se o valor já existe
        if self.buscar(valor) is not None:
            print(f"⚠️  Valor {valor} já existe na árvore. Inserção ignorada.")
            return False
        
        novo_no = No(valor)
        novo_no.esquerda = self.NIL
        novo_no.direita = self.NIL
        
        pai = None
        atual = self.raiz
        
        # Busca a posição correta para inserir (BST padrão)
        while atual != self.NIL:
            pai = atual
            if novo_no.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        
        novo_no.pai = pai
        
        if pai is None:
            self.raiz = novo_no
        elif novo_no.valor < pai.valor:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no
        
        self.tamanho += 1
        
        # Se for a raiz, apenas muda para preto
        if novo_no.pai is None:
            novo_no.cor = Cor.PRETO
            return True
        
        # Se o avô não existe, não precisa balancear
        if novo_no.pai.pai is None:
            return True
        
        # Corrige a árvore para manter propriedades Rubro-Negra
        self._corrigir_insercao(novo_no, capturar_estado=False)
        return True
    
    def _corrigir_insercao(self, no, capturar_estado=False):
        """Corrige propriedades da árvore após inserção"""
        while no.pai and no.pai.cor == Cor.VERMELHO:
            if no.pai == no.pai.pai.direita:
                tio = no.pai.pai.esquerda
                
                if tio.cor == Cor.VERMELHO:
                    # Caso 1: Tio é vermelho - recoloração
                    if capturar_estado:
                        self._capturar_estado(f"Caso 1: Tio {tio.valor} é VERMELHO - Recoloração")
                    tio.cor = Cor.PRETO
                    no.pai.cor = Cor.PRETO
                    no.pai.pai.cor = Cor.VERMELHO
                    no = no.pai.pai
                    if capturar_estado:
                        self._capturar_estado(f"Recoloração completa")
                else:
                    # Caso 2: Tio é preto e nó é filho esquerdo
                    if no == no.pai.esquerda:
                        if capturar_estado:
                            self._capturar_estado(f"Caso 2: Tio é PRETO, nó {no.valor} é filho esquerdo")
                        no = no.pai
                        self.rotacao_direita(no, capturar_estado)
                    
                    # Caso 3: Tio é preto e nó é filho direito
                    if capturar_estado:
                        self._capturar_estado(f"Caso 3: Ajustando cores e rotacionando")
                    no.pai.cor = Cor.PRETO
                    no.pai.pai.cor = Cor.VERMELHO
                    self.rotacao_esquerda(no.pai.pai, capturar_estado)
            else:
                tio = no.pai.pai.direita
                
                if tio.cor == Cor.VERMELHO:
                    # Caso 1: Tio é vermelho - recoloração
                    if capturar_estado:
                        self._capturar_estado(f"Caso 1: Tio {tio.valor} é VERMELHO - Recoloração")
                    tio.cor = Cor.PRETO
                    no.pai.cor = Cor.PRETO
                    no.pai.pai.cor = Cor.VERMELHO
                    no = no.pai.pai
                    if capturar_estado:
                        self._capturar_estado(f"Recoloração completa")
                else:
                    # Caso 2: Tio é preto e nó é filho direito
                    if no == no.pai.direita:
                        if capturar_estado:
                            self._capturar_estado(f"Caso 2: Tio é PRETO, nó {no.valor} é filho direito")
                        no = no.pai
                        self.rotacao_esquerda(no, capturar_estado)
                    
                    # Caso 3: Tio é preto e nó é filho esquerdo
                    if capturar_estado:
                        self._capturar_estado(f"Caso 3: Ajustando cores e rotacionando")
                    no.pai.cor = Cor.PRETO
                    no.pai.pai.cor = Cor.VERMELHO
                    self.rotacao_direita(no.pai.pai, capturar_estado)
            
            if no == self.raiz:
                break
        
        self.raiz.cor = Cor.PRETO
        if capturar_estado:
            self._capturar_estado(f"Garantindo que raiz seja PRETA")
    
    def buscar(self, valor):
        """Busca um valor na árvore"""
        return self._buscar_aux(self.raiz, valor)
    
    def _buscar_aux(self, no, valor):
        """Busca recursiva"""
        if no == self.NIL or no.valor == valor:
            return no if no != self.NIL else None
        
        if valor < no.valor:
            return self._buscar_aux(no.esquerda, valor)
        return self._buscar_aux(no.direita, valor)
    
    def excluir(self, valor):
        """Remove um valor da árvore"""
        no = self.buscar(valor)
        if no is None:
            print(f"⚠️  Valor {valor} não encontrado na árvore.")
            return False
        
        self._excluir_no(no)
        self.tamanho -= 1
        return True
    
    def _excluir_no(self, z):
        """Remove nó da árvore"""
        y = z
        y_cor_original = y.cor
        
        if z.esquerda == self.NIL:
            x = z.direita
            self._transplantar(z, z.direita)
        elif z.direita == self.NIL:
            x = z.esquerda
            self._transplantar(z, z.esquerda)
        else:
            # Encontra o sucessor (menor nó da subárvore direita)
            y = self._minimo(z.direita)
            y_cor_original = y.cor
            x = y.direita
            
            if y.pai == z:
                x.pai = y
            else:
                self._transplantar(y, y.direita)
                y.direita = z.direita
                y.direita.pai = y
            
            self._transplantar(z, y)
            y.esquerda = z.esquerda
            y.esquerda.pai = y
            y.cor = z.cor
        
        if y_cor_original == Cor.PRETO:
            self._corrigir_exclusao(x, capturar_estado=False)
    
    def _corrigir_exclusao(self, x, capturar_estado=False):
        """Corrige propriedades da árvore após exclusão"""
        while x != self.raiz and x.cor == Cor.PRETO:
            if x == x.pai.esquerda:
                irmao = x.pai.direita
                
                # Caso 1: Irmão é vermelho
                if irmao.cor == Cor.VERMELHO:
                    if capturar_estado:
                        self._capturar_estado(f"Caso 1 Exclusão: Irmão {irmao.valor} é VERMELHO")
                    irmao.cor = Cor.PRETO
                    x.pai.cor = Cor.VERMELHO
                    self.rotacao_esquerda(x.pai, capturar_estado)
                    irmao = x.pai.direita
                
                # Caso 2: Irmão é preto e ambos os filhos do irmão são pretos
                if irmao.esquerda.cor == Cor.PRETO and irmao.direita.cor == Cor.PRETO:
                    if capturar_estado:
                        self._capturar_estado(f"Caso 2 Exclusão: Irmão e filhos são PRETOS")
                    irmao.cor = Cor.VERMELHO
                    x = x.pai
                    if capturar_estado:
                        self._capturar_estado(f"Recolorindo irmão para VERMELHO")
                else:
                    # Caso 3: Irmão é preto, filho esquerdo é vermelho e direito é preto
                    if irmao.direita.cor == Cor.PRETO:
                        if capturar_estado:
                            self._capturar_estado(f"Caso 3 Exclusão: Preparando rotação")
                        irmao.esquerda.cor = Cor.PRETO
                        irmao.cor = Cor.VERMELHO
                        self.rotacao_direita(irmao, capturar_estado)
                        irmao = x.pai.direita
                    
                    # Caso 4: Irmão é preto e filho direito é vermelho
                    if capturar_estado:
                        self._capturar_estado(f"Caso 4 Exclusão: Ajuste final")
                    irmao.cor = x.pai.cor
                    x.pai.cor = Cor.PRETO
                    irmao.direita.cor = Cor.PRETO
                    self.rotacao_esquerda(x.pai, capturar_estado)
                    x = self.raiz
            else:
                irmao = x.pai.esquerda
                
                if irmao.cor == Cor.VERMELHO:
                    if capturar_estado:
                        self._capturar_estado(f"Caso 1 Exclusão: Irmão {irmao.valor} é VERMELHO")
                    irmao.cor = Cor.PRETO
                    x.pai.cor = Cor.VERMELHO
                    self.rotacao_direita(x.pai, capturar_estado)
                    irmao = x.pai.esquerda
                
                if irmao.direita.cor == Cor.PRETO and irmao.esquerda.cor == Cor.PRETO:
                    if capturar_estado:
                        self._capturar_estado(f"Caso 2 Exclusão: Irmão e filhos são PRETOS")
                    irmao.cor = Cor.VERMELHO
                    x = x.pai
                    if capturar_estado:
                        self._capturar_estado(f"Recolorindo irmão para VERMELHO")
                else:
                    if irmao.esquerda.cor == Cor.PRETO:
                        if capturar_estado:
                            self._capturar_estado(f"Caso 3 Exclusão: Preparando rotação")
                        irmao.direita.cor = Cor.PRETO
                        irmao.cor = Cor.VERMELHO
                        self.rotacao_esquerda(irmao, capturar_estado)
                        irmao = x.pai.esquerda
                    
                    if capturar_estado:
                        self._capturar_estado(f"Caso 4 Exclusão: Ajuste final")
                    irmao.cor = x.pai.cor
                    x.pai.cor = Cor.PRETO
                    irmao.esquerda.cor = Cor.PRETO
                    self.rotacao_direita(x.pai, capturar_estado)
                    x = self.raiz
        
        x.cor = Cor.PRETO
        if capturar_estado:
            self._capturar_estado(f"Garantindo propriedades finais")
    
    def _transplantar(self, u, v):
        """Substitui subárvore u por v"""
        if u.pai is None:
            self.raiz = v
        elif u == u.pai.esquerda:
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        v.pai = u.pai
    
    def _minimo(self, no):
        """Encontra valor mínimo na subárvore"""
        while no.esquerda != self.NIL:
            no = no.esquerda
        return no
    
    def em_ordem(self):
        """Percurso em ordem"""
        resultado = []
        self._em_ordem_aux(self.raiz, resultado)
        return resultado
    
    def _em_ordem_aux(self, no, resultado):
        """Percurso em ordem recursivo"""
        if no != self.NIL:
            self._em_ordem_aux(no.esquerda, resultado)
            resultado.append(no.valor)
            self._em_ordem_aux(no.direita, resultado)
    
    def pre_ordem(self):
        """Percurso em pré-ordem"""
        resultado = []
        self._pre_ordem_aux(self.raiz, resultado)
        return resultado
    
    def _pre_ordem_aux(self, no, resultado):
        """Percurso em pré-ordem recursivo"""
        if no != self.NIL:
            resultado.append(no.valor)
            self._pre_ordem_aux(no.esquerda, resultado)
            self._pre_ordem_aux(no.direita, resultado)
    
    def pos_ordem(self):
        """Percurso em pós-ordem"""
        resultado = []
        self._pos_ordem_aux(self.raiz, resultado)
        return resultado
    
    def _pos_ordem_aux(self, no, resultado):
        """Percurso em pós-ordem recursivo"""
        if no != self.NIL:
            self._pos_ordem_aux(no.esquerda, resultado)
            self._pos_ordem_aux(no.direita, resultado)
            resultado.append(no.valor)
    
    def altura(self):
        """Retorna altura da árvore"""
        return self._altura_aux(self.raiz)
    
    def _altura_aux(self, no):
        """Calcula altura recursivamente"""
        if no == self.NIL:
            return 0
        return 1 + max(self._altura_aux(no.esquerda), self._altura_aux(no.direita))
    
    def altura_preta(self):
        """Retorna altura preta da árvore"""
        return self._altura_preta_aux(self.raiz)
    
    def _altura_preta_aux(self, no):
        """Calcula altura preta recursivamente"""
        if no == self.NIL:
            return 1
        
        altura_esq = self._altura_preta_aux(no.esquerda)
        
        if no.cor == Cor.PRETO:
            return altura_esq + 1
        return altura_esq
    
    def __len__(self):
        """Retorna número de nós"""
        return self.tamanho
    
    def _capturar_estado(self, descricao):
        """Captura estado atual para animação"""
        estado = self._clonar_arvore()
        self.estados_animacao.append(estado)
        self.descricoes_animacao.append(descricao)
    
    def _clonar_arvore(self):
        """Cria cópia da estrutura da árvore"""
        nos = {}
        if self.raiz != self.NIL:
            self._clonar_no(self.raiz, nos)
        return nos
    
    def _clonar_no(self, no, nos_dict):
        """Clona nó recursivamente"""
        if no == self.NIL:
            return
        
        node_id = id(no)
        nos_dict[node_id] = {
            'valor': no.valor,
            'cor': no.cor,
            'esquerda_id': id(no.esquerda) if no.esquerda != self.NIL else None,
            'direita_id': id(no.direita) if no.direita != self.NIL else None,
            'pai_id': id(no.pai) if no.pai else None
        }
        
        if no.esquerda != self.NIL:
            self._clonar_no(no.esquerda, nos_dict)
        if no.direita != self.NIL:
            self._clonar_no(no.direita, nos_dict)
    
    def inserir_animado(self, valor):
        """Insere valor capturando estados para animação"""
        # Limpa estados anteriores
        self.estados_animacao = []
        self.descricoes_animacao = []
        
        # Captura estado inicial
        self._capturar_estado(f"Estado inicial antes de inserir {valor}")
        
        # Verifica se o valor já existe
        if self.buscar(valor) is not None:
            print(f"⚠️  Valor {valor} já existe na árvore. Inserção ignorada.")
            return False
        
        novo_no = No(valor)
        novo_no.esquerda = self.NIL
        novo_no.direita = self.NIL
        
        pai = None
        atual = self.raiz
        
        # Busca a posição correta para inserir
        while atual != self.NIL:
            pai = atual
            if novo_no.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        
        novo_no.pai = pai
        
        if pai is None:
            self.raiz = novo_no
        elif novo_no.valor < pai.valor:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no
        
        self.tamanho += 1
        
        # Captura estado após inserção como folha vermelha
        self._capturar_estado(f"Inserido {valor} como nó VERMELHO")
        
        # Se for a raiz, apenas muda para preto
        if novo_no.pai is None:
            novo_no.cor = Cor.PRETO
            self._capturar_estado(f"Nó {valor} é raiz - mudando para PRETO")
            return True
        
        # Se o avô não existe, não precisa balancear
        if novo_no.pai.pai is None:
            return True
        
        # Corrige a árvore para manter propriedades Rubro-Negra
        self._corrigir_insercao(novo_no, capturar_estado=True)
        
        # Captura estado final
        self._capturar_estado(f"Inserção de {valor} completa - Árvore balanceada")
        
        return True
    
    def excluir_animado(self, valor):
        """Remove valor capturando estados para animação"""
        # Limpa estados anteriores
        self.estados_animacao = []
        self.descricoes_animacao = []
        
        # Captura estado inicial
        self._capturar_estado(f"Estado inicial antes de excluir {valor}")
        
        no = self.buscar(valor)
        if no is None:
            print(f"⚠️  Valor {valor} não encontrado na árvore.")
            return False
        
        self._capturar_estado(f"Encontrado nó {valor} para exclusão")
        
        y = no
        y_cor_original = y.cor
        
        if no.esquerda == self.NIL:
            x = no.direita
            self._capturar_estado(f"Nó {valor} tem apenas filho direito")
            self._transplantar(no, no.direita)
        elif no.direita == self.NIL:
            x = no.esquerda
            self._capturar_estado(f"Nó {valor} tem apenas filho esquerdo")
            self._transplantar(no, no.esquerda)
        else:
            # Encontra o sucessor
            y = self._minimo(no.direita)
            y_cor_original = y.cor
            x = y.direita
            
            self._capturar_estado(f"Nó {valor} tem dois filhos - encontrando sucessor {y.valor}")
            
            if y.pai == no:
                x.pai = y
            else:
                self._transplantar(y, y.direita)
                y.direita = no.direita
                y.direita.pai = y
            
            self._transplantar(no, y)
            y.esquerda = no.esquerda
            y.esquerda.pai = y
            y.cor = no.cor
            
            self._capturar_estado(f"Substituindo {valor} pelo sucessor {y.valor}")
        
        self.tamanho -= 1
        
        if y_cor_original == Cor.PRETO:
            self._corrigir_exclusao(x, capturar_estado=True)
        
        # Captura estado final
        self._capturar_estado(f"Exclusão de {valor} completa - Árvore balanceada")
        
        return True
    
    def animar_operacao(self, intervalo=1.5):
        """Exibe animação dos estados capturados"""
        if len(self.estados_animacao) == 0:
            print("⚠️  Nenhuma operação para animar. Execute inserir_animado() ou excluir_animado() primeiro.")
            return
        
        print(f"\n🎬 Iniciando animação com {len(self.estados_animacao)} passos...")
        print("   Aguarde... As janelas gráficas serão exibidas.\n")
        
        for i, (estado, descricao) in enumerate(zip(self.estados_animacao, self.descricoes_animacao)):
            print(f"\n{'='*70}")
            print(f"📍 PASSO {i+1}/{len(self.estados_animacao)}")
            print(f"📝 {descricao}")
            print('='*70)
            
            # Cria figura para este estado
            fig, ax = plt.subplots(figsize=(16, 10))
            
            try:
                fig.canvas.manager.set_window_title(f"Animação Árvore Rubro-Negra - Passo {i+1}/{len(self.estados_animacao)}")
            except:
                pass  # Alguns backends não suportam set_window_title
            
            if estado:  # Se há nós na árvore
                G = nx.DiGraph()
                pos = {}
                cores_nos = {}
                labels = {}
                
                # Reconstrói o grafo a partir do estado
                raiz_id = self._encontrar_raiz(estado)
                if raiz_id:
                    self._construir_grafo_de_estado(raiz_id, estado, G, pos, cores_nos, labels, x=0, y=0, nivel=1, espaco=8)
                    
                    # Desenha arestas
                    nx.draw_networkx_edges(G, pos, ax=ax, arrows=False, width=2.5, edge_color='#555555')
                    
                    # Desenha nós
                    for node_id in G.nodes():
                        x, y = pos[node_id]
                        cor = 'red' if cores_nos[node_id] == Cor.VERMELHO else 'black'
                        
                        # Círculo do nó
                        circle = plt.Circle((x, y), 0.35, color=cor, ec='black', linewidth=3, zorder=3)
                        ax.add_patch(circle)
                        
                        # Texto do valor
                        ax.text(x, y, str(labels[node_id]), ha='center', va='center',
                               fontsize=14, fontweight='bold', color='white', zorder=4)
                
                # Calcula altura para ajustar visualização
                altura_atual = self._calcular_altura_estado(estado)
                ax.set_xlim(-10, 10)
                ax.set_ylim(-altura_atual - 1, 1)
            else:
                ax.text(0, 0, 'Árvore Vazia', ha='center', va='center', fontsize=20)
                ax.set_xlim(-5, 5)
                ax.set_ylim(-2, 2)
            
            ax.axis('off')
            ax.set_aspect('equal')
            
            # Título com destaque
            plt.suptitle("🎬 ANIMAÇÃO: ÁRVORE RUBRO-NEGRA", fontsize=16, fontweight='bold', y=0.98)
            plt.title(f"Passo {i+1}/{len(self.estados_animacao)}: {descricao}", 
                     fontsize=13, pad=20, wrap=True)
            
            # Legenda
            vermelho_patch = mpatches.Patch(color='red', label='Nó Vermelho')
            preto_patch = mpatches.Patch(color='black', label='Nó Preto')
            plt.legend(handles=[vermelho_patch, preto_patch], loc='upper right', fontsize=11)
            
            # Informações e instrução
            info_text = f"Frame {i+1}/{len(self.estados_animacao)}"
            plt.figtext(0.5, 0.02, info_text, ha='center', fontsize=12,
                       bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, edgecolor='orange', linewidth=2))
            
            plt.tight_layout()
            
            # Mostra a figura e aguarda
            if i < len(self.estados_animacao) - 1:
                plt.show(block=False)
                plt.pause(0.1)
                input("   ⏸️  Pressione ENTER para próximo passo... ")
                plt.close(fig)
            else:
                print(f"\n{'='*70}")
                print("✅ ANIMAÇÃO CONCLUÍDA!")
                print(f"{'='*70}\n")
                plt.show(block=True)
    
    def _encontrar_raiz(self, estado):
        """Encontra ID da raiz no estado"""
        # A raiz é o nó que não tem pai
        for node_id, dados in estado.items():
            if dados['pai_id'] is None:
                return node_id
        return None
    
    def _construir_grafo_de_estado(self, node_id, estado, G, pos, cores, labels, x, y, nivel, espaco):
        """Constrói grafo a partir do estado"""
        if node_id is None or node_id not in estado:
            return
        
        dados = estado[node_id]
        G.add_node(node_id)
        pos[node_id] = (x, -nivel)
        cores[node_id] = dados['cor']
        labels[node_id] = dados['valor']
        
        espaco_filho = espaco / 2
        
        if dados['esquerda_id']:
            G.add_edge(node_id, dados['esquerda_id'])
            self._construir_grafo_de_estado(dados['esquerda_id'], estado, G, pos, cores, labels,
                                           x - espaco_filho, y - 1, nivel + 1, espaco_filho)
        
        if dados['direita_id']:
            G.add_edge(node_id, dados['direita_id'])
            self._construir_grafo_de_estado(dados['direita_id'], estado, G, pos, cores, labels,
                                           x + espaco_filho, y - 1, nivel + 1, espaco_filho)
    
    def _calcular_altura_estado(self, estado):
        """Calcula altura do estado"""
        if not estado:
            return 0
        raiz_id = self._encontrar_raiz(estado)
        if raiz_id is None:
            return 0
        return self._calcular_altura_no_estado(raiz_id, estado)
    
    def _calcular_altura_no_estado(self, node_id, estado):
        """Calcula altura do nó no estado"""
        if node_id is None or node_id not in estado:
            return 0
        
        dados = estado[node_id]
        altura_esq = self._calcular_altura_no_estado(dados['esquerda_id'], estado)
        altura_dir = self._calcular_altura_no_estado(dados['direita_id'], estado)
        
        return 1 + max(altura_esq, altura_dir)
    
    def visualizar(self, titulo="Árvore Rubro-Negra", salvar=None):
        """Visualiza árvore usando matplotlib"""
        if self.raiz == self.NIL:
            print("⚠️  Árvore vazia!")
            return
        
        fig, ax = plt.subplots(figsize=(16, 10))
        
        # Cria o grafo usando NetworkX
        G = nx.DiGraph()
        pos = {}
        cores = {}
        labels = {}
        
        # Constrói o grafo
        self._construir_grafo(self.raiz, G, pos, cores, labels, x=0, y=0, nivel=1, espaco=8)
        
        # Desenha as arestas
        nx.draw_networkx_edges(G, pos, ax=ax, arrows=False, width=2, edge_color='gray')
        
        # Desenha os nós
        for no in G.nodes():
            x, y = pos[no]
            cor = 'red' if cores[no] == Cor.VERMELHO else 'black'
            cor_texto = 'white'
            
            # Desenha o círculo do nó
            circle = plt.Circle((x, y), 0.3, color=cor, ec='black', linewidth=2, zorder=3)
            ax.add_patch(circle)
            
            # Adiciona o texto
            ax.text(x, y, str(labels[no]), ha='center', va='center', 
                   fontsize=12, fontweight='bold', color=cor_texto, zorder=4)
        
        # Configurações do gráfico
        ax.set_xlim(-10, 10)
        ax.set_ylim(-self.altura() - 1, 1)
        ax.axis('off')
        ax.set_aspect('equal')
        
        # Adiciona título e informações
        plt.title(titulo, fontsize=16, fontweight='bold', pad=20)
        
        # Adiciona legenda
        vermelho_patch = mpatches.Patch(color='red', label='Nó Vermelho')
        preto_patch = mpatches.Patch(color='black', label='Nó Preto')
        plt.legend(handles=[vermelho_patch, preto_patch], loc='upper right')
        
        # Adiciona informações da árvore
        info_text = f"Nós: {len(self)} | Altura: {self.altura()} | Altura Preta: {self.altura_preta()}"
        plt.figtext(0.5, 0.02, info_text, ha='center', fontsize=12, 
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        
        if salvar:
            plt.savefig(salvar, dpi=300, bbox_inches='tight')
            print(f"✅ Árvore salva em: {salvar}")
        
        plt.show()
    
    def _construir_grafo(self, no, G, pos, cores, labels, x, y, nivel, espaco):
        """Constrói grafo recursivamente"""
        if no == self.NIL:
            return
        
        node_id = id(no)
        G.add_node(node_id)
        pos[node_id] = (x, -nivel)
        cores[node_id] = no.cor
        labels[node_id] = no.valor
        
        espaco_filho = espaco / 2
        
        if no.esquerda != self.NIL:
            filho_esq_id = id(no.esquerda)
            G.add_edge(node_id, filho_esq_id)
            self._construir_grafo(no.esquerda, G, pos, cores, labels, 
                                 x - espaco_filho, y - 1, nivel + 1, espaco_filho)
        
        if no.direita != self.NIL:
            filho_dir_id = id(no.direita)
            G.add_edge(node_id, filho_dir_id)
            self._construir_grafo(no.direita, G, pos, cores, labels, 
                                 x + espaco_filho, y - 1, nivel + 1, espaco_filho)
    
    def imprimir_estrutura(self):
        """Imprime estrutura hierárquica da árvore"""
        print("\n" + "="*60)
        print("ESTRUTURA DA ÁRVORE RUBRO-NEGRA")
        print("="*60)
        self._imprimir_estrutura_aux(self.raiz, "", True)
        print("="*60 + "\n")
    
    def _imprimir_estrutura_aux(self, no, prefixo, é_direita):
        """Imprime estrutura recursivamente"""
        if no != self.NIL:
            print(prefixo + ("└── " if é_direita else "├── ") + str(no))
            
            novo_prefixo = prefixo + ("    " if é_direita else "│   ")
            
            if no.esquerda != self.NIL or no.direita != self.NIL:
                self._imprimir_estrutura_aux(no.esquerda, novo_prefixo, False)
                self._imprimir_estrutura_aux(no.direita, novo_prefixo, True)


def menu():
    """Exibe menu de opções"""
    print("\n" + "="*60)
    print("   ÁRVORE RUBRO-NEGRA - MENU DE OPERAÇÕES")
    print("="*60)
    print("1  - Inserir valor")
    print("2  - Excluir valor")
    print("3  - Buscar valor")
    print("4  - Visualizar árvore (gráfico)")
    print("5  - Imprimir estrutura (texto)")
    print("6  - Mostrar percursos (in/pre/pós-ordem)")
    print("7  - Mostrar informações da árvore")
    print("8  - Inserir múltiplos valores")
    print("9  - Limpar árvore e criar exemplo com 21+ nós")
    print("A  - 🎬 ANIMAÇÃO: Inserir valor")
    print("B  - 🎬 ANIMAÇÃO: Excluir valor")
    print("0  - Sair")
    print("="*60)


def main():
    """Função principal"""
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "   IMPLEMENTAÇÃO DE ÁRVORE RUBRO-NEGRA (RED-BLACK TREE)".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    arvore = ArvoreRubroNegra()
    
    # Cria árvore inicial com mais de 21 nós
    print("\n🌳 Criando árvore inicial com 21 nós...")
    valores_iniciais = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93, 
                       3, 9, 15, 21, 28, 34, 40, 46, 53, 59]
    
    for valor in valores_iniciais:
        arvore.inserir(valor)
    
    print(f"✅ Árvore criada com {len(arvore)} nós!")
    arvore.imprimir_estrutura()
    
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            try:
                valor = int(input("Digite o valor a inserir: "))
                if arvore.inserir(valor):
                    print(f"✅ Valor {valor} inserido com sucesso!")
                    print(f"📊 Árvore agora tem {len(arvore)} nós")
            except ValueError:
                print("❌ Valor inválido!")
        
        elif opcao == "2":
            try:
                valor = int(input("Digite o valor a excluir: "))
                if arvore.excluir(valor):
                    print(f"✅ Valor {valor} excluído com sucesso!")
                    print(f"📊 Árvore agora tem {len(arvore)} nós")
            except ValueError:
                print("❌ Valor inválido!")
        
        elif opcao == "3":
            try:
                valor = int(input("Digite o valor a buscar: "))
                resultado = arvore.buscar(valor)
                if resultado:
                    print(f"✅ Valor {valor} encontrado na árvore!")
                    print(f"   Cor: {'VERMELHO' if resultado.cor == Cor.VERMELHO else 'PRETO'}")
                else:
                    print(f"❌ Valor {valor} não encontrado na árvore.")
            except ValueError:
                print("❌ Valor inválido!")
        
        elif opcao == "4":
            arvore.visualizar()
        
        elif opcao == "5":
            arvore.imprimir_estrutura()
        
        elif opcao == "6":
            print("\n📋 PERCURSOS DA ÁRVORE:")
            print(f"   Em ordem (in-order):   {arvore.em_ordem()}")
            print(f"   Pré-ordem (pre-order): {arvore.pre_ordem()}")
            print(f"   Pós-ordem (post-order): {arvore.pos_ordem()}")
        
        elif opcao == "7":
            print("\n📊 INFORMAÇÕES DA ÁRVORE:")
            print(f"   Número de nós: {len(arvore)}")
            print(f"   Altura total: {arvore.altura()}")
            print(f"   Altura preta: {arvore.altura_preta()}")
            print(f"   Raiz: {arvore.raiz.valor if arvore.raiz != arvore.NIL else 'Vazia'}")
        
        elif opcao == "8":
            entrada = input("Digite os valores separados por espaço: ")
            try:
                valores = [int(v) for v in entrada.split()]
                inseridos = 0
                for valor in valores:
                    if arvore.inserir(valor):
                        inseridos += 1
                print(f"✅ {inseridos}/{len(valores)} valores inseridos com sucesso!")
                print(f"📊 Árvore agora tem {len(arvore)} nós")
            except ValueError:
                print("❌ Valores inválidos!")
        
        elif opcao == "9":
            arvore = ArvoreRubroNegra()
            print("\n🌳 Criando nova árvore com 21+ nós...")
            for valor in valores_iniciais:
                arvore.inserir(valor)
            print(f"✅ Nova árvore criada com {len(arvore)} nós!")
            arvore.imprimir_estrutura()
        
        elif opcao.upper() == "A":
            try:
                valor = int(input("Digite o valor a inserir (com animação): "))
                print(f"\n🎬 Preparando animação da inserção de {valor}...")
                if arvore.inserir_animado(valor):
                    print(f"\n✅ Valor {valor} inserido com sucesso!")
                    print(f"📊 Árvore agora tem {len(arvore)} nós")
                    arvore.animar_operacao()
            except ValueError:
                print("❌ Valor inválido!")
        
        elif opcao.upper() == "B":
            try:
                valor = int(input("Digite o valor a excluir (com animação): "))
                print(f"\n🎬 Preparando animação da exclusão de {valor}...")
                if arvore.excluir_animado(valor):
                    print(f"\n✅ Valor {valor} excluído com sucesso!")
                    print(f"📊 Árvore agora tem {len(arvore)} nós")
                    arvore.animar_operacao()
            except ValueError:
                print("❌ Valor inválido!")
        
        elif opcao == "0":
            print("\n👋 Encerrando programa. Até logo!")
            break
        
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
