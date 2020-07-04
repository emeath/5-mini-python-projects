# 11-20 07-07-2020
#
# Projeto 2 - Mad Libs Generator
#
# Objetivo: informar adjetivos e substantivos para gerar uma história com esses dados
#
# Inspired by Summer Son’s Mad Libs project with Javascript.
#
# Nota: o que é uma 'mad lib': http://www.redkid.net/madlibs/

# TODO adicionar comentarios


class MadLib:

    script = """
    Um belo dia {0} decidiu que deveria finalizar 
    uma {1} de projetos relacionados a {2} 
    então sentou na {3} e começou a trabalhar 
    na {1} e até que conseguiu finalizar mas 
    o engraçado é que se sentiu {4} em vez
    de se sentir {5} por ter finalizado.
    """

    def gerar_mad_lib(self, lista_de_palavras):
        self.script_formatdo = MadLib.script.format(
            lista_de_palavras[0],
            lista_de_palavras[1],
            lista_de_palavras[2],
            lista_de_palavras[3],
            lista_de_palavras[4],
            lista_de_palavras[5]
        )

    def exibir_mad_lib(self):
        print(self.script_formatdo)


class Formulario:

    def set_nome(self):
        self.nome = input('Digite um nome: ')

    def set_substantivo0(self):
        self.substantivo0 = input('Digite um substantivo: ')

    def set_substantivo1(self):
        self.substantivo1 = input('Digite outro substantivo: ')

    def set_substantivo2(self):
        self.substantivo2 = input('Digite outro substantivo: ')

    def set_adjetivo0(self):
        self.adjetivo0 = input('Digite um adjetivo: ')

    def set_adjetivo1(self):
        self.adjetivo1 = input('Digite outro adjetivo: ')

    def set_informacoes_usuario(self):
        self.set_nome()
        self.set_substantivo0()
        self.set_substantivo1()
        self.set_substantivo2()
        self.set_adjetivo0()
        self.set_adjetivo1()

    def get_lista_respostas(self):
        return [self.nome,
                self.substantivo0,
                self.substantivo1,
                self.substantivo2,
                self.adjetivo0,
                self.adjetivo1]


if __name__ == '__main__':

    formulario = Formulario()
    madlib = MadLib()

    formulario.set_informacoes_usuario()

    respostas = formulario.get_lista_respostas()

    madlib.gerar_mad_lib(respostas)
    madlib.exibir_mad_lib()
