import meteo as m

msg_list = [
    ["🕯️Bonjour Franck","rand"], #1
    ["🕯️Je suis ©BigBirthdayBot 🎉🤖", "rand"] ,#2
    ["🕯️En ce 28/05/2023, je tiens à célébrer Habbybirthbot.io, mon modèle. Je t'enverrai 36 bougies 🕯️", "rand"] , #3
    ["🕯️C'est déjà le 5ème, ça va trop vite !", "rand"] , #4
    ["🕯️Un peu comme le temps qui passe...", "rand"] , #5
    ["🕯️En parlant de temps qui passe, ne trouves-tu pas que 36 est une beau nombre ? 💡", "rand"] , #6
    ["🕯️Si tu multiplies les dizaines par 2, le résultat est équal au chiffre des unités !", "rand"] , #7
    ["🕯️Magnifique n'est-ce pas ?", "rand"] , #8
    ["🕯️Avant d'être centenaire, seuls les âges de 12, 24, 34 et 48 ans peuvent prétendrent à de telles propriétés ! 💥", 1] , #9
    ["🕯️*_Erreur 400 : Failure... Failure..._*", 1] , #10
    ["🕯️_Error_message : Puissance de calcul nécessaire trop importante_", "rand"] , #11
    ["🕯️Arrêtons les calculs, ça a failli cramer mes circuits !!", "rand"] , #12
    ["🕯️Bon alors, qu'est-ce que tu as prévu de beau en cette journée ?", "rand"] , #13
    ["🕯️Si tu te trouves à Genneviliers le temps est " + m.meteo(m.Gennevilliers)['temps'].lower() + " et la température de " + str(m.meteo(m.Gennevilliers)['temperature']) + "°C", "rand"] , #14
    ["🕯️Au Touquet, le temps est " + m.meteo(m.LeTouquet)['temps'].lower() + " et la température de " + str(m.meteo(m.LeTouquet)['temperature']) + "°C", "rand"] , #15
    ["🕯️Peu importe où tu te trouves, j'espère (_je = moi bot doué de conscience, openIA est un enfant pour moi_)", "rand"] , #16
    ["🕯️Bref fin de la parenthèse, j'espère de Justine, Paul, Rose et Alix t'ont préparé une journée de folie", "rand"] , #17
    ["🕯️Et que tu n'es pas trop mal de ta soirée d'hier à l'impasse", "rand"] , #18
    ["🕯️avec les litres de champagne que tu as du siffler, ça ne m'étonnerait pas !", "rand"] , #19
    ["🕯️Profite bien de cette journée et un..", "rand"] , #20
    ["🕯️🕯️🕯️🕯️*TRES BON ANNIVERSAIRE* 🕯️🕯️🕯️🕯️", "rand"] , #21
    ["🕯️🕯️🕯️*TANK TANK TANK* 🕯️️🕯️🕯️", "rand"] , #22
    ["🕯️Ceci était une série de messages automatiques délivrés par ©BigBirthdayBot, c'était cadeau ! 😘", "rand"] #23
   ]
