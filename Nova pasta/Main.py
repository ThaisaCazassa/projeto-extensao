from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.config import Config

# Define o tamanho da tela e desativa o cursor vermelho
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class LogoApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Adiciona a logo (use o caminho para a sua imagem)
        logo = Image(source='logo.png', size_hint=(1, 1.5))
        layout.add_widget(logo)

        # Adiciona dois botões com os nomes especificados
        button1 = Button(
            text='Cadastrar novo livro', 
            size_hint=(1, 0.1),
            background_normal='',
            background_color=(0.1, 0.5, 0.6, 1),  # Cor de fundo do botão
            color=(1, 1, 1, 1)  # Cor do texto
        )
        
        button2 = Button(
            text='Pesquisar livros', 
            size_hint=(1, 0.1),
            background_normal='',
            background_color=(0.1, 0.5, 0.6, 1),  # Cor de fundo do botão
            color=(1, 1, 1, 1)  # Cor do texto
        )

        layout.add_widget(button1)
        layout.add_widget(button2)

        return layout

if __name__ == '__main__':
    LogoApp().run()
