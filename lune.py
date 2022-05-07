import sys
from lark import Lark
from os import system
from lune_parser import Lune_Parser

def create_lua_file(filename, code):
  try:
    lua_program = open(filename + ".lua", "x")
    lua_program.write(code)
    lua_program.close()
  except: 
    print("Erreur(Error): Impossible d'ouvrir le fichier Lune (Unable to open Lune file).")
    print(usage_help)
    sys.exit(1)

def run_lune_program(filename, usage):
  try:
    system("lua " + filename + ".lua")
  except:
    print("Erreur(Error): Impossible d'exécuter le fichier Lune (Unable to open Lune file).")
    print(usage)
    sys.exit(1)


if __name__ == "__main__":
  usage_help = """
  Usage (Français):
    * Créer un fichier .lune et écrivez votre programme en Lune
    * Avoir le fichier .moon dans le même dossier que moon.py
    * Assurez-vous que l'interpréteur Lua est installé sur votre machine
    * Pour exécutez le programme => python lune.py xxx.lune

  Usage (English):
    * Create a .lune file and start writing your Lune program
    * Have the .lune file inside the same folder as lune.py
    * Make sure Lua interpreter is installed on your computer
    * To run the program => python lune.py xxx.lune
  """

  if len(sys.argv) != 2:
    print("Erreur(Error): Commande Invalide (Incorrect command).")
    print(usage_help)
    sys.exit(1)
  else:
    try:
      program = open(sys.argv[1], "r")
    except: 
      print("Erreur(Error): Impossible d'ouvrir le fichier Lune (Unable to open Lune file).")
      print(usage_help)
      sys.exit(1)
  
  lune_parser = Lune_Parser()
  parser = Lark.open("lune_grammar.lark", start="start", parser="earley")
  parse_tree = parser.parse(program.read())
  filename = sys.argv[1].split(".")[0]
  create_lua_file(filename, lune_parser.translate(parse_tree))
  run_prompt = input("Voulez-vous exécuter le programme (Do you want to run the program)? (Oui/Non) (Yes/No) ")
  if run_prompt.strip().lower() == "oui" or run_prompt.strip().lower() == "yes":
    run_lune_program(filename, usage_help)
  else:
    print("Vérifier le fichier .lua généré (Checkout the generated .lua file).")
  # print(translate(parse_tree))
  # print(parse_tree.pretty())