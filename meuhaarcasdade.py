# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 03:02:53 2020

@author: Luiz Cardoso
"""
#Para treinar o arquivo de um haarcascade para gerar o .xml É necessário ter as imagens
#negativas e positivas(para o problema em questao, ser ou nao ser). As negativas sempre serão as principais e estarão em maior número
#pois servirão de base. Quando se tem uma imagem positiva (a imagem normal), esta será sobreposta
#sobre todas as imagens negativas para gerar uma nova pasta

#O haarcascade pode ser utilizado para treinar com qualquer tipod e objeto

import cv2
import os
from imutils import paths
import shutil #necessária para copiar os arquivos de um diretorio para outro



def redefinirImagensD():
    
    #passando o endereço das imagens para listagem das imagens
    imagePathD = list(paths.list_images('Imagens/Desertos'))
    contador = 1
    
    if not os.path.exists('negativa'): #função da biblioteca OS que checa se existe a pasta
        os.makedirs('negativa')
    
    #loop na variavel que contem todas as imagens listadas acima
    for i in imagePathD:
        
        #fazer a renomeação das imagens (enumerando) para ficar certinho
        shutil.copy(i, i.replace(i, "negativa/"+ str(contador)+".png"))
        #Após copiar as imagens, é bom passar para escada de Cinza e redimensionar todas para padronizar
        #pega imagem atual, passa para cinza, redimensiona e depois sobrescreve.
        imgAtual = cv2.imread("negativa/"+ str(contador)+".png", cv2.IMREAD_GRAYSCALE)
        imagemRedimensionada = cv2.resize(imgAtual, (100,100))
        cv2.imwrite("negativa/"+ str(contador)+".png", imagemRedimensionada)
        
        contador +=1
        
def redefinirImagensF():
    
    #mesmo codigo, redefinindo imagens de Florestas agora
    
    imagePathF = list(paths.list_images('Imagens/Florestas'))
    contador = 1
    
    if not os.path.exists('positiva'):
        os.makedirs('positiva')
    
    for i in imagePathF:
        
        shutil.copy(i, i.replace(i, "positiva/" + str(contador) + ".png"))
        imgAtual = cv2.imread("positiva/" + str(contador) + ".png", cv2.IMREAD_GRAYSCALE)
        imagemRedimensionada = cv2.resize(imgAtual, (100,100))
        cv2.imwrite("positiva/" + str(contador) + ".png", imagemRedimensionada)
        
        contador += 1

def create_pos_n_neg():
    
    for file_type in ['negativa']:
        for img in os.listdir(file_type):
            
            if file_type == 'positiva':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open ('info.dat', 'a') as f:
                    f.write(line)
                
            elif file_type == 'negativa':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)


redefinirImagensD()
redefinirImagensF()
create_pos_n_neg()
    
    