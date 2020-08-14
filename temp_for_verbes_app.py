# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

"""temp for the main code
"""

import tkinter as tk
import random as rdm


class Verbe:

    """object representing a verbe of german strong verb
    """

    def __init__(
            self,
            infinitif: str,
            present: str,
            preterit: str,
            parfait: str,
            sens: str
            ) -> None:
        self.infinitif = infinitif
        self.present = present
        self.preterit = preterit
        self.parfait = parfait
        self.sens = sens
        self.list = [infinitif, present, preterit, parfait, sens]
        self.save_str = ";".join(self.list) + "\n"

    def get_infinitif(self) -> str:
        """
        return verbale base of the verb
        """
        return self.infinitif

    def get_present(self) -> str:
        """
        return german present of the verb
        """
        return self.present

    def get_preterit(self) -> str:
        """return german preterit of the verb
        """
        return self.preterit

    def get_parfait(self) -> str:
        """return german perfect of the verb
        """
        return self.parfait

    def get_sens(self) -> str:
        """return french translation
        """
        return self.sens

    def get_list(self) -> list:
        """return the list
        """
        return self.list

    def get_save_str(self) -> list:
        """return the str for saving
        """
        return self.save_str


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


def plus_long(a: list) -> str:

    def fusion(lst1: list, lst2: list) -> list:
        """fusion de deux tableaux lst1 et lst2"""
        i1, i2, n1, n2, t = 0, 0, len(lst1), len(lst2), []
        while(i1 < n1 and i2 < n2):
            if lst1[i1] < lst2[i2]:
                t.append(lst1[i1])
                i1 += 1
            else:
                t.append(lst2[i2])
                i2 += 1
        if i1 == n1:
            t.extend(lst2[i2:])
        else:
            t.extend(lst1[i1:])
        return t

    def tri_fusion(lst: list) -> list:
        """fonction du tri par fusion"""
        n = len(lst)
        if n < 2:
            return_val = lst
        else:
            m = n // 2
            return_val = fusion(tri_fusion(lst[:m]), tri_fusion(lst[m:]))
        return return_val

    new = [len(j) for i in a for j in i.get_list()]
    return tri_fusion(new)[-1]


class ListvEntry:

    """object for create a table of entry
    """

    def __init__(self, frame: tk.Frame, i: int, j: int = None):
        self.frame = frame
        self.i = i
        self.j = j
        self.main_bg = "#777777"
        self.entry = tk.Entry(
                self.frame,
                width=((20, 29)[j == 4], 35)[j is None],
                disabledforeground="#000000",
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
    """return the geometrie of the window given in the params
    """
    return window.winfo_geometry()


def list_verbes() -> dict:
    """return the list of strong and weak irregular german verb
    """
    vocabulaire = {
            "ä, u, a": [
                    Verbe(
                            "ein/laden",
                            "lädt ... ein",
                            "lud ... ein",
                            "hat ... eingeladen",
                            "inviter"
                        ),
                    Verbe(
                            "fahren",
                            "fährt",
                            "fuhr",
                            "ist ... gefahren",
                            "aller (avec un moyen de locomotion)"
                        ),
                    Verbe(
                            "tragen",
                            "trägt",
                            "trug",
                            "hat ... getragen",
                            "porter"
                        ),
                    Verbe(
                            "schlagen",
                            "schlägt",
                            "schlug",
                            "hat ... geschlagen",
                            "frapper / battre"
                        ),
                    Verbe(
                            "vor/schlagen",
                            "schlägt ... vor",
                            "schlug ... vor",
                            "hat ... vorgeschlagen",
                            "proposer"
                        ),
                    Verbe(
                            "wachsen",
                            "wächst",
                            "wuchs",
                            "hat ... gewachsen",
                            "grandir"
                        ),
                    Verbe(
                            "waschen",
                            "wäscht",
                            "wusch",
                            "hat ... gewaschen",
                            "laver"
                        )
                ],
            "ä, i(e), a": [
                    Verbe(
                            "an/fangen",
                            "fängt ... an",
                            "fing ... an",
                            "hat ... an/gefangen",
                            "commencer"
                        ),
                    Verbe(
                            "fangen",
                            "fängt",
                            "fing",
                            "hat ... gefangen",
                            "attraper"
                        ),
                    Verbe(
                            "fallen",
                            "fält",
                            "fiel",
                            "ist ... gefallen",
                            "tomber"
                        ),
                    Verbe(
                            "halten",
                            "hält",
                            "hielt",
                            "hat ... gehalten",
                            "arrêter / tenir"
                        ),
                    Verbe(
                            "lassen",
                            "lässt",
                            "ließ",
                            "hat ... gelassen",
                            "laisser"
                        ),
                    Verbe(
                            "schlafen",
                            "schläft",
                            "schlief",
                            "hat ... geschlafen",
                            "dormir"
                        )
                ],
            "ä, ie, au": [
                    Verbe(
                            "laufen",
                            "läuft",
                            "lief",
                            "ist ... gelaufen",
                            "courir"
                        )
                ],
            "_, a, a": [
                    Verbe(
                            "auf/stehen",
                            "steht ... auf",
                            "stand ... auf",
                            "ist ... aufgestanden",
                            "se lever"
                        ),
                    Verbe(
                            "stehen",
                            "steht",
                            "stand",
                            "hat / ist ... gestanden",
                            "se tenir debout / se trouver"
                        ),
                    Verbe(
                            "tun",
                            "tut",
                            "tat",
                            "hat ... getan",
                            "faire"
                        )
                ],
            "ie, a, e": [
                    Verbe(
                            "lesen",
                            "liest",
                            "las",
                            "hat ... gelesen",
                            "lire"
                        ),
                    Verbe(
                            "sehen",
                            "sieht",
                            "sah",
                            "hat ... gesehen",
                            "voir"
                        ),
                    Verbe(
                            "fern/sehen",
                            "sieht ... fern",
                            "sah ... fern",
                            "hat ... ferngesehen",
                            "regarder la television"
                        )
                ],
            "i, a, e": [
                    Verbe(
                            "essen",
                            "isst",
                            "aß",
                            "hat ... gegessen",
                            "manger"
                        ),
                    Verbe(
                            "fressen",
                            "frisst",
                            "fraß",
                            "hat ... gefressen",
                            "manger (pour les animaux)"
                        ),
                    Verbe(
                            "geben",
                            "gibt",
                            "gab",
                            "hat ... gegeben",
                            "donner"
                        ),
                    Verbe(
                            "vergessen",
                            "vergisst",
                            "vergaß",
                            "hat ... vergessen",
                            "oublier"
                        ),
                ],
            "i(e), a, o": [
                    Verbe(
                            "brechen",
                            "bricht",
                            "brach",
                            "hat ... gebrochen",
                            "casser"
                        ),
                    Verbe(
                            "empfehlen",
                            "empfiehlt",
                            "empfahl",
                            "hat ... empfohlen",
                            "recommander"
                        ),
                    Verbe(
                            "helfen",
                            "hilft",
                            "half",
                            "hat ... geholfen",
                            "aider"
                        ),
                    Verbe(
                            "nehmen",
                            "nimmt",
                            "nahm",
                            "hat ... genommen",
                            "prendre"
                        ),
                    Verbe(
                            "sprechen",
                            "spricht",
                            "sprach",
                            "hat ... gesprochen",
                            "parler"
                        ),
                    Verbe(
                            "sterben",
                            "stirbt",
                            "starb",
                            "ist gestorben",
                            "mourir"
                        ),
                    Verbe(
                            "treffen",
                            "trifft",
                            "traf",
                            "hat ... getroffen",
                            "rencontrer"
                        ),
                    Verbe(
                            "werfen",
                            "wirft",
                            "warf",
                            "hat ... geworfen",
                            "lancer/jeter"
                        )
                ],
            "_, i, a": [
                    Verbe(
                            "gehen",
                            "geht",
                            "ging",
                            "ist ... gegangen",
                            "aller (à pied)"
                        )
                ],
            "i, u, o": [
                    Verbe(
                            "werden",
                            "wird",
                            "wurd",
                            "ist ... geworden",
                            "devenir"
                        )
                ],
            "_, i, i": [
                    Verbe(
                            "reiten",
                            "reitet",
                            "ritt",
                            "ist ... geritten",
                            "faire de l'équitation"
                        ),
                    Verbe(
                            "sich streiten",
                            "streitet sich",
                            "stritt sich",
                            "hat sich ... gestritten",
                            "se disputer"
                        )
                ],
            "_, ie, ie": [
                    Verbe(
                            "bleiben",
                            "bleibt",
                            "blieb",
                            "ist ... geblieden",
                            "rester"
                        ),
                    Verbe(
                            "entscheiden",
                            "entscheidet",
                            "entschied",
                            "hat ... entschieden",
                            "décider"
                        ),
                    Verbe(
                            "scheinen",
                            "scheint",
                            "schien",
                            "hat ... geschienen",
                            "briller, sembler"
                        ),
                    Verbe(
                            "schreiben",
                            "schreibt",
                            "schrieb",
                            "hat ... geschrieben",
                            "écrire"
                        ),
                    Verbe(
                            "schreien",
                            "schreit",
                            "schrie",
                            "hat ... geschrien",
                            "crier"
                        ),
                    Verbe(
                            "treiben",
                            "treibt",
                            "trieb",
                            "hat ... getrieben",
                            "pratiquer un sport"
                        )
                ],
            "_, ie, ei": [
                    Verbe(
                            "heißen",
                            "heißt",
                            "hieß",
                            "hat ... geheißen",
                            "s'appeler"
                        )
                ],
            "_, a, e": [
                    Verbe(
                            "bitten",
                            "bittet",
                            "bat",
                            "hat ... gebeten",
                            "prier (qqn de qqch)"
                        ),
                    Verbe(
                            "liegen",
                            "liegt",
                            "lag",
                            "hat / ist ... gelegen",
                            "être allongé"
                        ),
                    Verbe(
                            "sitzen",
                            "sitzt",
                            "saß",
                            "hat / ist ... gesetzen",
                            "être assis"
                        )
                ],
            "_, a, o": [
                    Verbe(
                            "beginnen",
                            "beginnt",
                            "begann",
                            "hat ... begonnen",
                            "commencer / débuter"
                        ),
                    Verbe(
                            "gewinnen",
                            "gewinnt",
                            "gewann",
                            "hat ... gewonnen",
                            "gagner"
                        ),
                    Verbe(
                            "schwimmen",
                            "schwimmt",
                            "schwamm",
                            "ist ... geschwommen",
                            "nager"
                        ),
                    Verbe(
                            "kommen",
                            "kommt",
                            "kam",
                            "ist ... gekommen",
                            "venir"
                        )
                ],
            "_, a, u": [
                    Verbe(
                            "finden",
                            "findet",
                            "fand",
                            "hat ... gefunden",
                            "trouver"
                        ),
                    Verbe(
                            "singen",
                            "singt",
                            "sang",
                            "hat ... gesungen",
                            "chanter"
                        ),
                    Verbe(
                            "springen",
                            "springt",
                            "sprang",
                            "ist ... gesprungen",
                            "sauter"
                        ),
                    Verbe(
                            "trinken",
                            "trinkt",
                            "trank",
                            "hat ... getrunkt",
                            "boire"
                        ),
                    Verbe(
                            "verschwinden",
                            "verschwindet",
                            "verschwand",
                            "hat ... verschwunden",
                            "disparaître"
                        ),
                ],
            "_, o, o": [
                    Verbe(
                            "an/bieten",
                            "bietet ... an",
                            "bot ... an",
                            "hat ... angeboten",
                            "offrir"
                        ),
                    Verbe(
                            "fliegen",
                            "fliegt",
                            "flog",
                            "ist ... geflogen",
                            "voler (avion, oiseau)"
                        ),
                    Verbe(
                            "frieren",
                            "friert",
                            "fror",
                            "hat ... gefroren",
                            "geler"
                        ),
                    Verbe(
                            "genießen",
                            "genießt",
                            "genoss",
                            "hat ... genossen",
                            "profiter de (savourer)"
                        ),
                    Verbe(
                            "schießen",
                            "schießt",
                            "schoss",
                            "hat ... geschossen",
                            "tirer, lancer (sur)"
                        ),
                    Verbe(
                            "schließen",
                            "schließt",
                            "schloss",
                            "hat ... geschlossen",
                            "fermer"
                        ),
                    Verbe(
                            "verlieren",
                            "verliert",
                            "verlor",
                            "hat ... verloren",
                            "perdre"
                        ),
                    Verbe(
                            "wiegen",
                            "wiegt",
                            "wog",
                            "hat ... gewogen",
                            "peser"
                        ),
                    Verbe(
                            "ziehen",
                            "zieht",
                            "zoh",
                            "hat ... gezohen",
                            "tirer (porte)"
                        )
                ],
            "_, ie, u": [
                    Verbe(
                            "an/rufen",
                            "ruft ... an",
                            "rief ... an",
                            "hat ... angerufen",
                            "appeler (au telephone)"
                        )
                ],
            "liste verbes faibles irréguliers": [
                    Verbe(
                            "brennen",
                            "brennt",
                            "brannte",
                            "hat ... gebrannt",
                            "brûler"
                        ),
                    Verbe(
                            "bringen",
                            "bringt",
                            "brachte",
                            "hat ... gebracht",
                            "apporter"
                        ),
                    Verbe(
                            "denken",
                            "denkt",
                            "dachte",
                            "hat ... gedacht",
                            "penser"
                        ),
                    Verbe(
                            "kennen",
                            "kennt",
                            "kannte",
                            "hat ... gekannt",
                            "connaître"
                        ),
                    Verbe(
                            "nennen",
                            "nennt",
                            "nannte",
                            "hat ... genannt",
                            "nommer"
                        ),
                    Verbe(
                            "rennen",
                            "rennt",
                            "rannte",
                            "ist ... gerannt",
                            "courrir"
                        )
                ]
        }
    return vocabulaire


def save() -> None:
    """function to save the list in a outfile .csv
    """
    voca = list_verbes()
    with open("liste_verbes.csv", "w") as file:
        file.write("liste;infinitif;présent;preterit;parfait;sens;\n")
        for liste in voca:
            for j in voca.get(liste):
                j: Verbe
                file.write(liste + ";" + j.get_save_str())


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

        self.ssr_button = tk.Button(
                self.button_vframe,
                text="Recapitulatif des sessions",
                font=self.button_font,
                command=self.score_session_recap
            )
        self.ssr_button.grid(row=0, column=2, sticky=tk.W, padx=4)

        self.option_button = tk.Button(
                self.button_vframe,
                text="Option",
                font=self.button_font,
                command=self.options
            )
        self.option_button.grid(row=0, column=3, sticky=tk.W, padx=4)

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
            i.entry.delete(0, tk.END)

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

        self.master_oframe = tk.Frame(self.wino)

        self.quit_vbutton = tk.Button(
                self.master_oframe,
                text="Quitter",
                font=self.button_font,
                command=self.quit_winv
            )
        self.quit_vbutton.pack(fill=tk.X)

        self.b_button = tk.Button(
                self.master_oframe,
                text="{name}",
                font=self.button_font,
                # command=
            )
        self.b_button.pack(fill=tk.X)

        self.c_button = tk.Button(
                self.master_oframe,
                text="{name}",
                font=self.button_font,
                # command=
            )
        self.c_button.pack(fill=tk.X)

        self.d_button = tk.Button(
                self.master_oframe,
                text="{name}",
                font=self.button_font,
                # command=
            )
        self.d_button.pack(fill=tk.X)

        self.master_oframe.pack(expand=tk.YES)

        self.menu_obar = tk.Menu(self.wino)

        self.file_omenu = tk.Menu(self.menu_obar, tearoff=0)

        self.file_omenu.add_command(
                label="Quitter",
                command=self.quit_wino
            )

        self.menu_obar.add_cascade(label="Fichier", menu=self.file_omenu)

        self.wino.config(menu=self.menu_obar)

        self.wino.mainloop()

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
        """
                "{}x{}+{}+{}".format(
                        self.winc.winfo_screenwidth()//3,
                        self.winc.winfo_screenheight()//3,
                        self.winc.winfo_screenwidth()//6,
                        self.winc.winfo_screenheight()//6
                    )
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
                label="Quitter",
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
