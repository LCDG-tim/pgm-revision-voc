# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

"""
interface pour vocabulaire.py
"""

import tkinter as tk


import random


from vocabulaire import voc


def swicth_variables(a, b) -> tuple:
    return b, a


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

    def give_name(self, *args) -> None:
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
        self.master_frame.bind("<Escape>", self.quit_window)

        # =====================================================================
        # set left window
        self.left_frame = tk.Frame(self.master_frame, bg="#777777", padx=20)

        # set default list studied
        self.liste_cible = 0.01
        self.current_score = tk.Label()

        # set & display the currently list studied
        self.list_label = tk.Label(
                self.left_frame,
                font=self.main_font,
                text="list studied : {}".format(self.liste_cible)
            )
        self.list_label.pack(fill=tk.X, expand=tk.YES)

        # set & display the text of the vocabulary word asked
        self.first_entry = tk.Label(
                self.left_frame,
                bg="#2020A5",
                font=self.main_font
            )
        self.first_entry.pack(fill=tk.X, expand=tk.YES)

        # set & display the entry to let the users try to complete
        self.second_entry = tk.Entry(
                self.left_frame,
                bg="#20A520",
                justify="center",
                font=self.main_font
            )
        self.second_entry.pack(fill=tk.X, expand=tk.YES)
        self.second_entry.bind("<Alt-s>", self.insert_s7)
        self.second_entry.bind("<Alt-a>", self.insert_aumlaut)
        self.second_entry.bind("<Alt-u>", self.insert_uumlaut)
        self.second_entry.bind("<Alt-o>", self.insert_oumlaut)

        self.second_entry.bind("<Return>", self.verif)
        self.second_entry.bind("<Control-a>", self.give_solution)
        self.second_entry.bind("<Control-s>", self.add_score)
        self.second_entry.bind("<Shift-Return>", self.change_word)

        # set & display the text to see if the second entry is True or False
        self.verif_label = tk.Label(
                self.left_frame,
                font=self.main_font
            )
        self.verif_label.pack(fill=tk.X, expand=tk.YES)

        # set & display the text to let the users have a solutio
        self.solut_label = tk.Label(
                self.left_frame,
                bg="#777777",
                font=self.main_font
            )
        self.solut_label.pack(fill=tk.X, expand=tk.YES)

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
        self.score_label.pack(fill=tk.X, expand=tk.YES)

        # display the left frame ont the left
        self.left_frame.grid(row=0, column=0, sticky=tk.W)
        # =====================================================================

        # =====================================================================
        # set the right_frame to put the button
        self.button_frame = tk.Frame(self.master_frame)

        # set & display the label to advert the goal of the right frame
        self.advert_label = tk.Label(
                self.button_frame,
                text="List of Button",
                bg="#777777",
                fg="#DADADA",
                font=self.main_font
            )
        self.advert_label.pack(fill=tk.X, expand=tk.YES)

        # set & display the button to change the language asked and answered
        self.language_button = tk.Button(
                self.button_frame,
                text="switch language to {}".format(
                        ("French", "German")[self.french_first]
                    ),
                font=self.main_font,
                command=self.change_language
            )
        self.language_button.pack(fill=tk.X, expand=tk.YES)

        # set & display the button to open the list of list of vocabulary
        self.list_selector_button = tk.Button(
                self.button_frame,
                text="choice a list",
                font=self.main_font,
                command=self.list_app
            )
        self.list_selector_button.pack(fill=tk.X, expand=tk.YES)

        # set & display the Scale for set or unset the random list mode
        self.only_a_list = tk.Scale(
                self.button_frame,
                orient="horizontal",
                from_=0,
                to=1,
                font=self.main_font,
                label="Only a list"
            )
        self.only_a_list.pack(fill=tk.X, expand=tk.YES)

        # set & display the button to verify if the word in the second entry
        # is True or False
        self.verif_button = tk.Button(
                self.button_frame,
                text="Verification",
                font=self.main_font,
                command=self.verif
            )
        self.verif_button.pack(fill=tk.X, expand=tk.YES)

        # set & display the button to change the word asked
        self.next_word = tk.Button(
                self.button_frame,
                text="Next word",
                font=self.main_font,
                command=self.change_word
            )
        self.next_word.pack(fill=tk.X, expand=tk.YES)

        # set & display the Button to display the solution, the translation of
        # the word
        self.solut_button = tk.Button(
                self.button_frame,
                text="solution",
                font=self.main_font,
                command=self.give_solution
            )
        self.solut_button.pack(fill=tk.X, expand=tk.YES)

        # set & display the button to add 1 at the score
        self.score_button = tk.Button(
                self.button_frame,
                text="add score",
                font=self.main_font,
                command=self.add_score
            )
        self.score_button.pack(fill=tk.X, expand=tk.YES)

        # set & display the button to open the score manager
        self.test = tk.Button(
                self.button_frame,
                text="score manager",
                font=self.main_font,
                command=self.score_manage
            )
        self.test.pack(fill=tk.X, expand=tk.YES)

        # set & display the button to quit the page
        self.quit_button = tk.Button(
                self.button_frame,
                text="Quit the page",
                font=self.main_font,
                command=self.quit_window
            )
        self.quit_button.pack(fill=tk.X, expand=tk.YES)

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
                label="quit the page",
                command=self.quit_window
            )

        # add the menu to the menu bar
        self.menu_bar.add_cascade(
                label="file",
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
                label="chose a list",
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

    def insert_s7(self, *args) -> None:
        self.second_entry.insert(tk.END, "ß")

    def insert_aumlaut(self, *arg) -> None:
        self.second_entry.insert("end", "ä")

    def insert_uumlaut(self, *arg) -> None:
        self.second_entry.insert("end", "ü")

    def insert_oumlaut(self, *arg) -> None:
        self.second_entry.insert("end", "ö")

    def list_app(self, *args) -> None:
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
        self.masterl_frame.bind("<Escape>", self.quit_windowl)

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

        # =====================================================================
        # set the menu bar
        self.menu_bar_winl = tk.Menu(self.windowl)

        # set first cascade
        self.file_menu_winl = tk.Menu(self.menu_bar_winl, tearoff=0)

        # add a command
        self.file_menu_winl.add_command(
                label="quit the page",
                command=self.quit_windowl
            )

        # add the cascade to the menu bar
        self.menu_bar_winl.add_cascade(
                menu=self.file_menu_winl,
                label="file"
            )

        # add the menu bar
        self.windowl.config(menu=self.menu_bar_winl)
        # =====================================================================

        # lauch the window
        self.windowl.mainloop()

    def quit_windowl(self, *args) -> None:
        self.windowl.quit()
        self.windowl.destroy()

    def score_manage(self, *args) -> None:
        self.windows = tk.Tk()
        self.windows.geometry("600x350+200+200")
        self.windows.minsize(600, 350)
        self.windows.maxsize(
                self.windows.winfo_screenwidth(),
                self.windows.winfo_screenheight()
            )
        self.windows.config(bg="#777777")
        self.windows.bind("<Escape>", self.quit_windows)

        self.save_value = (self.good_replies, self.number_words)

        # set master frame
        self.masters_frame = tk.Frame(self.windows, bg="#A0A0A0")
        self.masters_frame.bind("<Escape>", self.quit_windows)

        # set and display the main score display
        self.current_score = tk.Label(
                self.masters_frame,
                text="{} / {} or {} % good replies".format(
                        self.good_replies,
                        self.number_words,
                        round(self.good_replies * 100 / self.number_words, 1)
                    ),
                font=self.main_font,
                bg="#A0A0A0"
            )
        self.current_score.pack(fill=tk.X, expand=tk.YES)

        # set & display the number of good replies enumerate
        self.good_label = tk.Label(
                self.masters_frame,
                font=self.main_font,
                text="good replies : {}".format(self.good_replies),
                bg="#A0A0A0"
            )
        self.good_label.pack(fill=tk.X, expand=tk.YES)

        # set the frame with the add 1 remove 1 good replied
        self.good_frame = tk.Frame(self.masters_frame, bg="#A0A0A0")

        # set the -1 frame
        self.minus1F = tk.Frame(
                self.good_frame,
                bg="#A0A0A0"
            )
        # set and display the button to remove 1 good reply
        self.remove_good_rep_button = tk.Button(
                self.minus1F,
                font=self.main_font,
                text="-1",
                command=self.remove_good_reply
            )
        self.remove_good_rep_button.pack(fill=tk.X, expand=tk.YES)

        # display the -1 frame
        self.minus1F.grid(row=0, column=0, sticky=tk.W, padx=100, pady=3)

        # set the +1 frame
        self.plus1F = tk.Frame(
                self.good_frame,
                bg="#A0A0A0"
            )

        # set & display the button to add 1 good reply
        self.add_good_rep_button = tk.Button(
                self.plus1F,
                font=self.main_font,
                text="+1",
                command=self.add_score
            )
        self.add_good_rep_button.pack(fill=tk.X, expand=tk.YES)

        # display the +1 frame
        self.plus1F.grid(row=0, column=1, sticky=tk.W, padx=100, pady=3)

        # display the frame for good word
        self.good_frame.pack(fill=tk.X, expand=tk.YES)

        # set the number frame
        self.number_frame = tk.Frame(
                self.masters_frame,
                bg="#A0A0A0"
            )

        # set & display the number of words which are asked
        self.number_label = tk.Label(
                self.masters_frame,
                text="number of words asked : {}".format(self.number_words),
                font=self.main_font,
                bg="#A0A0A0"
            )
        self.number_label.pack(fill=tk.X, expand=tk.YES)

        # set the -1 frame
        self._minus1F = tk.Frame(
                self.number_frame,
                bg="#A0A0A0"
            )

        # set & display the button to remove 1 at the number word
        self.remove_1_word_but = tk.Button(
                self._minus1F,
                text='-1',
                font=self.main_font,
                command=self.remove_word_asked
            )
        self.remove_1_word_but.pack(fill=tk.X, expand=tk.YES)

        # display the -1 frame
        self._minus1F.grid(row=0, column=0, sticky=tk.W, padx=100, pady=3)

        # set the +1 frame
        self._plus1F = tk.Frame(
                self.number_frame,
                bg="#A0A0A0"
            )

        # set & display the button to add 1 word asked
        self.add_1_word_but = tk.Button(
                self._plus1F,
                text="+1",
                font=self.main_font,
                command=self.add_word_asked
            )
        self.add_1_word_but.pack(fill=tk.X, expand=tk.YES)

        # display the +1 frame
        self._plus1F.grid(row=0, column=1, sticky=tk.W, padx=100, pady=3)

        # display the number frame
        self.number_frame.pack(fill=tk.X, expand=tk.YES)

        # set & display the button to done the modification
        self.done_button = tk.Button(
                self.masters_frame,
                font=self.main_font,
                text="done",
                command=self.quit_windows
            )
        self.done_button.pack(expand=tk.YES)

        # display the master frame
        self.masters_frame.pack(expand=tk.YES)

        # =====================================================================
        # set the menu bar
        self.menu_bar_wins = tk.Menu(self.windows)

        # set first cascade
        self.file_menu_wins = tk.Menu(self.menu_bar_wins, tearoff=0)

        # add a command 3x
        self.file_menu_wins.add_cascade(
                label="cancel modifications",
                command=self.cancel_wins
            )
        self.file_menu_wins.add_command(
                label="done",
                command=self.quit_windows
            )
        self.file_menu_wins.add_command(
                label="quit the page",
                command=self.quit_windows
            )

        # add the cascade to the menu bar
        self.menu_bar_wins.add_cascade(
                menu=self.file_menu_wins,
                label="file"
            )

        # set second cascade
        self.command_menu_wins = tk.Menu(
                self.menu_bar_wins,
                tearoff=0
            )
        # add a command 4x
        self.command_menu_wins.add_command(
                label="-1 reply",
                command=self.remove_good_reply
            )
        self.command_menu_wins.add_command(
                label="+1 reply",
                command=self.add_score
            )
        self.command_menu_wins.add_command(
                label="-1 word",
                command=self.remove_word_asked
            )
        self.command_menu_wins.add_command(
                label="+1 word",
                command=self.add_word_asked
            )

        # add the cascade to the menu bar
        self.menu_bar_wins.add_cascade(
                menu=self.command_menu_wins,
                label="commands"
            )

        # add the menu bar
        self.windows.config(menu=self.menu_bar_wins)
        # =====================================================================

        # lauch the window
        self.windows.mainloop()

    def update_score_label(self, *args) -> None:
        self.score_label["text"] = "{} / {} or {} % of right replies".format(
                        self.good_replies,
                        self.number_words,
                        round(self.good_replies * 100 / self.number_words, 1)
                    )
        self.current_score["text"] = "{} / {} or {} % of right replies".format(
                        self.good_replies,
                        self.number_words,
                        round(self.good_replies * 100 / self.number_words, 1)
                    )
        self.good_label["text"] = "good replies : {}".format(self.good_replies)
        self.number_label["text"] = "number of words asked : " \
            "{}".format(self.number_words)

    def remove_good_reply(self, *args) -> None:
        self.good_replies -= 1
        self.update_score_label()

    def add_score(self, *args) -> None:
        self.good_replies += 1
        self.update_score_label()

    def remove_word_asked(self, *args) -> None:
        self.number_words -= 1
        self.update_score_label()

    def add_word_asked(self, *args) -> None:
        self.number_words += 1
        self.update_score_label()

    def cancel_wins(self, *args) -> None:
        self.good_replies, self.number_words = self.save_value
        self.update_score_label()

    def quit_windows(self, *args) -> None:
        self.windows.quit()
        self.windows.destroy()

    def verif(self, *args) -> None:
        if self.second_entry.get() == self.answer:
            self.verif_label["text"] = "Bon"
            self.verif_label["bg"] = "#20A520"
        else:
            self.verif_label["text"] = "Faux"
            self.verif_label["bg"] = "#A52020"

    def choix(self, *args) -> tuple:
        if not self.only_a_list.get():
            self.liste_cible = random.choice(list(voc().keys()))
        self.list_label["text"] = "liste étudiée : {}".format(self.liste_cible)
        return_value = random.choice(list(voc().get(self.liste_cible).items()))
        return return_value

    def quit_window(self, *args) -> None:
        self.window.quit()
        self.window.destroy()

    def change_word(self, *args) -> None:
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
        self.question, self.answer = (new, new[::-1])[self.french_first]
        self.first_entry["text"] = self.question
        self.verif_label["bg"] = "#777777"
        self.verif_label["text"] = ""
        self.solut_label["text"] = ""
        self.second_entry["width"] = len(self.answer) + 10

    def give_solution(self, *args) -> None:
        self.solut_label["text"] = "{}: {}".format(
                ("solution", "Lösung")[self.french_first],
                self.answer
            )

    def change_language(self, *args) -> None:
        self.french_first = not(self.french_first)
        self.language_button["text"] = "switch language to {}".format(
                        ("French", "German")[self.french_first]
                    )
        self.question, self.answer = swicth_variables(
                self.question,
                self.answer
            )
        self.first_entry["text"] = self.question
        self.solut_label["text"] = ""
        self.second_entry.delete(0, tk.END)


if __name__ == "__main__":
    MAIN = App()
