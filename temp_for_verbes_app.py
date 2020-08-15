# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

"""temp for the main code
"""

import tkinter as tk
import random as rdm


from liste_verbe import Verbe
from liste_verbe import list_verbes


def plus_grand(nb_a: float or int, nb_b: float or int) -> float:
    """fontion retournant le plus grand nombre des 2 entrés

    \n----\n

    - pre:
        a, nb_b sont des nombres reels
    - post:
        None
    """
    assert isinstance(nb_a, (int, float)),\
        "le premier argument n'est pas un float"
    assert isinstance(nb_b, (float, int)), \
        "le deuxieme argument n'est pas un float"
    return (nb_b, nb_a)[nb_a > nb_b]


def plus_long(a: list) -> int:
    """return the lengh of the longer element of a list
    """
    return_val: int = len(a[0])
    for i in a[1:]:
        if len(i) > return_val:
            return_val: int = len(i)
    return return_val


class ListvEntry:

    """object for create a table of entry
    """

    def __init__(self, frame: tk.Frame, i: int, j: int = None):
        self.frame = frame
        self.i = i
        self.j = j
        self.main_bg = "#777777"
        self.entry_bg = "#f0f0f0"
        self.entry = tk.Entry(
                self.frame,
                width=((20, 29)[j == 4], 40)[j is None],
                disabledforeground="#000000",
                background=self.entry_bg,
                justify="center"
            )
        self.entry.grid(
                row=i,
                column=(j, 0)[j is None],
                sticky=tk.W
            )

    def get_frame(self) -> None:
        """return the frame
        """
        return self.frame

    def get_i(self) -> int:
        """return i
        """
        return self.i

    def get_j(self) -> int:
        """return j
        """
        return self.j

    def get_entry(self) -> int:
        """return entry
        """
        return self.entry


def give_geometry(window: tk.Tk) -> str:
    """return the geometry of the window given in the params
    """
    return window.winfo_geometry()


class App:

    """App for revise the german irregular verbe
    """

    def __init__(self):
        self.winv = tk.Tk()
        self.winv.geometry(
                "{}x{}+{}+{}".format(
                        self.winv.winfo_screenwidth()//2,
                        self.winv.winfo_screenheight()//2,
                        self.winv.winfo_screenwidth()//4,
                        self.winv.winfo_screenheight()//4
                    )
            )
        self.winv.minsize(
                self.winv.winfo_screenwidth()//4,
                self.winv.winfo_screenheight()//4
            )
        self.winv.maxsize(
                self.winv.winfo_screenwidth(),
                self.winv.winfo_screenheight()
            )

        self.number_lines = 10
        self.all_points = []
        self.main_bg = "#777777"
        self.entry_bg = "#f0f0f0"
        self.voca = list_verbes()
        self.winssr_running = False
        self.button_font = ("calibri", 12)

        self.winv.config(bg=self.main_bg)

        self.masterv_frame = tk.Frame(self.winv, bg=self.main_bg)

        self.list_vframe = tk.Frame(self.masterv_frame, bg=self.main_bg)

        self.list_ventry = [
                ListvEntry(self.list_vframe, i, j)
                for i in range(self.number_lines)
                for j in range(5)
            ]

        self.put_list()

        self.list_vframe.pack(expand=tk.YES)

        self.button_vframe = tk.Frame(
                self.masterv_frame,
                background=self.main_bg
            )

        self.verif_vbutton = tk.Button(
                self.button_vframe,
                text="Verification",
                font=self.button_font,
                command=self.verif
            )
        self.verif_vbutton.grid(row=0, column=0, sticky=tk.W, padx=4)

        self.correction_button = tk.Button(
                self.button_vframe,
                text="Correction",
                font=self.button_font,
                command=self.correction
            )
        self.correction_button.grid(row=0, column=1, sticky=tk.W, padx=4)

        self.chang_verb = tk.Button(
                self.button_vframe,
                text="Changer les verbes",
                font=self.button_font,
                command=self.put_list
            )
        self.chang_verb.grid(row=0, column=2, sticky=tk.W, padx=4)

        self.ssr_button = tk.Button(
                self.button_vframe,
                text="Recapitulatif des sessions",
                font=self.button_font,
                command=self.score_session_recap
            )
        self.ssr_button.grid(row=0, column=3, sticky=tk.W, padx=4)

        self.option_button = tk.Button(
                self.button_vframe,
                text="Option",
                font=self.button_font,
                command=self.options
            )
        self.option_button.grid(row=0, column=4, sticky=tk.W, padx=4)

        self.button_vframe.pack(expand=tk.YES, pady=20)

        self.masterv_frame.pack(expand=tk.YES)

        self.menu_bar = tk.Menu(self.winv)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.file_menu.add_command(
                label="Quitter",
                command=self.quit_winv
            )

        self.menu_bar.add_cascade(menu=self.file_menu, label="Fichier")

        self.command_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.command_menu.add_command(
                label="Changer les verbes",
                command=self.put_list
            )

        self.command_menu.add_command(
                label="Verifier",
                command=self.verif
            )

        self.command_menu.add_command(
                label="Score session recap",
                command=self.score_session_recap
            )

        self.menu_bar.add_cascade(menu=self.command_menu, label="Commandes")

        self.winv.config(menu=self.menu_bar)

        self.winv.mainloop()

    def clear_lines(self) -> None:
        """clear all the table
        """
        for i in self.list_ventry:
            i: ListvEntry
            i.entry.delete(0, tk.END)
            i.entry["background"] = self.entry_bg

    def put_list(self) -> None:
        """change the verbs asked
        """
        self.clear_lines()
        self.lines = []

        for i in range(1, self.number_lines + 1):
            lst = rdm.choice(list(self.voca.items()))
            word: Verbe = self.voca.get(lst[0])[
                    rdm.randint(0, len(lst[1]) - 1)
                ]

            self.lines.append(
                    word
                )
            j = 5 * i - 1
            self.list_ventry[j].entry["state"] = "normal"
            self.list_ventry[j].entry.delete(0, tk.END)
            self.list_ventry[j].entry.insert(0, word.get_sens())
            self.list_ventry[j].entry["state"] = "disabled"

    def verif(self) -> None:
        """verify the answer
        """
        points = 0
        for i in range(self.number_lines):
            error = 0
            for j in range(5 * i, 5 * i + 4):
                if self.list_ventry[j].entry.get() != \
                        self.lines[i].get_list()[j % 5]:
                    error += 1
                    self.list_ventry[j].entry["background"] = "#A52020"
            if error == 0:
                points += 1
            elif error == 1:
                points += .5

        recap_points_str = "{} / {} ou {} % de bonnes réponses".format(
                        points,
                        self.number_lines,
                        round(points * 100 / self.number_lines, 1)
                    )

        self.all_points.append(recap_points_str)

    def score_session_recap(self) -> None:
        """open a page which recap all score
        """
        self.winssr = tk.Tk()
        self.winssr.geometry("500x400+340+230")
        self.winssr.maxsize(
                self.winssr.winfo_screenwidth(),
                self.winssr.winfo_screenwidth()
            )
        self.winssr.minsize(500, 400)
        self.winssr.config(background=self.main_bg)

        self.master_ssrframe = tk.Frame(self.winssr)
        self.list_ssrentry = []
        if self.all_points:
            for i in range(len(self.all_points)):
                zone = ListvEntry(self.master_ssrframe, i)
                zone.entry.insert(0, self.all_points[i])
                self.list_ssrentry.append(
                        zone
                    )
        else:
            self.none_label = tk.Label(
                    self.master_ssrframe,
                    text="pas de session",
                    font=("Arial bold", 40),
                    background=self.main_bg
                )
            self.none_label.pack(expand=tk.YES)

        self.master_ssrframe.pack(expand=tk.YES)

        self.menu_ssrbar = tk.Menu(self.winssr)

        self.file_ssrmenu = tk.Menu(self.menu_ssrbar, tearoff=0)

        self.file_ssrmenu.add_command(
                label="Quitter",
                command=self.quit_winssr
            )

        self.menu_ssrbar.add_cascade(menu=self.file_ssrmenu, label="Fichier")

        self.winssr.config(menu=self.menu_ssrbar)

        self.winssr.mainloop()

    def options(self) -> None:
        """open a window with more options
        """
        self.wino = tk.Tk()
        self.wino.geometry("300x324+1033+219")
        self.wino.maxsize(
                    self.wino.winfo_screenwidth(),
                    self.wino.winfo_screenheight()
                )
        self.wino.minsize(300, 324)
        self.wino.config(background=self.main_bg)

        self.master_oframe = tk.Frame(
                self.wino,
                background=self.main_bg
            )

        self.quit_vbutton = tk.Button(
                self.master_oframe,
                text="Quitter l'application",
                font=self.button_font,
                command=self.quit_winv_by_option
            )
        self.quit_vbutton.pack(fill=tk.X, pady=4)

        self.b_button = tk.Button(
                self.master_oframe,
                text="{name}",
                font=self.button_font,
                # command=
            )
        self.b_button.pack(fill=tk.X, pady=4)

        self.c_button = tk.Button(
                self.master_oframe,
                text="{name}",
                font=self.button_font,
                # command=
            )
        self.c_button.pack(fill=tk.X, pady=4)

        self.d_button = tk.Button(
                self.master_oframe,
                text="{name}",
                font=self.button_font,
                # command=
            )
        self.d_button.pack(fill=tk.X, pady=4)

        self.master_oframe.pack(expand=tk.YES)

        self.menu_obar = tk.Menu(self.wino)

        self.file_omenu = tk.Menu(self.menu_obar, tearoff=0)

        self.file_omenu.add_command(
                label="Fermer",
                command=self.quit_wino
            )

        self.menu_obar.add_cascade(label="Fichier", menu=self.file_omenu)

        self.options_omenu = tk.Menu(self.menu_obar, tearoff=0)

        self.options_omenu.add_command(
                label="Quitter l'application",
                command=self.quit_winv_by_option
            )

        self.menu_obar.add_cascade(label="Options", menu=self.options_omenu)

        self.wino.config(menu=self.menu_obar)

        self.wino.mainloop()

    def quit_winv_by_option(self) -> None:
        self.quit_wino()
        self.quit_winv()

    def quit_wino(self) -> None:
        """quit wino
        """
        self.wino.quit()
        self.wino.destroy()

    def quit_winssr(self) -> None:
        """quit winssr
        """
        self.winssr.quit()
        self.winssr.destroy()

    def quit_winv(self) -> None:
        """quit wino
        """
        self.winv.quit()
        self.winv.destroy()

    def correction(self) -> None:
        """table correction
        """
        p_l_lines = plus_long(self.lines)
        width_winc = 8 * p_l_lines + 670
        height_winc = int(self.winv.winfo_screenheight() // 3)
        self.winc = tk.Tk()
        self.winc.geometry(
                "{}x{}+{}+{}".format(
                        width_winc,
                        height_winc,
                        (self.winc.winfo_screenwidth() - width_winc) // 2,
                        (self.winc.winfo_screenheight() - height_winc) // 2
                    )
            )
        self.winc.maxsize(
                self.winc.winfo_screenwidth(),
                self.winc.winfo_screenheight()
            )
        self.winc.minsize(width_winc - 50, height_winc)

        self.winc.config(background=self.main_bg)

        self.master_cframe = tk.Frame(self.winc, background="#333333")
        self.list_centry = []
        for i in range(self.number_lines):
            for j in range(5):
                zone = tk.Label(
                        self.master_cframe,
                        text=self.lines[i].get_list()[j],
                        background="#A0A0A0",
                        width=(20, plus_grand(29, p_l_lines))[j == 4]
                    )
                zone.grid(row=i, column=j, sticky=tk.W, padx=1, pady=1)

        self.master_cframe.pack(expand=tk.YES)

        self.menu_cbar = tk.Menu(self.winc)

        self.file_cmenu = tk.Menu(self.menu_cbar, tearoff=0)

        self.file_cmenu.add_command(
                label="Fermer",
                command=self.quit_winc
            )

        self.menu_cbar.add_cascade(label="Fichier", menu=self.file_cmenu)

        self.winc.config(menu=self.menu_cbar)

        self.winc.mainloop()

    def quit_winc(self) -> None:
        self.winc.quit()
        self.winc.destroy()


if __name__ == "__main__":
    MAIN = App()
