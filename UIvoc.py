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
        # set main font
        self.main_font = ("Helvetica", 20)

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
                font=self.main_font,
                text="list studied : {}".format(self.liste_cible)
            )
        self.list_label.pack(fill=tk.X)

        # set & display the text of the vocabulary word asked
        self.first_entry = tk.Label(
                self.left_frame,
                bg="#2020A5",
                font=self.main_font
            )
        self.first_entry.pack(fill=tk.X)

        # set & display the entry to let the users try to complete
        self.second_entry = tk.Entry(
                self.left_frame,
                bg="#20A520",
                justify="center",
                font=self.main_font
            )
        self.second_entry.pack(fill=tk.X)

        # set & display the text to see if the second entry is True or False
        self.verif_label = tk.Label(
                self.left_frame,
                font=self.main_font
            )
        self.verif_label.pack(fill=tk.X)

        # set & display the text to let the users have a solutio
        self.solut_label = tk.Label(
                self.left_frame,
                bg="#777777",
                font=self.main_font
            )
        self.solut_label.pack(fill=tk.X)

        # set the default score and the number of word
        self.good_replies = 0
        self.number_words = 0

        # set & display the button to setup a score of right replies
        self.score_label = tk.Label(
                self.left_frame,
                bg="#777777",
                text="",
                font=self.main_font
            )
        self.score_label.pack(fill=tk.X)

        # display the left frame ont the left
        self.left_frame.grid(row=0, column=0, sticky=tk.W)
        # =====================================================================

        # =====================================================================
        # set the right_frame to put the button
        self.button_frame = tk.Frame(self.master_frame)

        # set & display the label to advert the goal of the right frame
        self.advert_label = tk.Label(
                self.button_frame,
                text="List of Button"
            )
        self.advert_label.pack(fill=tk.X)

        # set & display the button to change the language asked and answered
        self.language_button = tk.Button(
                self.button_frame,
                text="switch language to {}".format(
                        ("French", "German")[self.french_first]
                    ),
                font=self.main_font,
                command=self.change_language
            )
        self.language_button.pack(fill=tk.X)

        # set & display the button to open the list of list of vocabulary
        self.list_selector_button = tk.Button(
                self.button_frame,
                text="choice a list",
                font=self.main_font,
                command=self.list_app
            )
        self.list_selector_button.pack(fill=tk.X)

        # set & display the Scale for set or unset the random list mode
        self.only_a_list = tk.Scale(
                self.button_frame,
                orient="horizontal",
                from_=0,
                to=1,
                font=self.main_font,
                label="Only a list"
            )
        self.only_a_list.pack(fill=tk.X)

        # set & display the button to change the word asked
        self.next_word = tk.Button(
                self.button_frame,
                text="Next word",
                font=self.main_font,
                command=self.change_word
            )
        self.next_word.pack(fill=tk.X)

        # set & display the button to verify if the word in the second entry
        # is True or False
        self.verif_button = tk.Button(
                self.button_frame,
                text="Verification",
                font=self.main_font,
                command=self.verif
            )
        self.verif_button.pack(fill=tk.X)

        # set & display the Button to display the solution, the translation of
        # the word
        self.solut_button = tk.Button(
                self.button_frame,
                text="solution",
                font=self.main_font,
                command=self.give_solution
            )
        self.solut_button.pack(fill=tk.X)

        # set & display the button to add 1 at the score
        self.score_button = tk.Button(
                self.button_frame,
                text="add score",
                font=self.main_font,
                command=self.add_score
            )
        self.score_button.pack(fill=tk.X)

        # set & display the button to quit the page
        self.quit_button = tk.Button(
                self.button_frame,
                text="Quit the page",
                font=self.main_font,
                command=self.quit_window
            )
        self.quit_button.pack(fill=tk.X)

        # display the right button frame
        self.button_frame.grid(row=0, column=1, sticky=tk.W)
        # =====================================================================

        # =====================================================================
        # set the menu bar of the window
        self.menu_bar = tk.Menu(self.master_frame)

        # set the first menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        # add a command to the first menu to quit the page
        self.file_menu.add_command(
                label="quitter",
                command=self.quit_window
            )

        # add the menu to the menu bar
        self.menu_bar.add_cascade(
                label="fichier",
                menu=self.file_menu
            )

        # set a second menu with all the command which can be used in the App
        self.command_menu = tk.Menu(
                self.window,
                tearoff=0
            )

        # add a command to switch language
        self.command_menu.add_command(
                label="switch language",
                command=self.change_language
            )

        # add a command to open the list selector
        self.command_menu.add_command(
                label="chose a specific list",
                command=self.list_app
            )

        # add a command to change word
        self.command_menu.add_command(
                label="next word",
                command=self.change_word
            )

        # add a command to verify the second entry
        self.command_menu.add_command(
                label="verification",
                command=self.verif
            )

        # add a command to give the solution, the translation
        self.command_menu.add_command(
                label="solution",
                command=self.give_solution
            )

        # add the menu to the menu bar
        self.menu_bar.add_cascade(
                label="commands",
                menu=self.command_menu
            )
        # =====================================================================

        # =====================================================================
        # display the main frame
        self.master_frame.pack(expand=tk.YES)

        # add the menu bar to the window
        self.window.config(menu=self.menu_bar)

        # put a random word
        self.change_word()

        # launch the page
        self.window.mainloop()
        # =====================================================================

    def list_app(self) -> None:
        # config window
        self.windowl = tk.Tk()
        self.windowl.geometry("200x650+100+20")
        self.windowl.minsize(200, 650)
        self.windowl.maxsize(
                self.windowl.winfo_screenwidth(),
                self.windowl.winfo_screenheight()
            )
        self.windowl.config(bg="#777777")

        # set master frame
        self.masterl_frame = tk.Frame(self.windowl, bg="#777777")

        # set the left and right frame
        self.leftl_frame = tk.Frame(self.masterl_frame, bg="#777777")
        self.rightl_frame = tk.Frame(self.masterl_frame, bg="#777777")

        # create the button to select the list
        for i, j in enumerate(voc().keys()):
            self.test = List_button(self, i, j).button
            self.test.pack(fill=tk.X, padx=3, pady=3)

        # display the two frame
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

        # display the master frame
        self.masterl_frame.pack(expand=tk.YES)

        # lauch the window
        self.windowl.mainloop()

    def score_manage(self) -> None:
        self.windows = tk.Tk()
        self.windows.geometry("400x450+100+20")
        self.windows.minsize(400, 450)
        self.windows.maxsize(
                self.windows.winfo_screenwidth(),
                self.windows.winfo_screenheight()
            )
        self.windows.config(bg="#777777")

        # set master frame
        self.masters_frame = tk.Frame(self.windows, bg="#777777")

        # set and display the main score display
        self.current_score = tk.Label(
                self.masters_frame,
                text="{} / {} or {} % good replies".format(
                        self.good_replies,
                        self.number_words,
                        round(self.good_replies * 100 / self.number_words, 1)
                    ),
                font=self.main_font
            )
        self.current_score.pack(fill=tk.X)

        # set and display the number of good replies enumerate
        self.good_label = tk.Label(
                self.masters_frame,
                font=self.main_font,
                text="good replies : {}".format(self.good_replies)
            )
        self.good_label.pack(fill=tk.X)

        # set and display the number of words which are asked
        self.number_label = tk.Label(
                self.masters_frame,
                text="number of words asked : {}".format(
                        self.number_words
                    ),
                font=self.main_font
            )

        # display the master frame
        self.masters_frame.pack(expand=tk.YES)

        # lauch the window
        self.windows.mainloop()

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

    def add_score(self) -> None:
        self.good_replies += 1
        self.score_label["text"] = "{} / {} or {} % of right replies".format(
                        self.good_replies,
                        self.number_words,
                        round(self.good_replies * 100 / self.number_words, 1)
                    )

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
        self.number_words += 1
        self.score_label["text"] = "{} / {} or {} % of right replies".format(
                        self.good_replies,
                        self.number_words,
                        round(self.good_replies * 100 / self.number_words, 1)
                    )
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
        self.language_button["text"] = "switch language to {}".format(
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
