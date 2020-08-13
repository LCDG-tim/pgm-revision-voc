# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


import tkinter as tk
import random as rdm


class Verbe:

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
        return self.infinitif

    def get_present(self) -> str:
        return self.present

    def get_preterit(self) -> str:
        return self.preterit

    def get_parfait(self) -> str:
        return self.parfait

    def get_sens(self) -> str:
        return self.sens

    def get_list(self) -> list:
        return self.list

    def get_save_str(self) -> list:
        return self.save_str


class Listv_entry:

    def __init__(self, frame: tk.Frame, i: int, j: int):
        self.frame = frame
        self.i = i
        self.j = j
        self.main_bg = "#777777"
        self.entry = tk.Entry(
                self.frame,
                width=(20, 29)[j == 4],
                disabledforeground="#000000",
                justify="center"
            )
        self.entry.grid(
                row=i,
                column=j,
                sticky=tk.W
            )

    def get_frame(self) -> None:
        return self.frame

    def get_i(self) -> int:
        return self.i

    def get_j(self) -> int:
        return self.j

    def get_entry(self) -> int:
        return self.entry


def list_verbes() -> dict:
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
    voca = list_verbes()
    with open("liste_verbes.csv", "w") as file:
        file.write("liste;infinitif;présent;preterit;parfait;sens;\n")
        for liste in voca.keys():
            for j in voca[liste]:
                j: Verbe
                file.write(liste + ";" + j.get_save_str())


class App:

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
        self.number_session = 0
        self.main_bg = "#777777"
        self.voca = list_verbes()

        self.winv.config(bg=self.main_bg)

        self.masterv_frame = tk.Frame(self.winv, bg=self.main_bg)

        self.list_vframe = tk.Frame(self.masterv_frame, bg=self.main_bg)

        self.list_ventry = [
                Listv_entry(self.list_vframe, i, j)
                for i in range(self.number_lines)
                for j in range(5)
            ]
        self.put_list()

        self.list_vframe.pack()

        self.masterv_frame.pack(expand=tk.YES)

        self.menu_bar = tk.Menu(self.winv)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.file_menu.add_command(
                label="recap session score",
                command=self.score_session_recap
            )

        self.file_menu.add_command(
                label="quitter",
                command=self.quit_winv
            )

        self.menu_bar.add_cascade(menu=self.file_menu, label="Fichier")

        self.command_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.command_menu.add_command(
                label="changer les verbes",
                command=self.put_list
            )

        self.command_menu.add_command(
                label="verifier",
                command=self.verif
            )

        self.command_menu.add_command(
                label="score session recap",
                command=self.score_session_recap
            )

        self.menu_bar.add_cascade(menu=self.command_menu, label="Commandes")

        self.winv.config(menu=self.menu_bar)

        self.winv.mainloop()

    def clear_lines(self) -> None:
        for i in self.list_ventry:
            i.entry.delete(0, tk.END)

    def put_list(self) -> None:
        self.clear_lines()
        self.number_session += 1
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

        print(recap_points_str)

        self.all_points.append(recap_points_str)

    def score_session_recap(self) -> None:
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
        for i in range(self.number_session):
            zone = Listv_entry(self.master_ssrframe, i, 0)
            if i < len(self.all_points):
                zone.entry.insert(0, self.all_points[i])
            self.list_ssrentry.append(
                    zone
                )
        self.master_ssrframe.pack(expand=tk.YES)

    def quit_winv(self) -> None:
        self.winv.quit()
        self.winv.destroy()


if __name__ == "__main__":
    App()
