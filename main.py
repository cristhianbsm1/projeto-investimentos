from interface.menu import Menu

def main():    

  while True:
    opcao = Menu().menu_principal()

    if opcao == "s":
      break
    
    Menu().selecionar_opcao(opcao)

if __name__ == "__main__":
    main()