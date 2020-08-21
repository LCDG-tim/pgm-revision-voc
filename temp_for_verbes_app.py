# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

"""temp for the main code
"""

import re

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
    return_val: int = len(a[0].get_sens())
    for i in a[1:]:
        i: Verbe
        if len(i.get_sens()) > return_val:
            return_val: int = len(i.get_sens())
    return return_val


def affiche(args: "Any") -> None:
    text = "\n_______________ {} _______________\n".format(args)
    print(text)


class ListvEntry:

    """object for create a table of entry
    """

    def __init__(self, frame: tk.Frame, i: int, j: int = None):
        self.frame = frame
        self.i = i
        self.j = j
        self.main_bg = "#777777"
        self.entry_bg = "#a0a0a0"
        self.dis_bg_color = "#888888"
        self.entry = tk.Entry(
                self.frame,
                width=((20, 29)[j == 4], 40)[j is None],
                disabledforeground="#000000",
                disabledbackground=self.dis_bg_color,
                background=self.entry_bg,
                relief="flat",
                justify="center"
            )
        self.entry.grid(
                row=i,
                column=(j, 0)[j is None],
                sticky=tk.W,
                padx=1,
                pady=1
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

    def set_bg(self, bg: str) -> None:
        self.entry["background"] = bg

    def set_state(self, state: str) -> None:
        self.entry["state"] = state

    def set_dis_bg(self, new_bg: str) -> None:
        if re.findall(r"^#[a-fA-F0-9]{6}$", new_bg):
            self.entry["disabledbackground"] = new_bg

    def clear_self_entry(self) -> None:
        self.set_state("normal")
        self.set_dis_bg(self.dis_bg_color)
        self.entry.delete(0, tk.END)
        self.set_bg(self.entry_bg)


def give_geometry(window: tk.Tk) -> str:
    """return the geometry of the window given in the params
    """
    return window.winfo_geometry()


class App:

    """App for revise the german irregular verbe
    """

    def __init__(self):
        self.winv = tk.Tk()

        self.SCREEN_WIDTH = self.winv.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winv.winfo_screenheight()

        width = int(self.SCREEN_WIDTH // 1.8)
        height = int(self.SCREEN_HEIGHT // 2.25)

        self.winv.geometry(
                "{}x{}+{}+{}".format(
                        width,
                        height,
                        self.SCREEN_WIDTH // 2 - width // 2,
                        self.SCREEN_HEIGHT // 2 - height // 2
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
        self.entry_bg = "#a0a0a0"
        self.title_bgcolor = "#888888"
        self.voca = list_verbes()
        self.winssr_running = False
        self.button_font = ("calibri", 12)
        self.list_asked = None
        self.mod_current = None
        self.reset_after_session = True

        self.mod_cml_1 = "Toute la colonne 1 complétée"
        self.mod_cml_2 = "Toute la colonne 2 complétée"
        self.mod_cml_3 = "Toute la colonne 3 complétée"
        self.mod_cml_4 = "Toute la colonne 4 complétée"
        self.mod_cml_5 = "Toute la colonne 5 complétée"
        self.mod_cml_6 = [0, 1, 2, 3, 4]
        self.mod_cml_7 = [1, 2, 3, 4, 0]
        self.mod_cml_8 = [2, 3, 4, 0, 1]
        self.mod_cml_9 = [3, 4, 0, 1, 2]
        self.mod_cml_10 = [4, 0, 1, 2, 3]
        self.mod_cml_11 = "Aléatoire"
        self.list_asked = 4
        self.mod_current = self.mod_cml_5

        self.winv.config(bg=self.main_bg)

        self.masterv_frame = tk.Frame(self.winv, bg=self.main_bg)

        self.title_frame = tk.Frame(self.masterv_frame, bg="#333333")

        self.column_name_list = [
                "infinitif",
                "present",
                "prétérit",
                "parfait",
                "sens"
            ]

        for i in range(5):
            entry = tk.Entry(
                    self.title_frame,
                    justify="center",
                    background=self.entry_bg,
                    disabledforeground="#000000",
                    disabledbackground=self.title_bgcolor,
                    relief="flat",
                    width=(20, 29)[i == 4]
                )
            entry.grid(row=0, column=i, sticky=tk.W, padx=1, pady=1)

            entry.insert(0, self.column_name_list[i])

            entry["state"] = "disabled"

        self.title_frame.pack(expand=tk.YES)

        self.list_vframe = tk.Frame(self.masterv_frame, bg="#333333")

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
        self.command_menu.add_command(
                label="Options",
                command=self.options
            )

        self.option_vmenu = tk.Menu(self.menu_bar, tearoff=0)

        self.option_vmenu.add_command(
                label="Pas de reset",
                command=self.reset_as
            )

        self.option_vmenu.add_command(
                label="Choix du modèle",
                command=self.choice_model_l
            )

        self.menu_bar.add_cascade(menu=self.command_menu, label="Commandes")

        self.menu_bar.add_cascade(
                label="Options",
                menu=self.option_vmenu
            )

        self.winv.config(menu=self.menu_bar)

        self.winv.mainloop()

    def clear_lines(self) -> None:
        """clear all the table
        """
        for j, i in enumerate(self.list_ventry, start=1):
            i: ListvEntry
            i.clear_self_entry()

    def put_list(self) -> None:
        """change the verbs asked
        """

        print("")

        self.clear_lines()
        self.lines = []
        k = 0

        for i in range(self.number_lines):
            lst1, lst2 = rdm.choice(list(self.voca.items()))
            indix: Verbe = rdm.randint(0, len(lst2) - 1)
            word: Verbe = lst2[indix]

            self.lines.append(
                    word
                )

            del self.voca[lst1][indix]
            if not self.voca[lst1]:
                del self.voca[lst1]

            if isinstance(self.list_asked, int):
                j = 5 * i + self.list_asked
                self.list_ventry[j].entry["state"] = "normal"
                self.list_ventry[j].entry.delete(0, tk.END)
                self.list_ventry[j].entry.insert(
                        0,
                        word.get_list(self.list_asked)
                    )
                self.list_ventry[j].entry["state"] = "disabled"

            elif isinstance(self.list_asked, list):
                k %= 5
                colonne = self.list_asked[k]
                j = 5 * i + colonne
                self.list_ventry[j].entry["state"] = "normal"
                self.list_ventry[j].entry.delete(0, tk.END)
                self.list_ventry[j].entry.insert(
                        0,
                        word.get_list(colonne)
                    )
                self.list_ventry[j].entry["state"] = "disabled"
                k += 1

            else:
                colonne = rdm.randint(0, 4)
                j = 5 * i + colonne
                self.list_ventry[j].entry["state"] = "normal"
                self.list_ventry[j].entry.delete(0, tk.END)
                self.list_ventry[j].entry.insert(
                        0,
                        word.get_list(colonne)
                    )
                self.list_ventry[j].entry["state"] = "disabled"

        if self.reset_after_session:
            self.voca = list_verbes()

    def clear_bg(self) -> None:
        for j, i in enumerate(self.list_ventry, start=1):
            i: ListvEntry
            i.set_bg(self.entry_bg)

    def verif(self) -> None:
        """verify the answer
        """
        points = 0
        self.clear_bg()
        for i in range(self.number_lines):
            error = 0
            for j in range(5 * i, 5 * (i + 1)):
                self.list_ventry[j]: ListvEntry
                if self.list_ventry[j].entry.get() != \
                        self.lines[i].get_list(j % 5):
                    error += 1
                    self.list_ventry[j].set_bg("#A56060")
                else:
                    self.list_ventry[j].set_dis_bg(self.entry_bg)
                    self.list_ventry[j].set_state("disabled")

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

        self.reset_as_button = tk.Button(
                self.master_oframe,
                text="Ne pas réintialiser à chaque session",
                font=self.button_font,
                command=self.reset_as
            )
        self.reset_as_button.pack(fill=tk.X, pady=4)

        self.choice_mod_button = tk.Button(
                self.master_oframe,
                text="Choisir le modéle",
                font=self.button_font,
                command=self.choice_model_l
            )
        self.choice_mod_button.pack(fill=tk.X, pady=4)

        self.d_button = tk.Button(
                self.master_oframe,
                text="{name}",
                font=self.button_font,
                # command=self.a
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

    def reset_as(self) -> None:
        if self.reset_after_session:
            self.reset_as_button["text"] = "Ne pas réintialiser à chaque" \
                "session"
        else:
            self.reset_as_button["text"] = "Réinitialiser à chaque session"
        self.reset_after_session = not self.reset_after_session

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
        width_winc = 8 * p_l_lines + 700
        height_winc = int(self.winv.winfo_screenheight() // 3) + 20
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
        for i in range(self.number_lines + 1):
            for j in range(5):
                zone = tk.Label(
                        self.master_cframe,
                        text=(
                                self.lines[i - 1].get_list(j),
                                self.column_name_list[j]
                            )[i == 0],
                        background=(self.entry_bg, self.title_bgcolor)[i == 0],
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

    def choice_model_l(self) -> None:
        self.wincml = tk.Tk()
        self.wincml.geometry("300x500+20+100")
        self.wincml.minsize(300, 500)
        self.wincml.maxsize(
                self.wincml.winfo_screenwidth(),
                self.wincml.winfo_screenheight()
            )
        self.wincml.config(background=self.main_bg)

        self.master_cmlframe = tk.Frame(self.wincml, background=self.main_bg)

        self.list_asked_lab = tk.Label(
                self.master_cmlframe,
                background=self.main_bg
            )
        self.list_asked_lab.pack(expand=tk.YES)

        self.refresh_lab_cml()

        self.button_cmlframe1 = tk.Frame(self.master_cmlframe, bg=self.main_bg)

        all_colonne_1 = tk.Button(
                self.button_cmlframe1,
                text=self.mod_cml_1,
                command=self.set_list_sel_1
            )
        all_colonne_1.grid(row=1, column=0, sticky=tk.W, pady=3)

        all_colonne_2 = tk.Button(
                self.button_cmlframe1,
                text=self.mod_cml_2,
                command=self.set_list_sel_2
            )
        all_colonne_2.grid(row=2, column=0, sticky=tk.W, pady=3)

        all_colonne_3 = tk.Button(
                self.button_cmlframe1,
                command=self.set_list_sel_3,
                text=self.mod_cml_3
            )
        all_colonne_3.grid(row=3, column=0, sticky=tk.W, pady=3)

        all_colonne_4 = tk.Button(
                self.button_cmlframe1,
                command=self.set_list_sel_4,
                text=self.mod_cml_4
            )
        all_colonne_4.grid(row=4, column=0, sticky=tk.W, pady=3)

        all_colonne_5 = tk.Button(
                self.button_cmlframe1,
                command=self.set_list_sel_5,
                text=self.mod_cml_5
            )
        all_colonne_5.grid(row=5, column=0, sticky=tk.W, pady=3)

        self.button_cmlframe2 = tk.Frame(self.master_cmlframe, bg=self.main_bg)

        switch_1 = tk.Button(
                self.button_cmlframe2,
                command=self.set_list_sel_6,
                text=self.mod_cml_6
            )
        switch_1.grid(row=6, column=0, sticky=tk.W, pady=3)

        switch_2 = tk.Button(
                self.button_cmlframe2,
                command=self.set_list_sel_7,
                text=self.mod_cml_7
            )
        switch_2.grid(row=7, column=0, sticky=tk.W, pady=3)

        switch_3 = tk.Button(
                self.button_cmlframe2,
                command=self.set_list_sel_8,
                text=self.mod_cml_8
            )
        switch_3.grid(row=8, column=0, sticky=tk.W, pady=3)

        switch_4 = tk.Button(
                self.button_cmlframe2,
                command=self.set_list_sel_9,
                text=self.mod_cml_9
            )
        switch_4.grid(row=9, column=0, sticky=tk.W, pady=3)

        switch_5 = tk.Button(
                self.button_cmlframe2,
                command=self.set_list_sel_10,
                text=self.mod_cml_10
            )
        switch_5.grid(row=10, column=0, sticky=tk.W, pady=3)

        self.button_cmlframe1.pack(expand=tk.YES)

        self.button_cmlframe2.pack(expand=tk.YES)

        self.master_cmlframe.pack(expand=tk.YES)

        self.menu_cmlbar = tk.Menu(self.wincml)

        self.file_cmlmenu = tk.Menu(self.wincml, tearoff=0)

        self.file_cmlmenu.add_command(
                label="Fermer",
                command=self.quit_wincml
            )

        self.options_cmlmenu = tk.Menu(self.menu_cmlbar, tearoff=0)

        all_colonnes = tk.Menu(
                self.options_cmlmenu,
                tearoff=0
            )

        all_colonnes.add_command(
                label="commence en 1",
                command=self.set_list_sel_6
            )

        all_colonnes.add_command(
                label="commence en 2",
                command=self.set_list_sel_7
            )

        all_colonnes.add_command(
                label="commence en 3",
                command=self.set_list_sel_8
            )

        all_colonnes.add_command(
                label="commence en 4",
                command=self.set_list_sel_9
            )

        all_colonnes.add_command(
                label="commence en 5",
                command=self.set_list_sel_10
            )

        self.options_cmlmenu.add_cascade(
                menu=all_colonnes,
                label="Une colonne"
            )

        switchs = tk.Menu(
                self.options_cmlmenu,
                tearoff=0
            )

        self.options_cmlmenu.add_cascade(
                menu=switchs,
                label="Alternance"
            )

        self.options_cmlmenu.add_command(
                label="Aléatoire",
                command=self.set_list_sel_11
            )

        self.menu_cmlbar.add_cascade(label="Fichier", menu=self.file_cmlmenu)

        self.menu_cmlbar.add_cascade(label="Option", menu=self.options_cmlmenu)

        self.wincml.config(menu=self.menu_cmlbar)

        self.wincml.mainloop()

    def refresh_lab_cml(self) -> None:
        self.list_asked_lab["text"] = "modèle courant : {}" \
            .format(self.mod_current)

    def set_list_sel_1(self) -> None:
        self.list_asked = 0
        self.mod_current = self.mod_cml_1
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_2(self) -> None:
        self.list_asked = 1
        self.mod_current = self.mod_cml_2
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_3(self) -> None:
        self.list_asked = 2
        self.mod_current = self.mod_cml_3
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_4(self) -> None:
        self.list_asked = 3
        self.mod_current = self.mod_cml_4
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_5(self) -> None:
        self.list_asked = 4
        self.mod_current = self.mod_cml_5
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_6(self) -> None:
        self.list_asked = self.mod_cml_6
        self.mod_current = self.mod_cml_6
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_7(self) -> None:
        self.list_asked = self.mod_cml_7
        self.mod_current = self.mod_cml_7
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_8(self) -> None:
        self.list_asked = self.mod_cml_8
        self.mod_current = self.mod_cml_8
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_9(self) -> None:
        self.list_asked = self.mod_cml_9
        self.mod_current = self.mod_cml_9
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_10(self) -> None:
        self.list_asked = self.mod_cml_10
        self.mod_current = self.mod_cml_10
        self.refresh_lab_cml()
        self.put_list()

    def set_list_sel_11(self) -> None:
        self.list_asked = self.mod_cml_11
        self.mod_current = self.mod_cml_11
        self.refresh_lab_cml()
        self.put_list()

    def quit_winc(self) -> None:
        self.winc.quit()
        self.winc.destroy()

    def quit_wincml(self) -> None:
        self.wincml.quit()
        self.wincml.destroy()


if __name__ == "__main__":
    MAIN = App()
