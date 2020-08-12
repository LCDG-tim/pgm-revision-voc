# -*- coding: utf-8 -*-


import random as rdm


def voc() -> dict:
    vocabulaire = {
                0.01: {
                        "In meinem Vortrag möchte ich das Thema ... behandeln": "Dans mon exposée je veux traiter le thème ...",
                        "Ich möchte in meinem Bericht über ... sprechen": "Je veux, dans mon écrit, parler de ...",
                        "Im ersten Teil werde ich ... (+ VI fin)": "Dans une première partie, je vais (+VI) de ...",
                        "Im zweiten Teil ...": "Dans une seconde partie",
                        "Im dritten Teil ...": "Dans une troisième partie",
                        "Zuerst werde ich versuchen, auf die Frage ... beantworten": "Tout d'abord, je chercherai à répondre à la question ...",
                        "Dann/Dannach (+ V2)": "Puis/Ensuite (+ V2)",
                        "Zum Schluss möchte ich ... (+ VI fin)": "Pour finir, je veux (+ VI) ...",
                        "Schließlich möchte ich ... (+ VI fin)": "Enfin, je veux (+ VI) ...",
                        "Anschließend möchte ich ... (+ VI fin)": "Finallement, je veux (+ VI) ...",
                        "zum Beispiel": "par exemple (zum)",
                        "beispielweise": "par exemple",
                        "Ich möchte einen Beispiel nennen": "je veux citer un exemple",
                        "Ich möchte einen Beispiel anführen": "je veux donner un exemple",
                        "Ein Beispiel für ... ist ...": "un exemple pour ... est ...",
                        "Im Unterricht haben wir einen Text/einen Hörtext zu diesem Thema besprochen": "En cour nous avons étudier un texte/audio qui parlait sur le thème",
                        "Es handelt sich um einen Auszug aus dem Roman ... von ...": "Il s'agissait du roman ... de ...",
                        "Es handelt sich um einen Bericht über ...": "Il s'agissait d'un écrit sur ...",
                        "Es handelt sich um einen Zeitungsartikel zum Thema ...": "Il s'agissait d'un article de journal sur le thème de de ...",
                        "Wir haben zum Beispiel ein sehr interessantes Interview mit (D) gehört/gelesen und ich habe dabei erfahren, dass ... (+ V fin)": "nous avons entendu, lu par exemple une interview très interressante avec (D) et je compris que ...",
                        "In diesem Text/Film wird gezeit, wie ... (+ V fin)": "dans ce texte/film qui est montré, nous ... (+ V fin)",
                        "im Vergleich zu": "comparé à",
                        "in Unterschied zu": "à la différence de",
                        "im Gegensatz zu": "contrairement à",
                        "verglichen mit": "comparé à",
                        "und": "et",
                        "auch": "aussi",
                        "sowie": "aussi bien que",
                        "außerdem": "en plus",
                        "weiterhin": "en houtre",
                        "ansonsten": "autrement",
                        "sonst": "sinon",
                        "zusätzlich": "de surcroït",
                        "jedoch": "cependant",
                        "dennoch": "pourtant (de)",
                        "trotzdem": "pourtant",
                        "zwar ... aber": "certes ... mais",
                        "einerseits ... andereseits": "d'une part ... d'autre part",
                        "während (+ V fin)": "tandis que",
                        "obwohl (+ V fin)": "bien que",
                        "V2 + nämlich": "en effet",
                        "weil (+ V fin)": "parce que",
                        "da (+ V fin)": "puisque",
                        "denn": "car",
                        "deshalb (+ V2)": "c'est pourquoi",
                        "darum (+ V2)": "voilà pourquoi",
                        "aus diesem Grund (+ V2)": "pour cette raison",
                        "vor + D": "avant",
                        "nach + D": "après",
                        "bei + D": "lors de",
                        "vor + D (indication temporelle)": "il y a + indication temporelle",
                        "zu + D": "les fêtes",
                        "in + D": "l'année, la saison, le mois, le moment",
                        "an + D": "le jour et le moment de la journée",
                        "um": "l'heure exacte",
                        "Seit wann?": "Depuis quand?",
                        "seit + D": "depuis",
                        "seit": "depuis que (court)",
                        "seitdem": "depuis que (long)",
                        "seither": "depuis (lors)",
                        "seitdem (lors)": "depuis (lors)",
                        "seit langem": "depuis longtemps",
                        "schon lange/längst": "depuis longtemps(schon)",
                        "Bis wann?": "jusqu'à quand?",
                        "bis zu + D": "jusqu'à",
                        "bis": "jusqu'à ce que, avant que",
                        "bisher": "jusqu'alors",
                        "bislang": "jusqu'alors",
                        "Wie lange?": "combien de temps?",
                        "... (A) Lang": "durant ... (court)",
                        "togelang": "durant ... (t)",
                        "wochenlang": "durant ... (w)",
                        "solange": "tant que",
                        "lange": "longtemps",
                        "längst": "depuis longtemps",
                        "schon lange": "depuis longtemps (sc)",
                        "von ... bis ...": "de ... à ...",
                        "nie": "jamais",
                        "Ich finde, dass ...": "Je trouve que ...",
                        "Ich denke, dass ...": "Je pense que ...",
                        "Ich glaube, dass ...": "Je crois que ... ",
                        "Ich meine, dass ...": "Je pense que ... (pensée)",
                        "ich bin der Meinung, dass ...": "j'ai la pensé que ...",
                        "Meine Meinung nach, (+ V2) ...": "D'après ma pensée, ...",
                        "Ich bin mit Herrn W. (nicht) einverstanden": "Je (ne) suis (pas) d'accord avec Herrn W.",
                        "Herr W. denkt, dass ... Ich bin damit (nicht) einverstanden": "Mr. W. pense que ... je (ne) suis (pas) d'accord avec lui",
                        "Herr W. ist für/gegen ... Ich bin dafür / dagegen": "Mr W. est pour contre ... Je suis aussi pour / contre",
                        "In diesem Vortrag habe ich versucht, über ... nachzudenken": "Dans mon exposé, j'ai cherché à penser sur ...",
                        "In diesem Vortrag habe ich versucht, Ihnen über die Begriffe und Inhalte ... meine Gedanken darszustellen": "dans mon exposé, j'ai cherché grace à ... , à vous présenter ma pensée",
                        "Um meinem Vortrag zu beenden, (+ V2)": "Pour finir mon exposé, ...",
                        "Viele Danke!": "Merci beacoup!",
                        "Danke schön!": "Merci bien!",
                        "Ich bedanke mich bei Ihnen für Ihre Aufmerksamkeit": "Je vous remercie",
                        "Absatz": "paragraphe",
                        "indem +Vfin": "en + Vfin",
                        "die Welt": "le monde",
                        "das Fahrrad(¨-er)": "le vélo",
                        "adj-er als": "comparatif de supériorité",
                        "nicht so adj wie": "comparatif d'infériorité"
                        },
                0.1: {
                        "mich": "je (A)",
                        "dich": "tu (A)",
                        "ihn": "il (A)",
                        "sie": "elle (A)",
                        "es": "neutre (A)",
                        "wir": "nous (A)",
                        "ihr": "vous (A)",
                        "Sie": "vous (politesse) (A)",
                        "sie (pluriel)": "ils, elles (A) (add (pluriel) )"
                        },
                0.2: {
                        "mir": "je (D)",
                        "dir": "tu (D)",
                        "ihm": "il (D)",
                        "ihm (neutre)": "neutre (D) (add (neutre) )",
                        "ihr": "elle (D)",
                        "uns": "nous (D)",
                        "euch": "vous (D)",
                        "Ihnen": "vous (politesse) (D)",
                        "ihnen": "ils, elles (D)"
                        },
                0.3: {
                        "müssen": "devoir (dépend de moi)",
                        "können": "pouvoir (dépend de moi)",
                        "wollen": "vouloir (dépend de moi)",
                        "sollen": "devoir (dépend d'un tiers)",
                        "dürfen": "pouvoir (dépend d'un tiers)",
                        "mögen": "souhaiter (dépend d'un tiers)",
                        "sein": "être",
                        "haben": "avoir",
                        },
                0.4: {
                        "trotzdem": "pourtant, malgré tout, quand même",
                        "obwohl +Vfin": "bien que (mot subordonnant)",
                        "auch wenn": "même si (mot subordonnant)",
                        "sobald": "dès que",
                        "während": "pendant que, tandis que",
                        "wenn": "quand, lorsque",
                        "als": "quand, lorsque, au moment où"
                        },
                0.5: {
                        "durch": "à travers, grâce à",
                        "für": "pour + GN",
                        "gegen": "contre",
                        "ohne": "sans",
                        "um": "autour de",
                        },
                0.6: {
                        "aus": "hors de",
                        "bei": "chez",
                        "mit": "avec",
                        "nach": "après",
                        "seit": "depuis",
                        "von": "de",
                        "zu": "vers, chez"
                        },
                0.7: {
                        "während": "pendant",
                        "trotz": "malgré",
                        "(an)statt": "au lieu de",
                        "wegen": "à cause de"
                        },
                2.1: {
                        "die Herkunft": "l'origine",
                        "Woher": "d'où",
                        "her/kommen": "provenir",
                        "aus ... kommen": "venir de ...",
                        "dort": "là-bas",
                        "hier": "ici",
                        "die Heimat": "le pays d'accueil/le pays d'adoption",
                        "aus ... stammen": "provenir de ...",
                        "die Wurzel(-n)": "la racine",
                        "wo ich hingehöre": "là où je suis à ma place/chez moi",
                        "die Geborgenheit": "le sentiment de sécurité",
                        "sich geborgen fühlen": "se sentir en sécurité",
                        "sich wohl fühlen": "se sentir bien",
                        "traurig": "triste",
                        "sich in (A) integrieren": "s'intégrer à",
                        "Heimweh haben": "avoir le mal du pays, avoir le cafard",
                        "etw. fehlt mir": "qqch me manque (mir)",
                        "ich vermisse etw.": "qqch me manque (ich)",
                        "die Freiheit": "la liberté"
                        },
                2.2: {
                        "die Landschaft": "le paysage",
                        "der Ort(-e)": "le lieu",
                        "die Geschichte": "l'histoire",
                        "die Architektur": "l'architechture",
                        "das Erbe": "l'héritage",
                        "die Tracht(-en)": "die traditionelle Kleidung = l'habit traditionnel",
                        "der Kiosk, die Imbiss, die Bude": "le snack-bar",
                        "etw. dar/stellen": "représenter qqch",
                        "etw. symbolisieren": "symboliser qqch",
                        "etw. bedeuten": "signifier qqch",
                        "jm. wichtig sein": "être important pour qqn"
                        },
                2.3: {
                        "integriert sein": "être intégré",
                        "mit jm. in Kontakt kommen": "entrer en contact avec qqn",
                        "etw. gemeinsam haben": "avoir qqch en commun",
                        "das Zugehörigkeitsgefühl": "le sentiment d'appartenance",
                        "eine Zukunft haben": "avoir un avenir",
                        "die Freiheit": "la liberté",
                         "in ... leben": "vivre à/en ...",
                        "das Leben": "la vie",
                        "in ... auf/wachsen": "grandir en/à ...",
                        "die Flucht": "la fuite",
                        "aus einem Land fliehen": "fuir un pays",
                        "in Frieden leben": "vivre en paix",
                        "die Hilfsbereitschaft": "la serviabilité",
                        "jm. helfen": "aider qqn",
                        "etw. beschützen": "protéger qqch",
                        "sich heimisch fühlen": "se sentir chez soi"
                        },
                2.4: {
                        "weh tun": "faire mal",
                        "schmerzen": "faire souffrir, être douloureux",
                        "unerreichbar": "inaccessible",
                        "verloren": "perdu",
                        "zerstört": "détruit",
                        "Fernweh haben": "avoir envie d'ailleurs, avoir la nostalgie du voyage",
                        "eine Grenze überwinden": "surmonter, dépasser une frontière",
                        "etw. vermitteln": "transmettre qqch",
                        "etw. suchen": "chercher qqch",
                        "sich nach etw. sehnen": "désirer qqch",
                        "die Sehnsucht nach ...": "le désir de ...",
                        "das Besondere": "le caractère particulier, la spécificité",
                        "Identität stiften": "forger une identité"
                        },
                4.1: {
                        "das Festival(-s)": "le festival",
                        "ein Instrument spielen": "jouer d'un instrument",
                        "in einer Band, einem Orchestre spielen": "jouer dans un groupe de musique, un Orchestre",
                        "der Teilnehmer(-)": "le participant",
                        "der Auftritt(-e)": "le passage sur scène",
                        "auf/treten": "se produire sur scène",
                        "etw. auf/führen": "jouer qqch",
                        "etw. veranstalten": "etw. organisieren",
                        "an etw. (D) teil/nehmen": "participer à qqch (teil)",
                        "bei etw. (D) mit/machen": "participer à qqch (mit)",
                        "auf/nehmen": "enregistrer"
                        },
                4.2: {
                        "der Frieden": "la paix",
                        "das Glück": "le bonheur",
                        "die Freundschaft": "l'amitié",
                        "die Liebe": "l'amour",
                        "die Freiheit": "la liberté",
                        "frei": "libre",
                        "Werte vermitteln": "transmettre des valeurs",
                        "die Gerechtigkeit": "la justice",
                        "das Zugehörigkeitsgefühl": "le sentiment d'appartenance",
                        "die Gleichheit": "l'égalité des droits",
                        "gleich sein": "être égal",
                        "die Vielfalt": "la diversité",
                        "sich für / gegen etw. engagieren, ein/setzen": "s'engager pour / contre qqch",
                        "jm. unterstützen": "soutenir qqn",
                        "Einfluss auf jn./etw. haben": "avoir de l'influence sur qqn/qqch",
                        "sich fûr / gegen etw. (A) kämpfen": "se battre pour / contre qqch",
                        "zu etw. (D) Stellung nehmen": "prendre position sur qqch"
                        },
                4.3: {
                        "die Integration": "l'intégration",
                        "sich in (A) integrieren": "s'intégrer dans",
                        "neue Menschen, Kulturen kennen lernen": "faire la connaissance de nouvelles personnes, découvir de nouvelles cultures",
                        "die Fremdsprache(-n)": "la langue étrangère",
                        "der Flüchtling(-e)": "le réfugier",
                        "der Migrant(-en)": "le migrant",
                        "aus einem Land fliehen": "fuir un pays",
                        "in einem Land bleiben": "rester dans un pays",
                        "benachteiligt": "défavorisé",
                        "etw. fördern = stärken": "soutenir, consolider qqch",
                        "die Sprachbariere überwinden": "surmonter la barière de la langue",
                        "jn. mit etw. verbinden": "relier, unir qqn à qqch",
                        "etw. verbinden": "relier qqch",
                        "etw. trennen": "séparer, diviser qqch",
                        "verbindend": "qui relie, qui unit",
                        "trennend": "qui sépare",
                        "bereichern": "enrichir",
                        "bereichernd": "enrichissant",
                        "jm. etw. bei/bringen": "apprendre qqch à qqn",
                        "etw. ermöglichen, erlauben": "permettre qqch",
                        "etw. erleichtern": "faciliter qqch"
                        },
                4.4: {
                        "die Gesellschaft": "la société",
                        "die Zensur": "la censure",
                        "etw. zensieren": "censurer qqch",
                        "das Werk(-e)": "l'oeuvre",
                        "die Gemeinschaft": "la communauté",
                        "die Verantwortung": "la responsabilité",
                        "die politische Macht": "le pouvoir politique",
                        "die Meinungsfreiheit": "la liberté d'expression",
                        "das Regime kritisieren": "critiquer le régime",
                        "etw. verbieten": "interdir qqch",
                        "etw. erlauben": "autoriser qqch",
                        "das Verbot(-e)": "l'interdiction",
                        "die Erlaubnis": "l'autorisation",
                        "etw. (D) entsprechen": "correpondre à qqch",
                        "jn. von etw. überzeugen": "convaicre qqn de qqch"
                        },
                4.5: {
                        "der Verein(-e)": "l'association",
                        "etw. bieten": "proposer qqch",
                        "die darstellende und bildende Kunst": "les arts dramatiques et plastique",
                        "das Selbstbewusstsein": "la confiance en soi",
                        "jn. zu etw. an/regen": "inciter qqn à qqch",
                        "das Lied(-er)": "la chanson",
                        "sagen": "dire",
                        "das Motto": "le slogan",
                        "der Widerstand": "le résistant",
                        "statt/finden": "avoir lieu",
                        "der Eintritt": "l'entrée",
                        "dauern": "durer",
                        "das Mitglied": "le membre"
                        },
                7.1: {
                        "der Ort(-e)": "le lieu",
                        "der Wald(¨-er)": "la forêt",
                        "der Baum(¨-e)": "l'arbre",
                        "das Holz": "le bois",
                        "der Vollmond": "la pleine lune",
                        "spazieren gehen": "se promener",
                        "einen Spaziergang machen": "faire une promenade",
                        "wandern": "randonner",
                        "der Jäger": "le chasseur",
                        "der Vogel(¨-)": "l'oiseau",
                        "Vögel beobachten, hören": "observer, entendre les oiseaux",
                        "ruhig": "calme",
                        "still": "silencieux",
                        "die Ruhe": "le calme",
                        "die Stille": "le silence",
                        "die Meditation": "la méditation",
                        "meditieren": "méditer",
                        },
                7.2: {
                        "die Landschaft": "le paysage",
                        "Feuer an/machen": "faire du feu",
                        "die Natur verherrlichen": "glorifier la nature",
                        "die pure/reine Luft genießen": "apprècier, profiter de l'air pur",
                        "Landschaftsbilder malen": "peindre des paysages",
                        "der Rückzugsort": "le refuge",
                        "der Sehnsuchtsort": "le lieu auquel on aspire",
                        "sich von der Natur inpirieren lassen": "s'inspirer de la nature",
                        "der innere Frieden": "la paix intérieur",
                        "in Harmonie mit der Natur leben": "vivre en harmonie avec la nature"
                        },
                7.3: {
                        "die Legende(-n)": "la légende (leg)",
                        "die Sage(-en)": "la légende(sag)",
                        "das Mythos(die Mythen)": "le Mythe",
                        "der Räuber(-)": "le voleur",
                        "die Erzählung(-en)": "le récit",
                        "die böse Hexe": "la méchante sorcière",
                        "der Wolf": "le loup",
                        "der Geist": "l'esprit",
                        "auf Geister treffen": "tomber sur des esprits",
                        "jm. begegnen": "rencontrer qqch",
                        "das Bedroliche": "ce qui est menaçant",
                        "bedrolich": "menaçant",
                        "sich verrierren": "se perdre",
                        "sich verlaufen": "s'égarer",
                        "eine spannende Geschichte": "une histoire passionnante",
                        "vor etw. (D) Angst haben": "avoir peur de qqch",
                        "Angst, Furcht aus/lösen": "provoquer la peur",
                        "etw. befürchten": "craindre qqch",
                        "gruselig": "qui donne des frissons",
                        "ein grauenerregende Geschichte": "une histoire d'épouvante",
                        "eine düstere Stimmung": "une ambiance sombre",
                        "erschreckend": "effrayant",
                        "jm. erschrecken": "effrayer qqn",
                        "erschrecken": "prendre peur",
                        "die Gefahr": "le danger",
                        "gefahrlich": "dangereux",
                        "einer Gefahr ausgesetzt sein": "être exposé à un danger",
                        "sich in etw. (A) verwandeln": "se transformer en qqch",
                        "die Verwandlung": "la métamorphose"
                        },
                6.1: {
                        "der Senior(-en)": "le senior, la personne agée",
                        "einsam": "seul, solitaire",
                        "jn. unterhalten": "divertir qqn",
                        "behindert": "handicapé",
                        "jn. begleiten": "accompagner qqn",
                        "jn. unterstützen": "soutenir qqn",
                        "Geld spenden": "donner de l'argent",
                        "Schulmaterial spenden": "donner des fournitures scolaires",
                        "obdachlos": "sans-abri",
                        "auf der Straße leben": "vivre dans la rue",
                        "Essen verteilen": "distribuer à manger",
                        "Decken verteilen": "distribuer des couvertures"
                        },
                6.2: {
                        "der Flüchtling(-e)": "le réfugié",
                        "der Pate(-n)": "le parrain",
                        "die Patin(-nen)": "la marraine",
                        "das Familienmitglied(-er)": "le membre de la famille",
                        "jm. den Alltag zeigen": "montrer la vie quotidienne à qqn",
                        "mit jm. Zeit verbringen": "passer du temps avec qqn",
                        "aus seiner Heimat fliehen": "fuir son pays",
                        "vor dem Krieg fliehen": "fuir la guerre",
                        "monatelang auf der Flucht sein": "être en fuite pendant des mois",
                        "verfolgt werden": "être persécuter",
                        "in Not leben": "vivre dans le besoin",
                        },
                6.3: {
                        "(etw.) kochen": "faire la cuisine, cuisinier",
                        "den Tisch decken != ab/decken": "mettre != débarrasser la table",
                        "die Spülmaschine aus/räumen": "vider le lave-vaisselle",
                        "den Müll weg/bringen": "sortir la poubelle",
                        "die Freude": "la joie",
                        "froh": "content, joyeux",
                        "die Begeisterung": "l'enthousiasme",
                        "begeistert": "enthousiaste",
                        "ein Land entdecken": "découvrir un pays",
                        "ein Abenteuer erleben": "vivre une aventure",
                        "seinen Traum verwirklichen": "réaliser son rève",
                        "vor etw. (D) Angst haben": "avoir peur de qqch",
                        "der Mut": "le courage",
                        "mutig": "courageux",
                        "den Mut nicht verlieren": "ne pas se décourager",
                        "(keine) Vorurteile haben": "(ne pas) avoir des (de) préjugés",
                        "anders leben": "vivre autrement"
                        },
                9.1: {
                        "der Treffpunkt": "le point de rencontre",
                        "die erweiterte Realität (AR: Augmented Reality)": "la réalité augmentée",
                        "die künstliche Intelligenz (= KI)": "l'intelligence artificielle",
                        'etw. aus/leben':'expérimenter qqch ; exprimer qqch',
                        'etw. / jn. beeinflussen': 'influencer qqch / qqn',
                        'ab/schalten': 'se couper du monde, de la réalité ; se déconnecter',
                        'die Einsamkeit': 'la sollitude',
                        'die Täuschung': 'l\'illusion',
                        'die Unterhaltung': 'le divertissement',
                        'die Abhängigkeit': 'la dépendance, l\'addiction',
                        'für etw. verantwortlich sein': 'être responsable de qqch',
                        'die Verantwortung': 'la responsabilité',
                        'mit etw. verbunden sein': 'être lié à qqch'
                        },
                9.2: {
                        "der Vorteil(-e)": "l'avantage, le point positif",
                        "der Fortschritt(-e)": "le progrès",
                        "fortschritt": "progressiste",
                        "die Unterhaltung": "le divertissement",
                        "etw. ermöglichen": "rendre qqch possible",
                        "etw. aus/leben": "expérimenter, vivre qqch ; exprimer qqch",
                        "etw. bestellen": "commander qqch",
                        "etw. liefern": "livrer qqch",
                        "jm. helfen": "aider qqn",
                        "etw. ab/schaffen": "supprimer qqch",
                        "etw. ersetzen": "remplacer qqch",
                        "jm. etw. bei/bringen": "apprendre qqch à qqn",
                        "etw. lösen": "résoudre qqch",
                        "die Lösung(-en)": "la solution",
                        "einfach": "simple",
                        "etw. vereinfachen": "simplifier qqch"
                        },
                9.3: {
                        "der Nachteil(-e)": "l'inconvénient, le point négatif",
                        "der Missbrauch": "l'abus",
                        "missbrauchen": "abuser de qqch",
                        "einsam sein": "être isolé, seul",
                        "die Einsamkeit": "la sollitude",
                        "die Täuschung": "l'illusion",
                        "der Rückschritt(-e)": "la régression",
                        "rückschrittlich": "régressif",
                        "erniedrigend": "humiliant",
                        "die Gefahr(-en)": "le danger",
                        "gefahrlich": "dangereux",
                        "etw. / jm. ausgesetzt sein": "être à la merci de qqch / qqn",
                        "von etw. / jm. (un)abhängig sein": "être (in)dépendant de qqch / qqn",
                        "die Abhängigkeit": "la dépendance",
                        "konditioniert, unterworfen sein": "être conditionné, soumis",
                        "jn. beurteilen": "juger qqn",
                        "das Vorurteil(-e)": "le préjugé"
                        },
                9.4: {
                        "in der Zukunft": "dans le futur",
                        "verantwortlich": "responsable",
                        "Verantwortung für etw. tragen": "porter la responsabilité de qqch",
                        "die Gesellschaft": "la société",
                        "die Regierung": "le gouvernement",
                        "die Gesundheit": "la santé",
                        "für jn. Entscheidungen treffen": "prendre des décisions pour qqn",
                        "bewusst": "conscient",
                        "unbewusst": "inconscient",
                        "die Partei(-en)": "le partie politique",
                        "jn. identifizieren": "identifier qqn",
                        "der Bürger(-)": "le citoyen",
                        "die Bürgerin(-nen)": "la citoyenne",
                        "Kritik an etw. (D) üben": "faire une critisque",
                        "etw. / jn. kritisieren": "critiquer qqch / qqn",
                        "in Frage stellen, etw. hinterfragen": "remettre en question qqch",
                        "(keine) Willensfreiheit haben": "(ne pas) avoir de libre arbitre",
                        "etw. fördern": "financer qqch",
                        "die Förderung": "la subvention",
                        "etw. her/stellen": "etw. produzieren",
                        "menschlich": "humain",
                        "das Menschliche": "le caractère humain",
                        "etw. unterstützen": "soutenir qqch"
                        },
                9.9: {
                        'etw. (nicht) verwechseln': '(ne pas) confondre qqch',
                        'etw. ein/blenden': 'insérer, afficher qqch',
                        'der ieere Teiler': 'l\'assiette vide',
                        'das Gericht(-e)': 'le plat',
                        'beamen': 'télétransporter, téléporter',
                        },
                11.1: {
                        "sich befinden, liegen": "se trouver, être situé",
                        "der Norden": "le nord",
                        "der Süden": "le sud",
                        "der Osten": "l'est",
                        "der Westen": "l'ouest",
                        "nördlich / südlich von": "au nord / sud de",
                        "im Nordosten, Südwesten, im Zentrum ... liegen": "être situé au nord-est, au sud-ouest, au centre",
                        "ein Stadtstaat": "une ville-Etat",
                        "eine Stadt und ein Bundesland zugleich": "une ville qui est aussi un land",
                        "die sprachliche Vielfalt": "la diversité linguistique",
                        "der Unterschied(-e)": "la différence",
                        "die Gemeinsamkeit(-en)": "la similitude, le point commun",
                        "sich durch etw. unterschieden": "se distinguer par qqch",
                        "mit etw. vergleichen": "comparer à qqch",
                        "gleich sein": "être identique",
                        "anders sein": "être différent",
                        "verschieden": "différent, divers",
                        "das Bundesland(¨-er)": "le land, l'Etat fédéré",
                        "der Stadtstaat(-en)": "la ville-Etats",
                        "groß": "grand",
                        "klein": "petit",
                        "der Dialekt(-e)": "le dialecte, la langue régionnale",
                        "dagegen": "en revanche(adverbe)",
                        "aber": "mais",
                        "im Vergleich mit / zu": "comparé à",
                        "im Unterschied zu (D)": "à la différence de",
                        "adj-er als": "comparatif de supériorité",
                        "nicht so adj wie": "comparatif d'infériorité"
                        },
                11.2: {
                        "die Bundesrepublik Deutschland": "la république fédéral d'Allemagne",
                        "der Osten": "l'Est",
                        "der Westen": "l'Ouest",
                        "der Norden": "le Nord",
                        "der Süden": "le Sud",
                        "das Bundesland(¨-er)": "le land",
                        "föderal": "fédéral",
                        "der Föderalismus": "le fédéralisme",
                        "der Staat(-en)": "l'Etat",
                        "der Stadtstaat(-en)": "la ville-Etat",
                        "die Regierung": "le gouvernement",
                        "der Kanzler": "le chancelier",
                        "die Kanzlerin": "la chancelière",
                        "der Dialekt(-e)": "le dialecte"
                        },
                11.3: {
                        "der Erste Weltkrieg": "la Première guerre mondiale",
                        "der Zweite Weltkrieg": "la Seconde Guerre mondiale",
                        "die BRD (Bundesrepublik Deutschland)": "la RFA, l'Allemagne de l'Ouest",
                        "die DDR (Deuscthe Demokratische Republik)": "die RDA, l'allemagne de l'Est",
                        "das Deutsche Kaiserreich": "l'Empire allemand",
                        "einigen": "unifier",
                        "die Einigung": "l'unification",
                        "etw. gründen": "fonder qqch",
                        "die Gründung": "la création, la fondation",
                        "etw. teilen": "diviser qqch",
                        "die Teilung": "la division",
                        "etw. trennen": "séparer qqch",
                        "die Trennung": "la séparation",
                        "etw. versuchen": "tenter, essayer qqch",
                        "der Versuch": "la tentative",
                        "fliehen": "s'enfuir",
                        "die Flucht": "la fuite",
                        "eine Mauer bauen": "construire un mur",
                        "der Bau der Berliner Mauer": "la construction du mur de Berlin",
                        "der Fall der Berliner Mauer": "la chute du mur de Berlin",
                        "jn. erschießen": "abattre, tuer qqn par balle",
                        "jn. ein/sperren": "incarcérer, emprisonner qqn",
                        "jn. fest/nehmen": "arrêter qqn",
                        "die Wende": "le \"tournant\", le processus de changement social et politique en RDA qui a conduit à la réunification",
                        "vereinigen": "réunir",
                        "die Wiedervereinnigung": "la réunification",
                        "die deutsche Einheit": "l'unité allemande",
                        "beeinflussen": "influencer",
                        "der Einfluss(¨-e)": "l'influence",
                        "prägen": "marquer",
                        "die Prägung": "la marque, l'empreinte"
                        },
                11.4: {
                        "die wirschaft": "l'économie",
                        "stark": "fort",
                        "schwach": "faible",
                        "die Kluft": "le fossé",
                        "arbeitlos sein": "être au chômage",
                        "die Arbeitlosigkeit": "le chômage",
                        "jn. beschäftigen": "employer qqn",
                        "die Vollbeschäftigung": "le pleine emploi",
                        "der Bereich(-e)": "le domaine",
                        "die Gesundheit": "la santé",
                        "Berufstätig sein": "avoir une activité professionnelle",
                        "die Berufstätigkeit": "l'activité professionnelle",
                        "gleichberichtigt sein": "avoir les mêmes droits",
                        "die Gleichberichtigung": "l'egalité des droits"
                        },
                11.9: {
                        "der Arbeitslose": "le chômeur",
                        "niemand": "personne",
                        "sich ein/bilden": "s'imaginer à tort",
                        "per Sprachfeld": "par commande vocale",
                        "die Tastadur": "le clavier",
                        "sich die Mühe machen": "se donner la peine, faire l'effort de",
                        "die Lieferdrohne": "le drone livreur",
                        "der Zufall": "le hasard",
                        "die überaschung": "la surprise",
                        "etw. errechnen": "calculer qqch",
                        "das Fürstentum(¨-er)": "la principauté",
                        "mit etw. brechen": "rompre avec qqch",
                        "verhinden": "empêcher",
                        'die Wiederherstellung': "la restauration",
                        "wieder her/stellen": "rétablir",
                        "der Sohn": "le fils"
                        },
                "A.1": {
                        "jm. etw. schenken": "offrir qqch à qqn"
                        },
                "A.2": {
                        "natürlich": "Naturellement"
                        }
                    }
    assert isinstance(vocabulaire, dict), "vocabulaire n'est pas un dict"
    return vocabulaire


def save():
    voca = voc()
    with open("vocabulaire.csv", "w") as file:
        file.write("liste;allemand;francais\n")
        for i in voca.keys():
            for j in voca[i].items():
                file.write("{};{};{}\n".format(i,j[0], j[1]))


def test(a: dict = voc(), b: dict = voc()):
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
        nb_demande = int(input("le nombre doit être positif\ncombien de question vous seront posées ="))
    compteur = 0
    i = 1
    run = True

    if (request == "tout") :
        while i <= nb_demande and run:
            request = rdm.choice(list_of_voc_keys)
            key = str(rdm.choice(list(a[request].keys())))
            answer = input("{}: {} (ß) = ".format(request, a[request][key]))
            skipb = True
            while (answer!= key) and run and skipb:
                skip = input("skip ? ")

                if skip == "pass":
                    run = False

                elif (skip != ""):
                    answer = input("{}: {} (ß) = ".format(request, a[request][key]))

                else :
                    skipb = False
                    print(key)
            if (answer == key):
                compteur += 1
                del a[request][key]
                if len(a[request]) == 0:
                    del a[request]
                    request2 = input("continué? yes or no\n")
                    if (request2[0] == "Y" or request2[0] == "y") and (request2[1] == "E" or request2[1] == "e") and (request2[2] == "S" or request2[2] ==  "S"):
                        a[request] = b.copy().get(request)
                    else:
                        run = False
            i += 1

    elif (request == "alex"):
        while i <= nb_demande and run:
            request = rdm.choice([".".join(["A", str(i)]) for i in
                              range(1, nombre_de_liste_alex + 1)]
                        )
            key = str(rdm.choice(list(a[request].keys())))
            answer = input("{}: {} (ß) = ".format(request,
                           a[request][key]))
            skipb = True
            while (answer!= key) and run and skipb:
                skip = input("skip ? ")

                if skip == "pass":
                    run = False

                elif (skip != ""):
                    answer = input("{}: {} (ß) = ".format(request, a[request][key]))

                else :
                    skipb = False
                    print(key)
            if (answer == key):
                compteur += 1
                del a[request][key]
                if len(a[request]) == 0:
                    del a[request]
                    request2 = input("continué? yes or no\n")
                    if (request2[0] == "Y" or request2[0] == "y") and (request2[1] == "E" or request2[1] == "e") and (request2[2] == "S" or request2[2] ==  "S"):
                        a[request] = b.copy().get(request)
                    else:
                        run = False
            i += 1

    else:
        if "." in request:
            request = float(request)

            while i <= nb_demande and run :
                key = (str(rdm.choice(list(a[request].keys()))))
                answer = (input("{}: {} (ß) = ".format(request, a[request][key])))
                skipb = True
                while (answer!= key) and run and skipb:
                    skip = input("skip ? ")

                    if skip == "pass":
                        run = False

                    elif (skip != ""):
                        answer = input("{}: {} (ß) = ".format(request, a[request][key]))

                    else :
                        skipb = False
                        print(key)
                if (answer == key):
                    compteur += 1
                    del a[request][key]
                    if len(a[request]) == 0:
                        del a[request]
                        request2 = input("continué? yes or no\n")
                        if (request2[0] == "Y" or request2[0] == "y") and (request2[1] == "E" or request2[1] == "e") and (request2[2] == "S" or request2[2] ==  "S"):
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
                answer = input("{}: {} (ß) = ".format(request, a.get(request).get(key)))

                skipb = True
                while (answer!= key) and run and skipb:
                    skip = input("skip ? ")

                    if skip == "pass":
                        run = False

                    elif (skip != ""):
                        answer = input("{}: {} (ß) = ".format(request, a[request][key]))

                    else :
                        skipb = False
                        print(key)
                if (answer == key):
                    compteur += 1
                    del a[request][key]
                    if len(a[request]) == 0:
                        del a[request]
                        request2 = input("continué? yes or no\n")
                        if (request2[0] == "Y" or request2[0] == "y") and (request2[1] == "E" or request2[1] == "e") and (request2[2] == "S" or request2[2] ==  "S"):
                            a[request] = b.copy().get(request)
                        else:
                            run = False
                i += 1

    print("{} / {} soit {} % de bonnes réponses".format(compteur,i-1, round(compteur/(i-1)*100, 2)))


if __name__ == "__main__":
    vocabulaire = voc()
    test()
    save()
    del rdm, test, voc