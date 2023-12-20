
class Question:
    def __init__(self, question_text, options, correct_option):
        self.question = question_text
        self.options = options
        self.answer = correct_option


# Lista de perguntas
questions_data = [
    Question(
        "Qual é a capital do Brasil?",
        ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"],
        "Brasília"
    ),
    Question(
        "Quem é o autor de 'Dom Quixote'?",
        ["Miguel de Cervantes", "William Shakespeare", "Charles Dickens", "Jane Austen"],
        "Miguel de Cervantes"
    ),
    Question(
        "Quantos lados tem um triângulo?",
        ["Dois", "Três", "Quatro", "Cinco"],
        "Três"
    )
]

itens = [
    {
        'pergunta': 'Qual desses partidos possui mais senadores?',
        'alternativas': ['PSD', 'PT', 'PL', 'MDB'],
        'resposta_correta': 'PSD'
    },
    {
        'pergunta': 'Qual desses partidos possui menos senadores?',
        'alternativas': ['PP', 'NOVO', 'PSB', 'PODEMOS'],
        'resposta_correta': 'NOVO'
    },
    {
        'pergunta': 'Quantos senadores possui o partido com mais senadores?',
        'alternativas': ['15', '21', '12', '17'],
        'resposta_correta': '15'
    },
    {
        'pergunta': 'Qual desses partidos possui mais deputados federais?',
        'alternativas': ['PL', 'PT', 'UNIÃO', 'PP'],
        'resposta_correta': 'PL'
    },
    {
        'pergunta': 'Qual desses partidos possui menos deputados federais?',
        'alternativas': ['REDE', 'NOVO', 'CIDADANIA', 'SOLIDARIEDADE'],
        'resposta_correta': 'REDE'
    },
    {
        'pergunta': 'Quantos senadores possui o partido com mais deputados federais?',
        'alternativas': ['98', '97', '96', '95'],
        'resposta_correta': '96'
    }
]

