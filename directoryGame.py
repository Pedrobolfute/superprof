import os
import random
import string

GENERATE_SIZE = 10 #max 43 (random_anime_names and random_anime_speak size)

home_dir = os.getenv('HOME')
root_dir = '/'

abc_lowercase = list(string.ascii_lowercase)
abc_uppercase = list(string.ascii_uppercase)

random_dir_names = [''] * GENERATE_SIZE
random_anime_names = [
    'Luffy', 'Zoro', 'Sanji', 'Nami', 
    'Usopp', 'Chopper', 'Robin', 'Franky', 
    'Brook', 'Jinbe', 'Vivi', 'Ace', 
    'Sabo', 'Shanks', 'Whitebeard', 'Blackbeard', 
    'Kaido', 'Big-Mom', 'Doflamingo', 'Crocodile', 
    'Buggy', 'Law', 'Kid', 'Killer', 'King',
    'Hancock', 'Rayleigh', 'Smoker', 'Tashigi', 
    'Garp', 'Dragon', 'Bartolomeo', 'Cavendish', 
    'Marco', 'Katakuri', 'Perospero', 'Jack', 'Queen',
    'Fujitora', 'Aokiji', 'Akainu', 'Kizaru', 'Benn Beckman'
]
random_anime_speak = [
    "Vou me tornar o Rei dos Piratas!",  # Luffy
    "Serei o maior espadachim do mundo.",  # Zoro
    "Onde está a carne?",  # Sanji
    "Preciso de mais berries para fazer compras.",  # Nami
    "Serei um bravo guerreiro do mar!",  # Usopp
    "Eu sou um médico!",  # Chopper
    "Conhecimento é poder.",  # Robin
    "Super!",  # Franky
    "Yohohoho! Uma piada de esqueleto!",  # Brook
    "Vou proteger os Chapéus de Palha.",  # Jinbe
    "Por Alabasta!",  # Vivi
    "Vou proteger meu irmão.",  # Ace
    "Pela liberdade e pela revolução!",  # Sabo
    "Eu acredito no Luffy.",  # Shanks
    "Para o Novo Mundo!",  # Whitebeard
    "Vou governar os mares.",  # Blackbeard
    "Eu sou a criatura mais forte!",  # Kaido
    "Mama-mama!",  # Big-Mom
    "Eu controlo as cordas.",  # Doflamingo
    "Tempestade de Areia!",  # Crocodile
    "Eu sou o grande Buggy!",  # Buggy
    "Room!",  # Law
    "Punk Gibson!",  # Kid
    "Vou seguir o Kid.",  # Killer
    "Vou proteger meu rei.",  # King
    "O amor é um furacão!",  # Hancock
    "O Rei das Trevas.",  # Rayleigh
    "Vou te fumar.",  # Smoker
    "Vou seguir ordens.",  # Tashigi
    "A justiça prevalecerá.",  # Garp
    "Pela revolução.",  # Dragon
    "Eu idolatro o Luffy!",  # Bartolomeo
    "O belo pirata.",  # Cavendish
    "Chama da Fênix!",  # Marco
    "Vou vingar minha família.",  # Katakuri
    "Doces são doces!",  # Perospero
    "A seca está aqui.",  # Jack
    "Salve a Rainha!",  # Queen
    "A justiça é cega.",  # Fujitora
    "A verdade congelante.",  # Aokiji
    "A lava governa.",  # Akainu
    "Velocidade da luz.",  # Kizaru
    "Eu protejo o Ruivo.",  # Benn Beckman
]

random_absolute_dirs = {
  'key0': [os.path.join(home_dir, 'Documentos'), 'Documentos', 'home'],
  'key1': [os.path.join(home_dir, 'Downloads'), 'Downloads', 'home'],
  'key2': [os.path.join(home_dir, 'Desktop'), 'Desktop', 'home'],
  'key3': [os.path.join(home_dir, 'Imagens'), 'Imagens', 'home'],
  'key4': [os.path.join(home_dir, 'Videos'), 'Videos', 'home'],
  'key5': [os.path.join(home_dir, 'Musica'), 'Musica', 'home'],
  'key6': [os.path.join(home_dir, 'Workspace'), 'Workspace', 'home'],
  'key7': [os.path.join(root_dir, 'tmp'), 'tmp', 'root'],
  'key8': [os.path.join(root_dir, 'tmp'), 'tmp', 'root'],
  'key9': [os.path.join(root_dir, 'tmp'), 'tmp', 'root']
}

def objectToArray(object):
  array = []
  for value in object.items():
      array.append(value)
  return array

def createDir(pathDir=home_dir, nameDir='mainGame'):
  path_way = os.path.join(pathDir, nameDir)
  os.makedirs(path_way, exist_ok=True)

def generateRandomNums(min_range, max_range):
    return random.randint(min_range, max_range)
  
def generateRandomUniqueNums(min_range, max_range, quantite):
    return random.sample(range(min_range, max_range + 1), quantite)
  
def generateRandomDirNames(qtd_times, name_size):
  for i in range(qtd_times):
    for j in range(name_size):
      randomIndex = generateRandomNums(0, 25)     
      if random.choice([True, False]):
        random_dir_names[i] += abc_lowercase[randomIndex]
      else:
        random_dir_names[i] += abc_uppercase[randomIndex]
     
    
## Messagem de Inicio do jogo
def startGame():
  path_dir = os.path.join(home_dir, 'one-piece-directory-game')
  archieveName = 'One-Piece-Menssagem.txt'
  message = "\n\n#Navege até o personagem e exclua-o! \n#Depois exclua a pasta lixo que abriga ele!\n#Á! Antes, Aproveite e veja o que eles dizem sobre você.\n#Afinal, o personagem abriga um arquivo de texto.\n\n"
  print(message)
  ## Iteração do usuário
  user_input = input("Pressione Enter para continuar ou 'q' para sair.  ")
  if user_input.lower() == 'q':
    print("Jogo abortado!")
    return
  else:
    print('...')
    os.makedirs(path_dir, exist_ok=True)
    with open(os.path.join(path_dir, archieveName), 'w') as archieve:
      archieve.write(message)
      print(message)
      createScene()
      

# Criando cenário
def createScene():
  generateRandomDirNames(GENERATE_SIZE, 25)
  randomUniqueNums = generateRandomUniqueNums(0, len(random_anime_names)-1, GENERATE_SIZE)
  print("#Exclua-me se conseguir!\n")
  
  # print("#Exclua-me se conseguir! 'Porção de cegueira lançado!!'# \n")
  # command = 'alias ave="echo Quando-se-está-cego-não-consegue-vê"'
  # os.system(f'echo "{command}"')
  
  for i in range(GENERATE_SIZE):
    myPath = random_absolute_dirs[f'key{generateRandomNums(0, 9)}'][0]
    characterName = random_anime_names[randomUniqueNums[i]]

    createDir(os.path.join(os.path.join(myPath, random_dir_names[i]), characterName), "Vazio")
    print("- " + os.path.join(os.path.join(myPath, random_dir_names[i]), characterName))
    with open(os.path.join(os.path.join(os.path.join(myPath, random_dir_names[i]), characterName), characterName+".txt"), 'w') as archieve:
      archieve.write(random_anime_speak[i])
    # print(os.path.join(os.path.join(myPath, random_dir_names[i]), characterName))

  
startGame()