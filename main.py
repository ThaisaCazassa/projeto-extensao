from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class Cadastro(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20  # Adiciona um padding de 20 pixels em todos os lados
        self.spacing = 10  # Espaçamento entre os widgets

        # Layout central para centralizar tudo
        central_layout = BoxLayout(orientation='vertical', size_hint=(None, None))
        central_layout.width = 300  # Largura fixa para centralizar melhor
        central_layout.height = 400  # Altura fixa para centralizar melhor

        # Título. Linha única
        titulo_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=30)
        titulo_label = Label(text='Título:', size_hint=(None, 1), width=70)
        titulo_layout.add_widget(titulo_label)
        self.titulo = TextInput(size_hint=(None, 1), width=200, multiline=False)
        titulo_layout.add_widget(self.titulo)
        self.add_widget(titulo_layout)

        # Autor. Linha única
        autor_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=30)
        autor_label = Label(text='Autor:', size_hint=(None, 1), width=70)
        autor_layout.add_widget(autor_label)
        self.autor = TextInput(size_hint=(None, 1), width=200, multiline=False)
        autor_layout.add_widget(self.autor)
        self.add_widget(autor_layout)

        #Editora. Linha única
        editora_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=30)
        editora_label = Label(text='Editora:', size_hint=(None, 1), width=70)
        editora_layout.add_widget(editora_label)
        self.editora = TextInput(size_hint=(None, 1), width=200, multiline=False)
        editora_layout.add_widget(self.editora)
        self.add_widget(editora_layout)

        #Edição. Linha única
        edicao_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=30)
        edicao_label = Label(text='Edição:', size_hint=(None, 1), width=70)
        edicao_layout.add_widget(edicao_label)
        self.edicao = TextInput(size_hint=(None, 1), width=200, multiline=False)
        edicao_layout.add_widget(self.edicao)
        self.add_widget(edicao_layout)

        #Condição. Linha única
        condicao_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=30)
        condicao_label = Label(text='Condição:', size_hint=(None, 1), width=70)
        condicao_layout.add_widget(condicao_label)
        self.condicao = TextInput(size_hint=(None, 1), width=200, multiline=False)
        condicao_layout.add_widget(self.condicao)
        self.add_widget(condicao_layout)

        #Botão Salvar
        self.submit = Button(text='Salvar', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        self.submit.bind(on_press=self.salvar)
        self.add_widget(self.submit)

        # Adiciona o layout centralizado ao layout principal
        self.add_widget(central_layout)
        central_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

    def salvar(self, instance):
        print(f"Título: {self.titulo.text}")
        print(f"Autor: {self.autor.text}")
        print(f"Editora: {self.editora.text}")
        print(f"Edição: {self.edicao.text}")
        print(f"Condição: {self.condicao.text}")


class CadastroApp(App):
    def build(self):
        Window.size = (360, 640)  # Definir um tamanho padrão adequado para dispositivos móveis
        return Cadastro()

if __name__ == '__main__':
    CadastroApp().run()
