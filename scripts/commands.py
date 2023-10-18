import os
import scripts.variables as variables


def command(command):
    if command == ".help":
        print(variables.Texts.HELP)

    elif command == ".clear":
        os.system("cls" if os.name == "nt" else "clear")

    elif command == ".exit":
        os.system("cls" if os.name == "nt" else "clear")
        exit()

    else:
        print("Command not found")