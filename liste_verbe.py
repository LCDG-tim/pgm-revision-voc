# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

"""dictionnaire de verbes forts et irréguliers faibles et class qui va avec
et la save dans un fichier externe
"""


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


def save(liste: dict = list_verbes()) -> None:
    """function to save the list in a outfile .csv
    """
    with open("liste_verbes.csv", "w") as file:
        file.write("liste;infinitif;présent;preterit;parfait;sens;\n")
        for liste in liste:
            for j in liste.get(liste):
                j: Verbe
                file.write(liste + ";" + j.get_save_str())


if __name__ == "__main__":
    LISTE = list_verbes()
    save(LISTE)
    del Verbe, list_verbes, LISTE, save
