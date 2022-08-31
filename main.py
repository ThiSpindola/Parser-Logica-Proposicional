# Thiago Oliveira Spindola
"""
    Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a
  linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional
  escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma
  da expressão (sintaxe).

    A entrada será fornecida por um arquivo de textos que será carregado em linha de comando,
  com a seguinte formatação:
    1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões
  lógicas estão no arquivo.
    2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.

    A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída
  para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.

    Gramática:
    Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.
    Constante="T"|"F".
    Proposicao=[a−z0−9]+
    FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
    FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
      AbreParen="("
      FechaParen=")"
      OperatorUnario="¬"
      OperatorBinario="∨"|"∧"|"→"|"↔"

      " ¬ " \neg
      " ∨ " \lor
      " ∧ " \land
      " → " \Rightarrow
      " ↔ " \Leftrightarrow

    Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação,
  conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
  Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em
  qualquer expressão de entrada.

    Para  validar  seu  trabalho,  você  deve  incluir  no  repl.it,  no  mínimo  três  arquivos  contendo
  números  diferentes  de  expressões  proposicionais.  O  professor  irá  incluir  um  arquivo  de  testes  extra
  para validar seu trabalho. Para isso, caberá ao professor incluir o arquivo no seu repl.it e rodar o seu
  programa carregando o arquivo de testes.
"""
import re

pattern = re.compile(r'[a-z0-9]')


def readFile(txt):
    with open(txt) as file:
        entrada = file.readline()
        quantidade = (int)(entrada[0])

        print(txt + "\n")

        for l in range(quantidade):

            entrada = file.readline()
            entrada = entrada.rstrip("\n")
            formula = entrada.split()
            valido = Formula(formula)

            if quantidade == 0:
                print("")
                break

            quantidade -= 1

            if valido:
                print("'" + entrada + "'" + " é válida.")
            else:
                print("'" + entrada + "'" + " é inválida.")


def Formula(formula):
    if not formula:
        return True

    qParenteses = 0

    for l in formula:
        if l == '(':
            qParenteses += 1
        elif l == ')':
            qParenteses -= 1
            if qParenteses == 0:
                break

    if pattern.fullmatch(formula[0]) is not None:
        if len(formula) == 1:
            del formula[0]
            return Formula(formula)

    if formula[0] == 'T' or formula[0] == 'F':
        del formula[0]
        return Formula(formula)

    elif formula[0] == '(':
        if formula[-1] != ')':
            return False

        elif formula[1] == r'\neg':
            return FormulaUnaria(formula)

        elif formula[1] == r'\lor' or formula[1] == r'\land' or formula[1] == r'\Rightarrow' or formula[
            1] == r'\Leftrightarrow':
            return FormulaBinaria(formula)

        else:
            return False

    else:
        return False


def FormulaUnaria(formula):
    qParenteses = 0
    formulaUn = []

    for i in formula:
        formulaUn.append(i)
        if i == '(':
            qParenteses += 1
        elif i == ')':
            qParenteses -= 1
            if qParenteses == 0:
                break
            else:
                return False

    newF = formulaUn.copy()
    del newF[0]
    del newF[-1]
    del newF[0]

    if pattern.fullmatch(newF[0]) is not None:
        del newF[0]
    else:
        return False

    if not newF:
        del formula[0:len(formulaUn)]
        return Formula(formula)


def FormulaBinaria(formula):
    formulaBin = []
    qParenteses = 0
    aberto = True
    unarios = 0

    for i in formula:
        formulaBin.append(i)
        if i == '(':
            qParenteses += 1
        elif i == ')':
            qParenteses -= 1
            if qParenteses == 0:
                aberto = False
                break
        if i == r'\neg':
            unarios += 1
    if aberto:
        return False

    newF = formulaBin.copy()
    del newF[0]
    del newF[-1]

    for i in range(unarios):
        newF.remove(r'\neg')
        newF.remove('(')
        newF.remove(')')

    if newF[0] == r'\lor' or newF[0] == r'\land' or newF[0] == r'\Rightarrow' or newF[0] == r'\Leftrightarrow':
        del newF[0]

    else:
        return False

    if len(newF) > 2:
        return False
    else:
        del newF[0]
        del newF[0]

    if not newF:
        del formula[0:len(formulaBin)]
        return Formula(formula)


readFile("Texto_1.txt")
print('')
readFile("Texto_2.txt")
print('')
readFile("Texto_3.txt")
