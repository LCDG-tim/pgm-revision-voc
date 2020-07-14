# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

"""
interface pour vocabulaire.py
"""

import tkinter as tk


import random


from vocabulaire import voc


class List_button:

    def __init__(self, main, i: int, name: str) -> None:
        self.main = main
        self.name = name
        self.frame = (
                self.main.rightl_frame,
                self.main.leftl_frame
            )[i <= (len(voc().keys()) // 2)]
        self.button = tk.Button(
                self.frame,
                text=self.name,
                command=self.give_name
            )

    def give_name(self) -> None:
        self.main.liste_cible = self.name
        self.main.only_a_list.set(1)
        self.main.list_label["text"] = \
            "list studied : {}".format(self.name)
        self.main.change_word()


class App:
    """app de mot de vocabulaire
    """

    def __init__(self) -> None:
        # =====================================================================
        # init & config window

        self.window = tk.Tk()
        self.window.geometry("1080x720+10+10")
        self.window.title("revise ton voc")
        self.window.config(bg="#777777")
        self.window.minsize(480, 500)
        self.window.maxsize(
                self.window.winfo_screenwidth(),
                self.window.winfo_screenheight()
            )
        # =====================================================================

        # set language
        self.french_first = False

        # set main frame
        self.master_frame = tk.Frame(self.window, bg="#777777")

        # =====================================================================
        # set left window
        self.left_frame = tk.Frame(self.master_frame, bg="#777777", padx=20)

        # set default list studied
        self.liste_cible = 0.01

        # set & display the currently list studied
        self.list_label = tk.Label(
                self.left_frame,
                font=("Helvetica", 20),
                text="list studied : {}".format(self.liste_cible)
            )
        self.list_label.pack(fill=tk.X)

        # set & display the text of the vocabulary word asked
        self.first_entry = tk.Label(
                self.left_frame,
                bg="#2020A5",
                font=("Helvetica", 20)
            )
        self.first_entry.pack(fill=tk.X)

        # set & display the entry to let the users try to complete
        self.second_entry = tk.Entry(
                self.left_frame,
                bg="#20A520",
                justify="center",
                font=("Helvetica", 20)
            )
        self.second_entry.pack(fill=tk.X)

        # set & display the text to see if the second entry is True or False
        self.verif_label = tk.Label(
                self.left_frame,
                font=("Helvetica", 20)
            )
        self.verif_label.pack(fill=tk.X)

        # set & display the text to let the users have a solutio
        self.solut_label = tk.Label(
                self.left_frame,
                bg="#777777",
                font=("Helvetica", 20)
            )
        self.solut_label.pack(fill=tk.X)

        # display the left frame ont the left
        self.left_frame.grid(row=0, column=0, sticky=tk.W)
        # =====================================================================

        # =====================================================================
        # set the right_frame to put the button
        self.button_frame = tk.Frame(self.master_frame)

        # set & display the button to change the language asked and answered
        self.language_button = tk.Button(
                self.button_frame,
                text="change language to {}".format(
                        ("French", "German")[self.french_first]
                    ),
                font=("Helvetica", 20),
                command=self.change_language
            )
        self.language_button.pack(fill=tk.X)

        # set & display the button to open
        self.list_selector_button = tk.Button(
                self.button_frame,
                text="choice a list",
                font=("Helvetica", 20),
                command=self.list_app
            )
        self.list_selector_button.pack(fill=tk.X)

        self.next_word = tk.Button(
                self.button_frame,
                text="Next word",
                font=("Helvetica", 20),
                command=self.change_word
            )
        self.next_word.pack(fill=tk.X)

        self.verif_button = tk.Button(
                self.button_frame,
                text="Verification",
                font=("Helvetica", 20),
                command=self.verif
            )
        self.verif_button.pack(fill=tk.X)

        self.only_a_list = tk.Scale(
                self.button_frame,
                orient="horizontal",
                from_=0,
                to=1,
                font=("Helvetica", 20),
                label="Only a list"
            )
        self.only_a_list.pack(expand=tk.YES, fill=tk.X)

        self.solut_button = tk.Button(
                self.button_frame,
                text="solution",
                font=("Helvetica", 20),
                command=self.give_solution
            )
        self.solut_button.pack(expand=tk.YES)

        self.quit_button = tk.Button(
                self.button_frame,
                text="Quit the page",
                font=("Helvetica", 20),
                command=self.quit_window
            )
        self.quit_button.pack(expand=tk.YES)

        self.button_frame.grid(row=0, column=1, sticky=tk.W)

        # =====================================================================
        # =====================================================================

        self.menu_bar = tk.Menu(self.master_frame)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.file_menu.add_command(
                label="quitter",
                command=self.quit_window
            )

        self.menu_bar.add_cascade(
                label="fichier",
                menu=self.file_menu
            )

        self.command_menu = tk.Menu(
                self.window,
                tearoff=0
            )

        self.command_menu.add_command(
                label="change language",
                command=self.change_language
            )

        self.command_menu.add_command(
                label="next word",
                command=self.change_word
            )

        self.command_menu.add_command(
                label="verification",
                command=self.verif
            )

        self.command_menu.add_command(
                label="solution",
                command=self.give_solution
            )

        self.menu_bar.add_cascade(
                label="commands",
                menu=self.command_menu
            )

        self.master_frame.pack(expand=tk.YES)

        self.window.config(menu=self.menu_bar)

        self.change_word()

        self.window.mainloop()

    def list_app(self) -> None:
        self.windowl = tk.Tk()
        self.windowl.geometry("1080x720+20+0")
        self.windowl.minsize(200, 650)
        self.windowl.maxsize(
                self.windowl.winfo_screenwidth(),
                self.windowl.winfo_screenheight()
            )
        self.windowl.config(bg="#777777")

        self.masterl_frame = tk.Frame(self.windowl, bg="#777777")

        self.leftl_frame = tk.Frame(self.masterl_frame, bg="#777777")
        self.rightl_frame = tk.Frame(self.masterl_frame, bg="#777777")

        for i, j in enumerate(voc().keys()):
            self.test = List_button(self, i, j).button
            self.test.pack(fill=tk.X, padx=3, pady=3)

        self.leftl_frame.grid(
                row=0,
                column=0,
                sticky=tk.W
            )

        self.rightl_frame.grid(
                row=0,
                column=1,
                sticky=tk.W
            )

        self.masterl_frame.pack(expand=tk.YES)

        self.windowl.mainloop()

    def quit_windowl(self) -> None:
        self.windowl.quit()
        self.windowl.destroy()

    def verif(self) -> None:
        if self.second_entry.get() == self.answer:
            self.verif_label["text"] = "Bon"
            self.verif_label["bg"] = "#20A520"
        else:
            self.verif_label["text"] = "Faux"
            self.verif_label["bg"] = "#A52020"

    def choix(self) -> tuple:
        if not self.only_a_list.get():
            self.liste_cible = random.choice(list(voc().keys()))
        self.list_label["text"] = "liste étudiée : {}".format(self.liste_cible)
        return_value = random.choice(list(voc().get(self.liste_cible).items()))
        return return_value

    def quit_window(self) -> None:
        self.window.quit()
        self.window.destroy()

    def change_word(self) -> None:
        # il nettoye le champs
        self.second_entry.delete(0, tk.END)
        # il choisie le nouveau couple de vocabulaire
        new = self.choix()
        self.question, self.answer = (new, (new[1], new[0]))[self.french_first]
        self.first_entry["text"] = self.question
        self.verif_label["bg"] = "#777777"
        self.verif_label["text"] = ""
        self.solut_label["text"] = ""
        self.second_entry["width"] = len(self.answer) + 10

    def give_solution(self) -> None:
        self.solut_label["text"] = "{}: {}".format(
                ("solution", "Lösung")[self.french_first],
                self.answer
            )

    def change_language(self) -> None:
        self.french_first = not(self.french_first)
        self.language_button["text"] = "change language to {}".format(
                        ("French", "German")[self.french_first]
                    )
        a = self.question
        self.question = self.answer
        self.answer = a
        del a
        self.first_entry["text"] = self.question
        self.solut_label["text"] = ""
        self.second_entry.delete(0, tk.END)


if __name__ == "__main__":
    main = App()
