# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

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

    def get_infinitif(self) -> str:
        return self.infinitif

    def get_present(self) -> str:
        return self.present

    def get_preterit(self) -> str:
        return self.preterit

    def get_parfait(self) -> str:
        return self.parfait


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
                            "ist gefahren",
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
                            "frapper battre"
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
                            "hat ... gewaschen"
                            "laver"
                        )
                ],
            "ä, i(e), a": [
                    Verbe(
                            "an/fangen",
                            "fängt ... an",
                            "fing ... an",
                            "hat an/gefangen",
                            "commencer"
                        ),
                    Verbe(
                            "fangen",
                            "fängt",
                            "fing",
                            "hat ... gefangen",
                        )
                ]
        }
    return vocabulaire


class App:

    def __init__(self):
        pass
