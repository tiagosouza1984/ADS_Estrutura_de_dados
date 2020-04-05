

'''implemente uma funcao troca, 
que recebe uma lista e duas posicoes,
e troca os valores das duas posicoes. 
Um exemplo:
   troca(['a','b','c'],0,1) deve retornar ['b','a','c']
Um exemplo diferente:
   troca(['a','b','c'],0,2) deve retornar ['c','b','a']
      '''
def troca(lista,pos1,pos2):
  if pos1 != pos2:
    last = lista.pop(pos2)
    first = lista.pop(pos1)
  else:
    return lista
  lista.insert(pos1, last)
  lista.insert(pos2, first)
  return lista

'''implemente uma funcao indice_menor, 
que recebe uma lista e devolve o indice do seu menor elemento. 
Se houver mais de um menor elemento, retorna o indice menor.
por exemplo, a=[2,3,1] indice_menor(a) retorna 2, pois a[2]==1

Dica: talvez você queira usar a função "indices" que está no arquivo
de revisão de python, no classroom

NAO USE "atalhos" do python, como lista.index nem min(lista)
'''
def indice_menor(lista):
  menor= lista[0]
  indice = 0
  for x in range(len(lista)):
    if lista[x] <= menor:
      menor = lista[x]
      indice = x
  return indice

'''
Monte uma função quebra em dois 
que recebe uma lista L e um numero D

Ela devolve duas listas: uma dos numeros de L menores que D
e a outra, dos numeros de L maiores que D.

Se L tiver algum números igual a D, ele deve ser colocado na segunda lista
'''

def quebra_em_dois(lista,divisor):
    maiores = []
    menores = []
    for x in range(len(lista)):
      if lista[x]< divisor:
        menores.append(lista[x])
      else:
        maiores.append(lista[x])
    return menores, maiores

'''
Defina uma função merge que faz o seguinte:
    Dadas duas listas ordenadas L1 e L2, 
    retorna uma lista ordenada com todos os números de L1 e L2.

    A função NAO deve usar o método sort do python.

    Em vez disso, faça o seguinte:
       * Crie um indice i1 para a lista L1 e um i2 para L2
       * Inicialize i1 e i2 com 0
       * Compare L1[i1] com L2[i2] e coloque o menor dos dois
       na lista de resposta. Se o menor era L1[i1], aumente i1.
       Caso contrário, aumente i2
       * Assim, L1[i1] e L2[i2] são sempre os menores elementos
       de L1 e L2, e um  deles é sempre o proximo que deve entrar 
       na resposta
       * Continue fazendo isso até adicionar todos os elementos
       de L1 e L2 na resposta
'''
def merge(lista1,lista2):
  resposta = []
  i1=0
  i2=0
  if len(lista1) == 0 and len(lista2) == 0:
    return list([])
  while len(resposta) < len(lista1)+len(lista2):
    if len(lista1) == 0:
      return lista2
    elif len(lista2) == 0:
      return lista1
    elif lista1[i1] < lista2[i2]:
      resposta.append(lista1[i1])
      i1+=1
      if i1 == len(lista1):
        for x in range(i2, len(lista2)):
          resposta.append(lista2[x])
        return resposta
    else:
      resposta.append(lista2[i2])
      i2+=1
      if i2 == len(lista2):
        for x in range(i1, len(lista1)):
          resposta.append(lista1[x])
        return resposta 
    if len(resposta) >= len(lista1)+len(lista2):
      break

import unittest
class TestStringMethods(unittest.TestCase):
   
    def test_00_troca(self):
        self.assertEqual(
          troca([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],5,6), 
          [3,44,38,5,47,36,15,26,27,2,46,4,19,50,48])
        self.assertEqual(
          troca([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],5,5), 
          [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48])
        self.assertEqual(
          troca([3,44],0,1), 
          [44,3])
        self.assertEqual(
          troca([3],0,0), 
          [3])

    def test_01_indice_menor(self):
        self.assertEqual(
          indice_menor([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          9)
        self.assertEqual(
          indice_menor([3,44,38,5,47,15,36,26,27,46,4,19,50,48]), 
          0)
        self.assertEqual(
          indice_menor([44,38,5,47,15,36,26,27,46,4,19,50,48]), 
          9)
    
    def test_02_quebra(self):
        self.assertEqual(
          quebra_em_dois([1,2,3,4,5,5,6,7],4),
          ([1, 2, 3], [4, 5, 5, 6, 7]))

        self.assertEqual(
          quebra_em_dois([10,20,30,40,5,5,6,7],4),
          ([], [10, 20, 30, 40, 5, 5, 6, 7]))

        self.assertEqual(
          quebra_em_dois([10,20,30,40,5,5,6,7],100),
          ([10, 20, 30, 40, 5, 5, 6, 7], []))
    
    
    def test_03_merge_simple(self):
        self.assertEqual(merge([1,2,3],[4,5,6]), [1,2,3,4,5,6])
        self.assertEqual(merge([1,3,5],[2,4,6]), [1,2,3,4,5,6])
    
    def test_04_merge_vazios(self):
        self.assertEqual(merge([1,2,3],[]), [1,2,3])
        self.assertEqual(merge([],[2,4,6]), [2,4,6])
        self.assertEqual(merge([],[]), [])
    
    
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == "__main__":
    runTests()
    
    