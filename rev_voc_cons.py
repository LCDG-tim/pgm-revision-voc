# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


"""revise voc in console
"""


import random as rdm


from vocabulaire import voc


def revise_voc_in_console(a: dict = voc(), b: dict = voc()):
    list_of_voc_keys = list(a.keys())
    nombre_de_liste_alex = 0
    for i in list_of_voc_keys:
        if isinstance(i, str):
            nombre_de_liste_alex += 1
    list_of_request_possible = [i for i in list_of_voc_keys] + ["tout", 'alex']

    request = input(
        """Choisissez l'une des proposition suivante:
{lst}

Liste à étudier =
""".format(
            lst=", ".join(
                str(i)
                for i in list_of_request_possible
            )
        )
    )
    nb_demande = int(input("combien de question vous seront posées = "))
    while nb_demande < 0:
        nb_demande = int(
                input(
                        "le nombre doit être positif\ncombien de question vous"
                        " seront posées ="
                    )
            )
    compteur = 0
    i = 1
    run = True

    if request == "tout":
        while i <= nb_demande and run:
            request = rdm.choice(list_of_voc_keys)
            key = str(rdm.choice(list(a[request].keys())))
            answer = input("{}: {} (ß) = ".format(request, a[request][key]))
            skipb = True
            while (answer != key) and run and skipb:
                skip = input("skip ? ")

                if skip == "pass":
                    run = False

                elif (skip != ""):
                    answer = input(
                            "{}: {} (ß) = ".format(request, a[request][key])
                        )

                else:
                    skipb = False
                    print(key)
            if (answer == key):
                compteur += 1
                del a[request][key]
                if len(a[request]) == 0:
                    del a[request]
                    request2 = input("continué? yes or no\n")
                    if (request2[0] in "Yy") and (request2[1] in "Ee") \
                            and (request2[2] in "Ss"):
                        a[request] = b.copy().get(request)
                    else:
                        run = False
            i += 1

    elif (request == "alex"):
        while i <= nb_demande and run:
            request = rdm.choice(
                    [
                            ".".join(["A", str(i)])
                            for i in range(1, nombre_de_liste_alex + 1)
                        ]
                )
            key = str(rdm.choice(list(a[request].keys())))
            answer = input("{}: {} (ß) = ".format(request,
                           a[request][key]))
            skipb = True
            while (answer != key) and run and skipb:
                skip = input("skip ? ")

                if skip == "pass":
                    run = False

                elif (skip != ""):
                    answer = input(
                            "{}: {} (ß) = ".format(request, a[request][key])
                        )

                else:
                    skipb = False
                    print(key)
            if (answer == key):
                compteur += 1
                del a[request][key]
                if len(a[request]) == 0:
                    del a[request]
                    request2 = input("continué? yes or no\n")
                    if (request2[0] in "Yy") and (request2[1] in "Ee") \
                            and (request2[2] in "Ss"):
                        a[request] = b.copy().get(request)
                    else:
                        run = False
            i += 1

    else:
        if "." in request:
            request = float(request)

            while i <= nb_demande and run:
                key = (str(rdm.choice(list(a[request].keys()))))
                answer = input(
                        "{}: {} (ß) = ".format(request, a[request][key])
                    )
                skipb = True
                while (answer != key) and run and skipb:
                    skip = input("skip ? ")

                    if skip == "pass":
                        run = False

                    elif (skip != ""):
                        answer = input(
                                "{}: {} (ß) = ".format(
                                        request,
                                        a[request][key]
                                    )
                            )

                    else:
                        skipb = False
                        print(key)
                if (answer == key):
                    compteur += 1
                    del a[request][key]
                    if len(a[request]) == 0:
                        del a[request]
                        request2 = input("continué? yes or no\n")
                        if (request2[0] in "Yy") and (request2[1] in "Ee") \
                                and (request2[2] in "Ss"):
                            a[request] = b.copy().get(request)
                        else:
                            run = False
                i += 1

        else:
            request = int(request)

            list_of_chapter_voc = [
                i
                for i in list_of_voc_keys
                if isinstance(i, float)
                if request < i < request + 1
            ]

            while i <= nb_demande and run:
                request = rdm.choice(list_of_chapter_voc)
                key = rdm.choice(list(a[request].keys()))
                answer = input(
                        "{}: {} (ß) = ".format(
                                request,
                                a.get(request).get(key)
                            )
                    )

                skipb = True
                while (answer != key) and run and skipb:
                    skip = input("skip ? ")

                    if skip == "pass":
                        run = False

                    elif (skip != ""):
                        answer = input(
                                "{}: {} (ß) = ".format(
                                        request,
                                        a[request][key]
                                    )
                            )

                    else:
                        skipb = False
                        print(key)
                if (answer == key):
                    compteur += 1
                    del a[request][key]
                    if len(a[request]) == 0:
                        del a[request]
                        request2 = input("continué? yes or no\n")
                        if (request2[0] in "Yy") and (request2[1] in "Ee") \
                                and (request2[2] in "Ss"):
                            a[request] = b.copy().get(request)
                        else:
                            run = False
                i += 1

    print(
            "{} / {} soit {} % de bonnes réponses".format(
                    compteur,
                    i - 1,
                    round(compteur / (i - 1) * 100, 2)
                )
        )


if __name__ == "__main__":
    revise_voc_in_console()
