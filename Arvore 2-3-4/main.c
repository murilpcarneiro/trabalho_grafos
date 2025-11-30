#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

typedef struct no{
	int numeros[3];
	struct no *pai;
	struct no *filhos[4];
	int quantChaves; 
}No;

typedef struct{
	No *raiz;
}Arvore_2_3_4;

No* criarNo(){
	No *novo = malloc(sizeof(No));
	
	if(novo){
		novo->numeros[0] = 0;
		novo->numeros[1] = 0;
		novo->numeros[2] = 0;
		novo->filhos[0] = NULL;
		novo->filhos[1] = NULL;
		novo->filhos[2] = NULL;
		novo->filhos[3] = NULL;
		novo->pai = NULL;
		novo->quantChaves = 0;
	}
	
	return novo;
}

int ehFolha(No *no){
	if(no == NULL) return 1;
	if(no->filhos[0]){
		return 0;
	}else{
		return 1;
	}
}

No* escolherFilho(No *no, int valor){
	int i = 0, tam = no->quantChaves;
	
	if(ehFolha(no) == 1)
		return no;
	while(i < tam && valor > no->numeros[i])
		i++;
	return no->filhos[i];
}

void dividirRaiz(No *raiz){
	No *direita, *esquerda;
	
	esquerda = criarNo();
	direita = criarNo();
	
	if(esquerda && direita){
		esquerda->numeros[0] = raiz->numeros[0];
		esquerda->filhos[0] = raiz->filhos[0];
		esquerda->filhos[1] = raiz->filhos[1];
		esquerda->pai = raiz;
		esquerda->quantChaves++;
		
		if(esquerda->filhos[0]){
			esquerda->filhos[0]->pai = esquerda;
			esquerda->filhos[1]->pai = esquerda;
		}
		
		direita->numeros[0] = raiz->numeros[2];
		direita->filhos[0] = raiz->filhos[2];
		direita->filhos[1] = raiz->filhos[3];
		direita->pai = raiz;
		direita->quantChaves++;
		
		if(direita->filhos[0]){
			direita->filhos[0]->pai = direita;
			direita->filhos[1]->pai = direita;
		}
		
		raiz->numeros[0] = raiz->numeros[1];
		raiz->numeros[1] = 0;
		raiz->numeros[2] = 0;
		raiz->filhos[0] = esquerda;
		raiz->filhos[1] = direita;
		raiz->filhos[2] = NULL;
		raiz->filhos[3] = NULL;
		raiz->quantChaves = 1;
	}else{
		printf("\n\tErro ao alocar memoria em dividirRaiz\n");
	}
}

void dividirFilho(No *no){
	No *direita, *pai = no->pai;
	int i, tam;
	
	direita = criarNo();
	
	if(direita){
		direita->numeros[0] = no->numeros[2];
		direita->filhos[0] = no->filhos[2];
		direita->filhos[1] = no->filhos[3];
		direita->pai = pai;
		direita->quantChaves++;
		
		if(direita->filhos[0]){
			direita->filhos[0]->pai = direita;
			direita->filhos[1]->pai = direita;
		}
		
		tam = pai->quantChaves - 1;
		
		if(no->numeros[1] > pai->numeros[tam]){
			pai->numeros[tam + 1] = no->numeros[1];
			pai->filhos[tam + 2] = direita;
			pai->quantChaves++;
		}else{
			for(i = tam; i >= 0; i--){
				if(no->numeros[1] < pai->numeros[i]){
					pai->numeros[i + 1] = pai->numeros[i];
					pai->filhos[i + 2] = pai->filhos[i + 1];
				}else{
					break;
				}
			}
			
			i++;
			pai->numeros[i] = no->numeros[1];
			pai->quantChaves++;
			pai->filhos[i + 1] = direita;
		}
		
		no->quantChaves = 1;
		no->numeros[1] = 0;
		no->numeros[2] = 0;
		no->filhos[2] = NULL;
		no->filhos[3] = NULL;
	}else{
		printf("\n\tErro ao alocar memoria em dividirFilho");
	}
}

void dividir(No *no){
	if(no->pai){
		dividirFilho(no);
	}else{
		dividirRaiz(no);
	}
}

void ordenar(No *no){
	int i, j, aux;
	
	for(i = 0; i < no->quantChaves - 1; i++){
		for(j = i + 1; j < no->quantChaves; j++){
			if(no->numeros[i] > no->numeros[j]){
				aux = no->numeros[i];
				no->numeros[i] = no->numeros[j];
				no->numeros[j] = aux;
			}
		}
	}
}

void inserirValor(No *raiz, int valor){
	No *aux = raiz;
	
	do{
		if(aux->quantChaves == 3){
			dividir(aux);
			
			if(aux->pai)
				aux = aux->pai;
		}
		
		aux = escolherFilho(aux, valor);
	}while(ehFolha(aux) == 0 || aux->quantChaves == 3);
	
	aux->numeros[aux->quantChaves] = valor;
	aux->quantChaves++;
	ordenar(aux);
}

void inserir(Arvore_2_3_4 *arv, int valor){
	if(arv->raiz){
		inserirValor(arv->raiz, valor);
	}else{
		arv->raiz = criarNo();
		arv->raiz->numeros[0] = valor;
		arv->raiz->quantChaves++;
	}
}

void imprimir(No *raiz, int nivel){
	int i;
	
	if(raiz){
		for(i = 0; i < nivel; i++){
			printf("\t");
		}
		
		printf(" Nivel %2d: ", nivel);
		for(i = 0; i < raiz->quantChaves; i++){
			printf("%3d", raiz->numeros[i]);
			if(i < raiz->quantChaves - 1) printf(" | ");
		}
		printf("\n");
		
		i = 0;
		while(i < 4 && raiz->filhos[i]){
			imprimir(raiz->filhos[i], nivel + 1);
			i++;
		}
	}
}

No* buscar(No *no, int valor, int nivel){
	int i;
	
	if(no){
		for(i = 0; i < no->quantChaves; i++){
			if(no->numeros[i] == valor){
				printf("\nO elemento %d esta no nivel %d na posicao %d\n", valor, nivel, i);
				return no;
			}else if(valor < no->numeros[i])
				break;
		}
		
		return buscar(no->filhos[i], valor, nivel + 1);
	}
	printf("\n\tO elemento %d nao foi encontrado!\n");
	return NULL;
}

int quantidadeChaves(No *raiz){
	int quantidade = 0;

	if(raiz){
		quantidade = raiz->quantChaves;
		quantidade += quantidadeChaves(raiz->filhos[0]);
		quantidade += quantidadeChaves(raiz->filhos[1]);
		quantidade += quantidadeChaves(raiz->filhos[2]);
		quantidade += quantidadeChaves(raiz->filhos[3]);
	}

	return quantidade;
}

int buscar_pos_valor(No *no, int valor){
	int i;
	if(!no) return -1;
	
	for(i = 0; i < no->quantChaves; i++){
		if(no->numeros[i] == valor)
			return i;
	}
	return -1;
}

int buscar_pos_filho(No *pai, No *filho){
	int i;
	if(!pai || !filho) return -1;
	
	for(i = 0; i <= pai->quantChaves; i++){
		if(pai->filhos[i] == filho)
			return i;
	}
	return -1;
}

No* buscar_no(No *raiz, int valor){
	int i;
	if(!raiz) return NULL;
	
	for(i = 0; i < raiz->quantChaves; i++){
		if(raiz->numeros[i] == valor)
			return raiz;
		else if(valor < raiz->numeros[i])
			break;
	}
	
	if(!ehFolha(raiz))
		return buscar_no(raiz->filhos[i], valor);
	
	return NULL;
}

No* encontrarPredecessorNo(No *node, int idx){
	No *atual = node->filhos[idx];
	if(!atual) return NULL;
	while(!ehFolha(atual)){
		atual = atual->filhos[atual->quantChaves];
	}
	return atual;
}

void shiftLeftFrom(No *no, int start){
	int i;
	for(i = start; i < no->quantChaves - 1; i++){
		no->numeros[i] = no->numeros[i+1];
	}
	if(no->quantChaves > 0)
		no->numeros[no->quantChaves - 1] = 0;
}

void shiftRightFrom(No *no, int start){
	int i;
	for(i = no->quantChaves; i > start; i--){
		no->numeros[i] = no->numeros[i-1];
	}
	no->numeros[start] = 0;
}

void removerChaveDaFolha(No *no, int pos){
	if(no == NULL || pos < 0 || pos >= no->quantChaves) return;
	shiftLeftFrom(no, pos);
	no->quantChaves--;
}

void atualizarPaisDosFilhos(No *no){
	int i;
	if(!no) return;
	for(i = 0; i <= no->quantChaves; i++){
		if(no->filhos[i])
			no->filhos[i]->pai = no;
	}
}

int emprestarDoEsquerdo(No *pai, int idxFilho){
	No *filho = pai->filhos[idxFilho];
	No *esq = pai->filhos[idxFilho - 1];
	if(!esq || esq->quantChaves < 2) return 0; 
	
	shiftRightFrom(filho, 0);
	
	filho->numeros[0] = pai->numeros[idxFilho - 1];
	filho->quantChaves++;
	
	pai->numeros[idxFilho - 1] = esq->numeros[esq->quantChaves - 1];
	
	if(!ehFolha(esq)){
		filho->filhos[filho->quantChaves] = filho->filhos[filho->quantChaves - 1];
		
		int i;
		for(i = filho->quantChaves - 1; i > 0; i--){
			filho->filhos[i] = filho->filhos[i-1];
		}
		filho->filhos[0] = esq->filhos[esq->quantChaves];
		esq->filhos[esq->quantChaves] = NULL;
	}
	esq->quantChaves--;
	atualizarPaisDosFilhos(filho);
	return 1;
}

int emprestarDoDireito(No *pai, int idxFilho){
	No *filho = pai->filhos[idxFilho];
	No *dir = pai->filhos[idxFilho + 1];
	if(!dir || dir->quantChaves < 2) return 0;

	filho->numeros[filho->quantChaves] = pai->numeros[idxFilho];
	filho->quantChaves++;
	
	pai->numeros[idxFilho] = dir->numeros[0];
	
	shiftLeftFrom(dir, 0);
	
	if(!ehFolha(dir)){
		filho->filhos[filho->quantChaves] = dir->filhos[0];
		
		int i;
		for(i = 0; i < dir->quantChaves + 1; i++){
			dir->filhos[i] = dir->filhos[i+1];
		}
	}
	dir->quantChaves--;
	atualizarPaisDosFilhos(filho);
	return 1;
}

void mergeComEsquerdo(Arvore_2_3_4 *arv, No *pai, int idxFilho){
	No *filho = pai->filhos[idxFilho];
	No *esq = pai->filhos[idxFilho - 1];
	
	esq->numeros[esq->quantChaves] = pai->numeros[idxFilho - 1];
	esq->quantChaves++;
	
	int i;
	for(i = 0; i < filho->quantChaves; i++){
		esq->numeros[esq->quantChaves + i] = filho->numeros[i];
	}
	
	int base = esq->quantChaves;
	for(i = 0; i <= filho->quantChaves; i++){
		esq->filhos[base + i] = filho->filhos[i];
		if(esq->filhos[base + i]) esq->filhos[base + i]->pai = esq;
	}
	esq->quantChaves += filho->quantChaves;
	
	int j;
	for(j = idxFilho - 1; j < pai->quantChaves - 1; j++){
		pai->numeros[j] = pai->numeros[j+1];
		pai->filhos[j+1] = pai->filhos[j+2];
	}
	pai->filhos[pai->quantChaves] = NULL;
	pai->quantChaves--;
	
	free(filho);
	
	if(pai->quantChaves == 0 && pai == arv->raiz){
		esq->pai = NULL;
		arv->raiz = esq;
		free(pai);
	}
}

void mergeComDireito(Arvore_2_3_4 *arv, No *pai, int idxFilho){
	No *filho = pai->filhos[idxFilho];
	No *dir = pai->filhos[idxFilho + 1];
	
	filho->numeros[filho->quantChaves] = pai->numeros[idxFilho];
	filho->quantChaves++;
	
	int i;
	for(i = 0; i < dir->quantChaves; i++){
		filho->numeros[filho->quantChaves + i] = dir->numeros[i];
	}
	
	int base = filho->quantChaves;
	for(i = 0; i <= dir->quantChaves; i++){
		filho->filhos[base + i] = dir->filhos[i];
		if(filho->filhos[base + i]) filho->filhos[base + i]->pai = filho;
	}
	filho->quantChaves += dir->quantChaves;
	
	int j;
	for(j = idxFilho; j < pai->quantChaves - 1; j++){
		pai->numeros[j] = pai->numeros[j+1];
		pai->filhos[j+1] = pai->filhos[j+2];
	}
	pai->filhos[pai->quantChaves] = NULL;
	pai->quantChaves--;
	
	free(dir);

	if(pai->quantChaves == 0 && pai == arv->raiz){
		filho->pai = NULL;
		arv->raiz = filho;
		free(pai);
	}
}

void corrigirUnderflow(Arvore_2_3_4 *arv, No *no){
	if(no == NULL) return;
	if(no == arv->raiz){
		
		if(arv->raiz->quantChaves == 0){
			if(arv->raiz->filhos[0]){
				No *nova = arv->raiz->filhos[0];
				nova->pai = NULL;
				free(arv->raiz);
				arv->raiz = nova;
			}else{
				free(arv->raiz);
				arv->raiz = NULL;
			}
		}
		return;
	}
	No *pai = no->pai;
	if(!pai) return;
	int idx = buscar_pos_filho(pai, no);

	if(idx > 0 && pai->filhos[idx - 1] && pai->filhos[idx - 1]->quantChaves > 1){
		emprestarDoEsquerdo(pai, idx);
		return;
	}

	if(idx < pai->quantChaves && pai->filhos[idx + 1] && pai->filhos[idx + 1]->quantChaves > 1){
		emprestarDoDireito(pai, idx);
		return;
	}

	if(idx > 0){
		mergeComEsquerdo(arv, pai, idx);
		corrigirUnderflow(arv, pai);
	}else{
		
		mergeComDireito(arv, pai, idx);
		corrigirUnderflow(arv, pai);
	}
}


void removerRec(Arvore_2_3_4 *arv, No *node, int valor){
	if(!node) return;
	int pos = buscar_pos_valor(node, valor);
	if(pos != -1){
		
		if(!ehFolha(node)){
			
			No *predNo = encontrarPredecessorNo(node, pos);
			int predVal = predNo->numeros[predNo->quantChaves - 1];
			
			node->numeros[pos] = predVal;
			
			removerRec(arv, predNo, predVal);
		}else{
		
			removerChaveDaFolha(node, pos);
			
			if(node->quantChaves >= 1) return;
			
			corrigirUnderflow(arv, node);
		}
	}else{
		
		int i;
		for(i = 0; i < node->quantChaves; i++){
			if(valor < node->numeros[i]) break;
		}
		No *filho = node->filhos[i];
		if(!filho){
			
			printf("\n\tO elemento %d nao foi encontrado!\n", valor);
			return;
		}
	
		removerRec(arv, filho, valor);
	}
}

void remover(Arvore_2_3_4 *arv, int valor){
	if(!arv->raiz){
		printf("\n\tArvore vazia.\n");
		return;
	}
	removerRec(arv, arv->raiz, valor);
}

int main() {
	Arvore_2_3_4 arv;
	arv.raiz = NULL;
	int opcao;
	
	do{
		printf("Digite o valor a ser inserido ou 0 para finalizar: ");
		scanf("%d", &opcao);
		
		if(opcao != 0)
			inserir(&arv, opcao);
		
		printf("\n\tARVORE 2 3 4 \n\n");
		imprimir(arv.raiz, 0);
		printf("\n");
	}while(opcao != 0);
	
	imprimir(arv.raiz, 0);
	printf("\nQuantidade de chaves: %d\n", quantidadeChaves(arv.raiz));
	
	do{
		printf("\nDigite o valor a ser buscado ou 0 para finalizar: ");
		scanf("%d", &opcao);
		if(opcao != 0)
			buscar(arv.raiz, opcao, 0);
	}while(opcao != 0);
	
	do{
		printf("\nDigite o valor a ser removido ou 0 para finalizar: ");
		scanf("%d", &opcao);
		printf("\n");
		
		if(opcao != 0){
			remover(&arv, opcao);
			imprimir(arv.raiz, 0);
			printf("\n");
		}
	}while(opcao != 0);
    
    return 0;
}

