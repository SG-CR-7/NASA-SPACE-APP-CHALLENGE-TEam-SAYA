import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.uix.popup import Popup
lang='en'
# Language dictionary
LANGUAGES = {
    'en': {
        'title': "Eco Explorer Jr.",
        'temperature_game': "Temperature Observation Game",
        'cloud_game': "Cloud Identification Game",
        'enter_temp': "Enter the temperature you observed (in °C):",
        'enter_cloud': "Is the sky clear or cloudy?",
        'enter_ph': "Enter water pH level (0-14):",
        'submit': "Submit",
        'temp_result': "Actual temperature: ",
        'cloud_result': "Sky condition: ",
        'water_result': "Water pH is: ",
        "Nice! It's a sunny day!": "Nice! It's a sunny day!",
        "Looks like it's cloudy!": "Looks like it's cloudy!",
        "Please enter 'clear' or 'cloudy'.": "Please enter 'clear' or 'cloudy'.",
        'home': "Home",
        'quiz_game': "Environment Quiz"  # Fixed key
    },
    'es': {
        'title': "Explorador Eco Jr.",
        'temperature_game': "Juego de Observación de Temperatura",
        'cloud_game': "Juego de Identificación de Nubes",
        'enter_temp': "Introduce la temperatura que observaste (en °C):",
        'enter_cloud': "¿Está despejado o nublado?",
        'enter_ph': "Introduce el nivel de pH del agua (0-14):",
        'submit': "Enviar",
        'temp_result': "Temperatura real: ",
        'cloud_result': "Condición del cielo: ",
        'water_result': "El pH del agua es: ",
        "Nice! It's a sunny day!": "¡LINDO! ES UN DÍA SOLEADO",
        "Looks like it's cloudy!": "¡PARECE QUE ESTÁ NUBLADO!",
        "Please enter 'clear' or 'cloudy'.": "Por favor ingrese claro o nublado.",
        'home': "Inicio",
        'quiz_game': "Cuestionario Ambiental"  # Fixed key
    },
    'fr': {
        'title': "Explorateur Eco Jr.",
        'temperature_game': "Jeu d'Observation de Température",
        'cloud_game': "Jeu d'Identification des Nuages",
        'enter_temp': "Entrez la température observée (en °C):",
        'enter_cloud': "Le ciel est-il dégagé ou nuageux?",
        'enter_ph': "Entrez le niveau de pH de l'eau (0-14):",
        'submit': "Soumettre",
        'temp_result': "Température réelle: ",
        'cloud_result': "État du ciel: ",
        'water_result': "Le pH de l'eau est: ",
        "Nice! It's a sunny day!": "BON! C'EST UNE JOURNÉE ENSOLEILLÉE",
        "Looks like it's cloudy!": "ON DIRAIT QUE C'EST NUAGEUX !",
        "Please enter 'clear' or 'cloudy'.": "Veuillez entrer clair ou nuageux.",
        'home': "Accueil",
        'quiz_game': "Quiz Environnemental"  # Fixed key
    }
}

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.current_lang = 'en'  # Default language
        self.layout = BoxLayout(orientation='vertical', padding=10)

        # Language Selector
        self.lang_spinner = Spinner(
            text="English",  # Default language in spinner
            values=('English', 'Spanish', 'French'),
            size_hint=(0.5, 0.2)
        )
        self.lang_spinner.bind(text=self.set_language)
        self.layout.add_widget(self.lang_spinner)

        # Title and buttons that depend on the selected language
        self.title_label = Label(text=LANGUAGES[self.current_lang]['title'], font_size=24)
        self.layout.add_widget(self.title_label)

        self.python_button = Button(text=LANGUAGES[self.current_lang]['temperature_game'], font_size=20)
        self.python_button.bind(on_press=self.go_to_python)
        self.layout.add_widget(self.python_button)

        self.cloud_button = Button(text=LANGUAGES[self.current_lang]['cloud_game'], font_size=20)
        self.cloud_button.bind(on_press=self.go_to_js)
        self.layout.add_widget(self.cloud_button)

        self.quiz_button = Button(text=LANGUAGES[self.current_lang]['quiz_game'], font_size=20)  # Fixed button text
        self.quiz_button.bind(on_press=self.go_to_quiz)
        self.layout.add_widget(self.quiz_button)

        self.add_widget(self.layout)

    def set_language(self, spinner, text):
        global lang
        if text == 'English':
            self.current_lang = 'en'
        elif text == 'Spanish':
            self.current_lang = 'es'
        elif text == 'French':
            self.current_lang = 'fr'
        lang=self.current_lang
        # Update button texts and title based on selected language
        self.title_label.text = LANGUAGES[self.current_lang]['title']
        self.python_button.text = LANGUAGES[self.current_lang]['temperature_game']
        self.cloud_button.text = LANGUAGES[self.current_lang]['cloud_game']
        self.quiz_button.text = LANGUAGES[self.current_lang]['quiz_game']  # Updated correctly

    def go_to_python(self, instance):
        global lang
        self.manager.get_screen('python_game').current_lang = self.current_lang
        self.manager.current = "python_game"
        lang=self.current_lang
    def go_to_js(self, instance):
        global lang
        self.manager.get_screen('js_game').current_lang = self.current_lang
        self.manager.current = "js_game"
        lang=self.current_lang
    def go_to_quiz(self, instance):
        global lang,sm
        self.manager.get_screen('quiz').current_lang = self.current_lang
        lang=self.current_lang
        print("lang go to", lang)
        sm.add_widget(Quiz(name='quiz'))
        self.manager.current = "quiz"


class PythonGame(Screen):
    def __init__(self, **kwargs):
        super(PythonGame, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10)

        self.temp_input = TextInput(hint_text="", font_size=20)
        self.submit_button = Button(text="", font_size=20)
        self.result_label = Label(text="", font_size=20)
        self.weather_image = Image(source="default.png")

        # Home button to return to the main menu
        self.home_button = Button(text="", font_size=20)

        self.layout.add_widget(self.temp_input)
        self.layout.add_widget(self.submit_button)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.weather_image)
        self.layout.add_widget(self.home_button)

        self.submit_button.bind(on_press=self.check_temperature)
        self.home_button.bind(on_press=self.go_home)

        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.temp_input.hint_text = LANGUAGES[self.current_lang]['enter_temp']
        self.submit_button.text = LANGUAGES[self.current_lang]['submit']
        self.home_button.text = LANGUAGES[self.current_lang]['home']

    def check_temperature(self, instance):
        try:
            temp = float(self.temp_input.text)
            real_temp = round(random.uniform(-10, 40), 1)

            self.result_label.text = LANGUAGES[self.current_lang]['temp_result'] + f"{real_temp}°C"

            if real_temp <= 0:
                self.weather_image.source = "snowflake.png"
            elif real_temp <= 20:
                self.weather_image.source = "cloud.png"
            else:
                self.weather_image.source = "sun.png"
        except ValueError:
            self.result_label.text = "Please enter a valid number!"

    def go_home(self, instance):
        self.manager.current = 'main_menu'


class JSGame(Screen):
    def __init__(self, **kwargs):
        super(JSGame, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10)

        self.cloud_input = TextInput(hint_text="", font_size=20)
        self.submit_button = Button(text="", font_size=20)
        self.result_label = Label(text="", font_size=20)
        self.cloud_image = Image(source="cloud.png", size_hint=(None, None), size=(200, 200))

        # Home button to return to the main menu
        self.home_button = Button(text="", font_size=20)

        self.layout.add_widget(self.cloud_input)
        self.layout.add_widget(self.submit_button)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.cloud_image)
        self.layout.add_widget(self.home_button)

        self.submit_button.bind(on_press=self.check_cloud)
        self.home_button.bind(on_press=self.go_home)

        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.cloud_input.hint_text = LANGUAGES[self.current_lang]['enter_cloud']
        self.submit_button.text = LANGUAGES[self.current_lang]['submit']
        self.home_button.text = LANGUAGES[self.current_lang]['home']

    def check_cloud(self, instance):
        cloud_status = self.cloud_input.text.lower()
        if cloud_status == "clear":
            self.result_label.text = LANGUAGES[self.current_lang]["Nice! It's a sunny day!"]
            self.cloud_image.source = "sun.png"
        elif cloud_status == "cloudy":
            self.result_label.text = LANGUAGES[self.current_lang]["Looks like it's cloudy!"]
            self.cloud_image.source = "cloud.png"
        else:
            self.result_label.text = LANGUAGES[self.current_lang]["Please enter 'clear' or 'cloudy'."]

    def go_home(self, instance):
        self.manager.current = 'main_menu'
from kivy.uix.dropdown import DropDown
class Quiz(Screen):
    def __init__(self, **kwargs):
        super(Quiz, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10)
        global lang

        # Add a language selection button
        self.language_button = Button(text=f"Language: {lang}", font_size=20)
        print('lang',lang)
        self.language_button.bind(on_release=self.show_language_dropdown)
        self.layout.add_widget(self.language_button)

        # Quiz data in different languages (English, Spanish, French)
        self.create_quiz_data()
        
        self.current_question_index = 0
        self.score = 0

        # Question label
        self.question_label = Label(text="", font_size=20)
        self.layout.add_widget(self.question_label)

        # Answer choice buttons
        self.choice_buttons = []
        for i in range(4):  # Assume there are always 4 choices per question
            btn = Button(text="", font_size=20)
            btn.bind(on_press=self.check_answer)
            self.choice_buttons.append(btn)
            self.layout.add_widget(btn)

        # Score label
        self.score_label = Label(text="Score: 0", font_size=18)
        self.layout.add_widget(self.score_label)

        # Button to return to the main menu

        self.add_widget(self.layout)
        self.show_question()

    def create_quiz_data(self):
        """Creates the quiz data for different languages."""
        self.questions = {
            'en': [  # English questions
                {'question': "What is the main cause of global warming?", 'choices': ["Greenhouse gases", "Deforestation", "Ozone depletion", "Pollution"], 'correct': 0},
                {'question': "Which gas is most responsible for the greenhouse effect?", 'choices': ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], 'correct': 1},
                {'question': "What is the largest source of renewable energy?", 'choices': ["Solar", "Wind", "Hydro", "Geothermal"], 'correct': 2},
                {
                'question': "Which of the following is a non-renewable resource?",
                'choices': ["Solar", "Wind", "Coal", "Hydro"],
                'correct': 2
            },
            {
                'question': "What is the main component of natural gas?",
                'choices': ["Methane", "Ethane", "Propane", "Butane"],
                'correct': 0
            },
            {
                'question': "Which country emits the most carbon dioxide?",
                'choices': ["USA", "China", "India", "Russia"],
                'correct': 1
            },
            {
                'question': "What is the process by which plants make their food?",
                'choices': ["Photosynthesis", "Respiration", "Transpiration", "Digestion"],
                'correct': 0
            },
            {
                'question': "Which layer of the atmosphere contains the ozone layer?",
                'choices': ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
                'correct': 1
            },
            {
                'question': "What is the main cause of ocean acidification?",
                'choices': ["Plastic pollution", "Oil spills", "Carbon dioxide", "Overfishing"],
                'correct': 2
            },
            {
                'question': "Which of the following is a greenhouse gas?",
                'choices': ["Oxygen", "Nitrogen", "Methane", "Argon"],
                'correct': 2
            },
            {
                'question': "What is the main source of energy for the Earth?",
                'choices': ["Wind", "Sun", "Water", "Geothermal"],
                'correct': 1
            },
            {
                'question': "Which of the following is a biodegradable material?",
                'choices': ["Plastic", "Glass", "Paper", "Metal"],
                'correct': 2
            },
            {
                'question': "What is the main cause of deforestation?",
                'choices': ["Urbanization", "Agriculture", "Logging", "All of the above"],
                'correct': 3
            },
            {
                'question': "Which of the following is a consequence of global warming?",
                'choices': ["Rising sea levels", "Increased biodiversity", "More stable weather patterns", "Decreased temperatures"],
                'correct': 0
            },
            {
                'question': "What is the main purpose of the Paris Agreement?",
                'choices': ["Reduce plastic waste", "Combat climate change", "Protect endangered species", "Promote renewable energy"],
                'correct': 1
            }
            ],
            'es': [  # Spanish questions
                {'question': "¿Cuál es la principal causa del calentamiento global?", 'choices': ["Gases de efecto invernadero", "Deforestación", "Depleción del ozono", "Contaminación"], 'correct': 0},
                {'question': "¿Qué gas es el más responsable del efecto invernadero?", 'choices': ["Oxígeno", "Dióxido de carbono", "Nitrógeno", "Hidrógeno"], 'correct': 1},
                {'question': "¿Cuál es la mayor fuente de energía renovable?", 'choices': ["Solar", "Eólica", "Hidráulica", "Geotérmica"], 'correct': 2},
                {
                    'question': "¿Cuál de los siguientes es un recurso no renovable?",
                    'choices': ["Solar", "Eólica", "Carbón", "Hidráulica"],
                    'correct': 2
                },
                {
                    'question': "¿Cuál es el componente principal del gas natural?",
                    'choices': ["Metano", "Etano", "Propano", "Butano"],
                    'correct': 0
                },
                {
                    'question': "¿Qué país emite más dióxido de carbono?",
                    'choices': ["EE. UU.", "China", "India", "Rusia"],
                    'correct': 1
                },
                {
                    'question': "¿Cuál es el proceso por el cual las plantas producen su alimento?",
                    'choices': ["Fotosíntesis", "Respiración", "Transpiración", "Digestión"],
                    'correct': 0
                },
                {
                    'question': "¿Qué capa de la atmósfera contiene la capa de ozono?",
                    'choices': ["Troposfera", "Estratosfera", "Mesosfera", "Termosfera"],
                    'correct': 1
                },
                {
                    'question': "¿Cuál es la principal causa de la acidificación del océano?",
                    'choices': ["Contaminación plástica", "Derrames de petróleo", "Dióxido de carbono", "Sobrepesca"],
                    'correct': 2
                },
                {
                    'question': "¿Cuál de los siguientes es un gas de efecto invernadero?",
                    'choices': ["Oxígeno", "Nitrógeno", "Metano", "Argón"],
                    'correct': 2
                },
                {
                    'question': "¿Cuál es la principal fuente de energía para la Tierra?",
                    'choices': ["Eólica", "Solar", "Hidráulica", "Geotérmica"],
                    'correct': 1
                },
                {
                    'question': "¿Cuál de los siguientes es un material biodegradable?",
                    'choices': ["Plástico", "Vidrio", "Papel", "Metal"],
                    'correct': 2
                },
                {
                    'question': "¿Cuál es la principal causa de la deforestación?",
                    'choices': ["Urbanización", "Agricultura", "Aprovechamiento de madera", "Todas las anteriores"],
                    'correct': 3
                },
                {
                    'question': "¿Cuál de las siguientes es una consecuencia del calentamiento global?",
                    'choices': ["Aumento del nivel del mar", "Mayor biodiversidad", "Patrones climáticos más estables", "Disminución de las temperaturas"],
                    'correct': 0
                },
                {
                    'question': "¿Cuál es el principal propósito del Acuerdo de París?",
                    'choices': ["Reducir los residuos plásticos", "Combatir el cambio climático", "Proteger especies en peligro", "Promover la energía renovable"],
                    'correct': 1
                }
            ],
            'fr': [  # French questions
                {'question': "Quelle est la principale cause du réchauffement climatique ?", 'choices': ["Gaz à effet de serre", "Déforestation", "Appauvrissement de l'ozone", "Pollution"], 'correct': 0},
                {'question': "Quel gaz est le plus responsable de l'effet de serre ?", 'choices': ["Oxygène", "Dioxyde de carbone", "Azote", "Hydrogène"], 'correct': 1},
                {'question': "Quelle est la plus grande source d'énergie renouvelable ?", 'choices': ["Solaire", "Éolienne", "Hydroélectrique", "Géothermique"], 'correct': 2},
                {
                    'question': "Lequel des éléments suivants est une ressource non renouvelable ?",
                    'choices': ["Solaire", "Éolienne", "Charbon", "Hydroélectrique"],
                    'correct': 2
                },
                {
                    'question': "Quel est le principal composant du gaz naturel ?",
                    'choices': ["Méthane", "Éthane", "Propane", "Butane"],
                    'correct': 0
                },
                {
                    'question': "Quel pays émet le plus de dioxyde de carbone ?",
                    'choices': ["États-Unis", "Chine", "Inde", "Russie"],
                    'correct': 1
                },
                {
                    'question': "Quel est le processus par lequel les plantes produisent leur nourriture ?",
                    'choices': ["Photosynthèse", "Respiration", "Transpiration", "Digestion"],
                    'correct': 0
                },
                {
                    'question': "Quelle couche de l'atmosphère contient la couche d'ozone ?",
                    'choices': ["Troposphère", "Stratosphère", "Mésosphère", "Thermosphère"],
                    'correct': 1
                },
                {
                    'question': "Quelle est la principale cause de l'acidification des océans ?",
                    'choices': ["Pollution plastique", "Marées noires", "Dioxyde de carbone", "Surpêche"],
                    'correct': 2
                },
                {
                    'question': "Lequel des éléments suivants est un gaz à effet de serre ?",
                    'choices': ["Oxygène", "Azote", "Méthane", "Argon"],
                    'correct': 2
                },
                {
                    'question': "Quelle est la principale source d'énergie de la Terre ?",
                    'choices': ["Éolienne", "Solaire", "Hydroélectrique", "Géothermique"],
                    'correct': 1
                },
                {
                    'question': "Lequel des éléments suivants est un matériau biodégradable ?",
                    'choices': ["Plastique", "Verre", "Papier", "Métal"],
                    'correct': 2
                },
                {
                    'question': "Quelle est la principale cause de la déforestation ?",
                    'choices': ["Urbanisation", "Agriculture", "Exploitation forestière", "Toutes les réponses ci-dessus"],
                    'correct': 3
                },
                {
                    'question': "Laquelle des conséquences suivantes résulte du réchauffement climatique ?",
                    'choices': ["Élévation du niveau de la mer", "Augmentation de la biodiversité", "Modèles climatiques plus stables", "Diminution des températures"],
                    'correct': 0
                },
                {
                    'question': "Quel est le principal objectif de l'Accord de Paris ?",
                    'choices': ["Réduire les déchets plastiques", "Lutter contre le changement climatique", "Protéger les espèces menacées", "Promouvoir les énergies renouvelables"],
                    'correct': 1
                }
            ]
        }
        self.home_button_text = {
            'en': "Home",
            'es': "Inicio",
            'fr': "Accueil"
        }
        self.current_language = lang
        print("lang beore button",self.home_button_text[lang])
        self.home_button = Button(text=f'{self.home_button_text[lang]}', font_size=20)
        self.home_button.bind(on_press=self.go_home)
        self.layout.add_widget(self.home_button)
    def show_question(self):
        """Show the current question in the selected language."""
        questions = self.questions[self.current_language]
        question_data = questions[self.current_question_index]
        self.question_label.text = question_data['question']

        # Update the answer choices
        for i, choice in enumerate(question_data['choices']):
            self.choice_buttons[i].text = choice

    def check_answer(self, instance):
        """Check if the selected answer is correct."""
        selected_answer_index = self.choice_buttons.index(instance)
        correct_answer_index = self.questions[self.current_language][self.current_question_index]['correct']

        if selected_answer_index == correct_answer_index:
            self.score += 1
            self.score_label.text = f"Score: {self.score}"

        # Move to the next question or end the quiz
        self.current_question_index += 1
        if self.current_question_index < len(self.questions[self.current_language]):
            self.show_question()
        else:
            self.show_scoreboard()

    def show_scoreboard(self):
        """Display final score and message."""
        self.question_label.text = f"You've completed the quiz! Final Score: {self.score}"
        for btn in self.choice_buttons:
            btn.disabled = True  # Disable answer buttons once quiz is over

    def go_home(self, instance):
        self.manager.current = 'main_menu'

    def show_language_dropdown(self, instance):
        """Show a dropdown to change the language."""
        dropdown = DropDown()
        for language in ['en', 'es', 'fr']:
            btn = Button(text=language.upper(), size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.change_language(btn.text.lower(), dropdown))
            dropdown.add_widget(btn)
        dropdown.open(instance)

    def change_language(self, new_lang, dropdown):
        """Change the quiz language and reset the quiz."""
        global lang
        print("change lang func", lang)
        lang = new_lang
        self.current_language = lang
        self.language_button.text = f"Language: {lang.upper()}"
        dropdown.dismiss()
        self.home_button = Button(text=f'{self.home_button_text[lang]}', font_size=20)
        # Reset the quiz in the new language
        self.current_question_index = 0
        self.score = 0
        self.score_label.text = "Score: 0"
        for btn in self.choice_buttons:
            btn.disabled = False  # Re-enable buttons for the new game
        self.show_question()
sm=ScreenManager()
class EcoExplorerApp(App):
    def build(self):
        global sm
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(PythonGame(name='python_game'))
        sm.add_widget(JSGame(name='js_game'))
        sm.add_widget(Quiz(name='quiz'))

        return sm

if __name__ == '__main__':
    EcoExplorerApp().run()
