import tkinter as tk
from views.app import DeskAppGUI


def main():
    janela_principal = tk.Tk()
    app = DeskAppGUI(janela_principal)
    janela_principal.mainloop()

if __name__ == "__main__":
    main()