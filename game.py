from re import S
import time
import random

accumulatore_punti_Forza = []
accumulatore_punti_Salute = []
accumulatore_punti_Difesa = []
sex = []
faz = []
name = []
inventario = []
png = ['Cyborg', 'Androide', 'Polizia', 'Cyber-Polizia', 'Soldato Umano', 'Hacker']
png_scelto = []

time.sleep(1)
print('START ROM...')
time.sleep(3)
print('LOAD PROGRAM FILE...')
time.sleep(3)
print('Attendere...')
time.sleep(2)
print('ERRORE!')
time.sleep(5)
print('SCHERZETTO! AH AH AH! :3')
time.sleep(1)

def titolo(): #TITOLO. Si attiva appena parte il gioco
    print('''
    
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄        ▄  ▄    ▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌      ▐░▌▐░▌  ▐░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌░▌     ▐░▌▐░▌ ▐░▌ 
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌  
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌▐░▌░▌   
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░▌    
▐░▌           ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌▐░▌░▌   
▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌▐░▌  
▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌▐░▌ ▐░▌ 
▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌  ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀    ▀ 
                                                                                                                  
    ''')
    time.sleep(1)
    print('Caricamento...\n')
    time.sleep(1)

def menu(): #MENÙ DI GIOCO
    print('Benvenuto!\n')

    while True: #while 1
        scelta = input('\n[START]\nPremi S per iniziare il gioco...\n'
                       '\n[EXIT]\nPremi E per uscire dal gioco...\n')

        if scelta == 'S' or scelta == 's':
            print('Caricamento...\n')
            time.sleep(3)
            start()
            gioco()
            break


        elif scelta == 'E' or scelta == 'e':
            uscita = input('Sei sicuto di voler uscie dal gioco? S/N: ')

            if uscita == 'S' or uscita == 's':
                print('PROGRAMMA TERMINATO...')
                break

            elif uscita == 'N' or uscita == 'n':
                menu()
        
        if uscita != 'S' or uscita != 's' or uscita != 'N' or uscita != 'n':
                print('ERRORE! Carattere non accettato. Attendere...')
                time.sleep(1)

def start(): #INIZIA IL GIOCO
    print('Edoardo Martino presenta:\nCYBERPUNK\n')


def gioco(): #FUNZIONE PRINCIPALE DEL GIOCO. Incorpora le funzioni principali quali scelta_personaggio() e altre
    while True:
        prova_scelta = input('CYBERPUNK è un gioco di ruolo a scelte.\nHai capito? S/N: \n')

        if prova_scelta == 'S' or prova_scelta == 's':
            print('Bene! Incominciamo allora.\n\nRicordati quando vedi S/N dovrai scegliere.\n'
                  'S vuol dire Sì, N vuol dire No.\n'
                  'In alcuni casi dovrai digitare e interaggire direttamente con il gioco.\n')

            scelta_personaggio()

            time.sleep(5)

            print('\nEssendo un gioco di ruolo, CYBERPUNK_2020 ti permetterà di potenziare il tuo personaggio'
                  'a piacimento.\nLe abilità che puoi potenziare sono: Forza, Salute e Difesa.\n'
                  'Hai a disposizione 5 punti da utilizzare per potenziare queste tre abilità: \n')

            scelta_abilita()

            scelta_arma()

            chap1()
            chap2()
            chap3()
            chap4()
            chap5()

            break

        elif prova_scelta == 'N' or prova_scelta == 'n':
            time.sleep(2)
            print('Okay! Allora te lo ripeterò di nuovo. \n')

        if prova_scelta != 'N' or prova_scelta != 'n' or prova_scelta != 'S' or prova_scelta != 's':
            print('ERRORE! Carattere inesistente. Attendere... ')
            time.sleep(1)
            gioco()

def scelta_personaggio():

    print('Attendi...\n')
    time.sleep(3)
    print('Bene iniziamo a creare il tuo personaggio.\n')

    while True:
        global sex

        sesso = input('Vuoi essere un Maschio o una Femmina?\n'
                       'Digita Maschio oppure digita Femmina: \n')

        if sesso == 'Maschio' or sesso == 'maschio' or sesso == 'MASCHIO':
            domanda_sex = input('Sicuro di voler essere un Maschio? S/N: \n')
            if domanda_sex == 'S' or domanda_sex == 's':
                sex.append(sesso)
                print('Perfetto sei un Maschio.\n')
                break

            elif domanda_sex == 'N' or domanda_sex == 'n':
                scelta_personaggio()

        elif sesso == 'Femmina' or sesso == 'femmina' or sesso == 'FEMMINA':
            domanda_sex2 = input('Sicuro di voler essere una Femmina? S/N: \n')
            if domanda_sex2 == 'S' or domanda_sex2 == 's':
                sex.append(sesso)
                print('Perfetto sei una Femmina.\n')
                break

            elif domanda_sex2 == 'N' or domanda_sex2 == 'n':
                scelta_personaggio()

        if sesso != 'Maschio' or sesso != 'maschio' or sesso != 'MASCHIO'\
            or sesso != 'Femmina' or sesso != 'femmina' or sesso != 'FEMMINA':

            print('ERRORE! Digita Maschio o Femmina.\n')

    while True:
        global faz

        print('Inserisci la fazione che più ti rappresenta.\n')

        fazione = input('Vuoi essere: Umano o Cyborg?\n'
                       'Digita Umano oppure digita Cyborg: \n')

        if fazione == 'Umano' or fazione == 'umano' or fazione == 'UMANO':

            print('Creazione giocatore, attendere...\n')
            time.sleep(3)
            faz.append(fazione)
            print('Umano creato. \n')
            break

        elif fazione == 'Cyborg' or fazione == 'cyborg' or fazione == 'CYBORG':

            print('Creazione giocatore, attendere...\n')
            time.sleep(3)
            faz.append(fazione)
            print('Cyborg creato. \n')
            break

        if fazione != 'Umano' or fazione != 'umano' or fazione != 'UMANO'\
            or fazione != 'Cyborg' or fazione != 'cyborg' or fazione != 'CYBORG':
            print('ERRORE! Fazione non esistente.\n')


    while True:
        global name

        nome_player = input('Come vuoi chiamarti? \n')
        salva_nome = input('Bel nome. Vuoi salvarlo? S/N: \n')

        if salva_nome == 'S' or salva_nome == 's':
            name.append(nome_player)
            print('Benvenuto ' + str(nome_player) + '!\n')
            print ('La tua scheda giocatore è: ')
            print('SESSO:' + str(sex))
            print('FAZIONE: ' + str(faz))
            print('NOME: ' + str(name))
            break

        elif salva_nome == 'N' or salva_nome == 'n':
            print('Attendere prego...')
            time.sleep(1)

def scelta_abilita():
    scelta_abl = input('Quale abilità desideri potenziare?\n'
                       '[F] Per la Forza, [S] Per la Salute, [V] Per la Velocità: ')

    if scelta_abl == 'F' or scelta_abl == 'f':
        print('RICORDA! Inizieremo con tre [*] punti abilità gratis...')
        forza()

    elif scelta_abl == 'S' or scelta_abl == 's':
        print('RICORDA! Inizieremo con tre [*] punti abilità gratis...')
        salute()

    elif scelta_abl == 'V' or scelta_abl == 'v':
        print('RICORDA! Inizieremo con tre [*] punti abilità gratis...')
        difesa()

    if scelta_abl != 'F' or scelta_abl != 'f' \
            or scelta_abl != 'S' or scelta_abl != 's' \
            or scelta_abl != 'V' or scelta_abl != 'v':

        print('ERRORE! Carattere inesistente. Attendi...')
        time.sleep(1)
        scelta_abilita()


def forza():
    global accumulatore_punti_Forza
    global accumulatore_punti_Salute
    global accumulatore_punti_Difesa

    while True:
        punti_F = input('\nInserisci un numero da 1 a 5 per aggiungere [*]. '
                        'Quanti punti forza vuoi aggiungere?: ')

        if punti_F < '1':
            print('ERRORE! Valore non accettato! Attendere...')
            time.sleep(1)
            forza()
        elif punti_F > '5':
            print('ERRORE! Valore troppo grande Hai solo 5 punti abilità! Attendere...')
            time.sleep(1)
            forza()

        if punti_F == '5':
            scelta2 = input('Sei sicuro di voler dare 5 [*] alla Forza?\n'
                            'Non potrai usarli né per la Salute né la Difesa. S/N: ')

            if scelta2 == 'S' or scelta2 == 's':
                accumulatore_punti_Forza.append('*****')
                print('I punti Forza sono: ' + str(accumulatore_punti_Forza))
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza)\
                                                                          + str(accumulatore_punti_Salute)\
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta2 == 'N' or scelta2 == 'n':
                forza()

        elif punti_F == '4':
            accumulatore_punti_Forza.append('****')
            print('I punti Forza sono: ' + str(accumulatore_punti_Forza))

            scelta3 = input('Hai 4 [*] Forza. Ti rimane solo un punto abilità,\n'
                            'lo vuoi usare per la Salute o la Difesa? S/D: ')

            if scelta3 == 'S' or scelta3 == 's':
                accumulatore_punti_Salute.append('*')
                print('I punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('I punti Difesa sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta3 == 'D' or scelta3 == 'd':
                accumulatore_punti_Difesa.append('*')
                print('I punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('I punti Salute sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

        elif punti_F == '3':
            accumulatore_punti_Forza.append('***')
            print('I punti Forza sono: ' + str(accumulatore_punti_Forza))

            scelta4 = input('Hai 3 [*] Forza. Ti rimangono solo due punti abilità,\n'
                            'li vuoi usare per la Salute, per la Difesa oppure \n'
                            'vuoi usare un punto per la Salute e uno per la Difesa? S/D/SD: ')

            if scelta4 == 'S' or scelta4 == 's':
                accumulatore_punti_Salute.append('**')
                print('I punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('I punti Difesa sono: 0 ')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta4 == 'D' or scelta4 == 'd':
                accumulatore_punti_Difesa.append('**')
                print('I punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('I punti Salute sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta4 == 'SD' or scelta4 == 'sd':
                accumulatore_punti_Salute.append('*')
                print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                accumulatore_punti_Difesa.append('*')
                print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

        elif punti_F == '2':
            accumulatore_punti_Forza.append('**')
            print('I punti Forza sono: ' + str(accumulatore_punti_Forza))

            scelta5 = input('Hai 2 [*] Forza. Ti rimangono solo tre punti abilità,\n'
                            'li vuoi usare per la Salute, per la Difesa oppure \n'
                            'li vuoi dividere tra la Salute e la Difesa? S/D/SD: ')

            if scelta5 == 'S' or scelta5 == 's':
                accumulatore_punti_Salute.append('***')
                print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('I tuoi punti Difesa sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta5 == 'D' or scelta5 == 'd':
                accumulatore_punti_Difesa.append('***')
                print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('I tuoi punti Salute sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta5 == 'SD' or scelta5 == 'sd':
                scelta6 = input('Come vuoi spartire i tuoi tre punti?\n '
                                'Vuoi aggiungere 2[*] alla Salute e 1 [*] alla Difesa?\n'
                                'Oppure vuoi aggiungere 2[*] alla Difesa e 1[*] alla Salute?\n'
                                'Digita DD per dare 2[*] alla Difesa e 1[*] alla Salute\n'
                                'Oppure digita SS per dare 2[*] alla Salute e 1[*] alla Difesa: ')

                if scelta6 == 'DD' or scelta6 == 'dd':
                    accumulatore_punti_Difesa.append('**')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    accumulatore_punti_Salute.append('*')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

                elif scelta6 == 'SS' or scelta6 == 'ss':
                    accumulatore_punti_Salute.append('**')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    accumulatore_punti_Difesa.append('*')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()
                

        elif punti_F == '1':
            accumulatore_punti_Forza.append('*')
            print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))

            scelta7 = input('Hai 1 [*] Forza. Ti rimangono solo 4 punti abilità,\n'
                            'li vuoi usare per la Salute, per la Difesa oppure \n'
                            'li vuoi dividere tra la Salute e la Difesa? S/D/SD: ')

            if scelta7 == 'S' or scelta7 == 's':
                accumulatore_punti_Salute.append('****')
                print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('I tuoi punti Difesa sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta7 == 'D' or scelta7 == 'd':
                accumulatore_punti_Difesa.append('****')
                print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('I tuoi punti Salute sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

            elif scelta7 == 'SD' or scelta7 == 'sd':
                scelta8 = input('Come vuoi spartire i tuoi quattro punti?\n '
                                'Vuoi aggiungere 2[*] alla Salute e 2 [*] alla Difesa?\n'
                                'Oppure vuoi aggiungere 3[*] alla Difesa e 1[*] alla Salute?\n'
                                'Oppure vuoi aggiungere 3[*] alla Salute e 1[*] alla Difesa?\n'
                                'Oppure vuoi aggiungere 2[*] alla Salute e 2[*] alla Difesa?\n'
                                'Digita DD per dare 3[*] alla Difesa e 1[*] alla Salute\n'
                                'Oppure digita SS per dare 3[*] alla Salute e 1[*] alla Difesa\n'
                                'Oppure digita DDSS per dare 2[*] alla Difesa e 2[*] alla Salute: ')

                if scelta8 == 'DD' or scelta8 == 'dd':
                    accumulatore_punti_Difesa.append('***')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    accumulatore_punti_Salute.append('*')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

                elif scelta8 == 'SS' or scelta8 == 'ss':
                    accumulatore_punti_Salute.append('***')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    accumulatore_punti_Difesa.append('*')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

                elif scelta8 == 'SSDD' or scelta8 == 'ssdd':
                    accumulatore_punti_Salute.append('**')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    accumulatore_punti_Difesa.append('**')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()
        break     

def salute():
    global accumulatore_punti_Forza
    global accumulatore_punti_Salute
    global accumulatore_punti_Difesa

    while True:
        punti_S = input('\nInserisci un numero da 1 a 5 per aggiungere [*]. '
                        'Quanti punti Salute vuoi aggiungere?: ')

        if punti_S < '1':
            print('ERRORE! Valore non accettato! Attendere...')
            time.sleep(1)
            salute()

        elif punti_S > '5':
            print('ERRORE! Valore troppo grande Hai solo 5 punti abilità! Attendere...')
            time.sleep(1)
            salute()

        if punti_S == '5':
            scelta2 = input('Sei sicuro di voler dare 5 [*] alla Salute?\n'
                            'Non potrai usarli né per la Forza né la Difesa. S/N: ')

            if scelta2 == 'S' or scelta2 == 's':
                accumulatore_punti_Salute.append('*****')
                print('I punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()
                

            elif scelta2 == 'N' or scelta2 == 'n':
                salute()

        elif punti_S == '4':
            accumulatore_punti_Salute.append('****')
            print('I punti Salute sono: ' + str(accumulatore_punti_Salute))

            scelta3 = input('Hai 4 [*] Salute. Ti rimane solo un punto abilità,\n'
                            'lo vuoi usare per la Forza o la Difesa? F/D: ')

            if scelta3 == 'F' or scelta3 == 'f':
                accumulatore_punti_Forza.append('*')
                print('I punti Forza sono: ' + str(accumulatore_punti_Forza))
                print('I punti Difesa sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta3 == 'D' or scelta3 == 'd':
                accumulatore_punti_Difesa.append('*')
                print('I punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('I punti Forza sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

        elif punti_S == '3':
            accumulatore_punti_Salute.append('***')
            print('I punti Salute sono: ' + str(accumulatore_punti_Salute))

            scelta4 = input('Hai 3 [*] Salute. Ti rimangono solo due punti abilità,\n'
                            'li vuoi usare per la Forza, per la Difesa oppure \n'
                            'vuoi usare un punto per la Forza e uno per la Difesa? F/D/FD: ')

            if scelta4 == 'F' or scelta4 == 'f':
                accumulatore_punti_Forza.append('**')
                print('I punti Forza sono: ' + str(accumulatore_punti_Forza))
                print('I punti Difesa sono: 0 ')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta4 == 'D' or scelta4 == 'd':
                accumulatore_punti_Difesa.append('**')
                print('I punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('I punti Forza sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta4 == 'FD' or scelta4 == 'fd':
                accumulatore_punti_Forza.append('*')
                print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                accumulatore_punti_Difesa.append('*')
                print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

        elif punti_S == '2':
            accumulatore_punti_Salute.append('**')
            print('I punti Salute sono: ' + str(accumulatore_punti_Salute))

            scelta5 = input('Hai 2 [*] Salute. Ti rimangono solo tre punti abilità,\n'
                            'li vuoi usare per la Forza, per la Difesa oppure \n'
                            'li vuoi dividere tra la Forza e la Difesa? F/D/FD: ')

            if scelta5 == 'F' or scelta5 == 'f':
                accumulatore_punti_Forza.append('***')
                print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                print('I tuoi punti Difesa sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta5 == 'D' or scelta5 == 'd':
                accumulatore_punti_Difesa.append('***')
                print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('I tuoi punti Forza sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta5 == 'FD' or scelta5 == 'fd':
                scelta6 = input('Come vuoi spartire i tuoi tre punti?\n '
                                'Vuoi aggiungere 2[*] alla Forza e 1 [*] alla Difesa?\n'
                                'Oppure vuoi aggiungere 2[*] alla Difesa e 1[*] alla Forza?\n'
                                'Digita DD per dare 2[*] alla Difesa e 1[*] alla Forza\n'
                                'Oppure digita FF per dare 2[*] alla Forza e 1[*] alla Difesa: ')

                if scelta6 == 'DD' or scelta6 == 'dd':
                    accumulatore_punti_Difesa.append('**')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    accumulatore_punti_Forza.append('*')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

                elif scelta6 == 'FF' or scelta6 == 'ff':
                    accumulatore_punti_Forza.append('**')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    accumulatore_punti_Difesa.append('*')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

        elif punti_S == '1':
            accumulatore_punti_Salute.append('*')
            print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))

            scelta7 = input('Hai 1 [*] Salute. Ti rimangono solo 4 punti abilità,\n'
                            'li vuoi usare per la Forza, per la Difesa oppure \n'
                            'li vuoi dividere tra la Forza e la Difesa? F/D/FD: ')

            if scelta7 == 'F' or scelta7 == 'f':
                accumulatore_punti_Forza.append('****')
                print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                print('I tuoi punti Difesa sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta7 == 'D' or scelta7 == 'd':
                accumulatore_punti_Difesa.append('****')
                print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('I tuoi punti Forza sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

            elif scelta7 == 'FD' or scelta7 == 'fd':
                scelta8 = input('Come vuoi spartire i tuoi quattro punti?\n '
                                'Vuoi aggiungere 2[*] alla Forza e 2 [*] alla Difesa?\n'
                                'Oppure vuoi aggiungere 3[*] alla Difesa e 1[*] alla Forza?\n'
                                'Oppure vuoi aggiungere 3[*] alla Forza e 1[*] alla Difesa?\n'
                                'Oppure vuoi aggiungere 2[*] alla Forza e 2[*] alla Difesa?\n'
                                'Digita DD per dare 3[*] alla Difesa e 1[*] alla Forza\n'
                                'Oppure digita FF per dare 3[*] alla Forza e 1[*] alla Difesa\n'
                                'Oppure digita FFDD per dare 2[*] alla Difesa e 2[*] alla Forza: ')

                if scelta8 == 'DD' or scelta8 == 'dd':
                    accumulatore_punti_Difesa.append('***')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    accumulatore_punti_Forza.append('*')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

                elif scelta8 == 'FF' or scelta8 == 'ff':
                    accumulatore_punti_Forza.append('***')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    accumulatore_punti_Difesa.append('*')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

                elif scelta8 == 'FFDD' or scelta8 == 'ffdd':
                    accumulatore_punti_Forza.append('**')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    accumulatore_punti_Difesa.append('**')
                    print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()


def difesa():
    global accumulatore_punti_Forza
    global accumulatore_punti_Salute
    global accumulatore_punti_Difesa

    while True:
        punti_D = input('\nInserisci un numero da 1 a 5 per aggiungere [*]. '
                        'Quanti punti Difesa vuoi aggiungere?: ')

        if punti_D < '1':
            print('ERRORE! Valore non accettato! Attendere...')
            time.sleep(1)
            difesa()
        elif punti_D > '5':
            print('ERRORE! Valore troppo grande Hai solo 5 punti abilità! Attendere...')
            time.sleep(1)
            difesa()

        if punti_D == '5':
            scelta2 = input('Sei sicuro di voler dare 5 [*] alla Difesa?\n'
                            'Non potrai usarli né per la Forza né la Salute. S/N: ')

            if scelta2 == 'S' or scelta2 == 's':
                accumulatore_punti_Difesa.append('*****')
                print('I punti Difesa sono: ' + str(accumulatore_punti_Difesa))
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta2 == 'N' or scelta2 == 'n':
                difesa()

        elif punti_D == '4':
            accumulatore_punti_Salute.append('****')
            print('I punti Difesa sono: ' + str(accumulatore_punti_Difesa))

            scelta3 = input('Hai 4 [*] Difesa. Ti rimane solo un punto abilità,\n'
                            'lo vuoi usare per la Forza o la Salute? F/S: ')

            if scelta3 == 'F' or scelta3 == 'f':
                accumulatore_punti_Forza.append('*')
                print('I punti Forza sono: ' + str(accumulatore_punti_Forza))
                print('I punti Salute sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta3 == 'S' or scelta3 == 's':
                accumulatore_punti_Salute.append('*')
                print('I punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('I punti Forza sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

        elif punti_D == '3':
            accumulatore_punti_Difesa.append('***')
            print('I punti Difesa sono: ' + str(accumulatore_punti_Difesa))

            scelta4 = input('Hai 3 [*] Difesa. Ti rimangono solo due punti abilità,\n'
                            'li vuoi usare per la Forza, per la Salute oppure \n'
                            'vuoi usare un punto per la Forza e uno per la Salute? F/S/FS: ')

            if scelta4 == 'F' or scelta4 == 'f':
                accumulatore_punti_Forza.append('**')
                print('I punti Forza sono: ' + str(accumulatore_punti_Forza))
                print('I punti Salute sono: 0 ')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta4 == 'S' or scelta4 == 's':
                accumulatore_punti_Salute.append('**')
                print('I punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('I punti Forza sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta4 == 'FS' or scelta4 == 'fs':
                accumulatore_punti_Forza.append('*')
                print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                accumulatore_punti_Salute.append('*')
                print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

        elif punti_D == '2':
            accumulatore_punti_Difesa.append('**')
            print('I punti Difesa sono: ' + str(accumulatore_punti_Difesa))

            scelta5 = input('Hai 2 [*] Difesa. Ti rimangono solo tre punti abilità,\n'
                            'li vuoi usare per la Forza, per la Salute oppure \n'
                            'li vuoi dividere tra la Forza e la Salute? F/S/FS: ')

            if scelta5 == 'F' or scelta5 == 'f':
                accumulatore_punti_Forza.append('***')
                print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                print('I tuoi punti Salute sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta5 == 'S' or scelta5 == 's':
                accumulatore_punti_Salute.append('***')
                print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('I tuoi punti Forza sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta5 == 'FS' or scelta5 == 'fs':
                scelta6 = input('Come vuoi spartire i tuoi tre punti?\n '
                                'Vuoi aggiungere 2[*] alla Forza e 1 [*] alla Salute?\n'
                                'Oppure vuoi aggiungere 2[*] alla Salute e 1[*] alla Forza?\n'
                                'Digita SS per dare 2[*] alla Salute e 1[*] alla Forza\n'
                                'Oppure digita FF per dare 2[*] alla Forza e 1[*] alla Salute: ')

                if scelta6 == 'SS' or scelta6 == 'ss':
                    accumulatore_punti_Salute.append('**')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    accumulatore_punti_Forza.append('*')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

                elif scelta6 == 'FF' or scelta6 == 'ff':
                    accumulatore_punti_Forza.append('**')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    accumulatore_punti_Salute.append('*')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

        elif punti_D == '1':
            accumulatore_punti_Difesa.append('*')
            print('I tuoi punti Difesa sono: ' + str(accumulatore_punti_Difesa))

            scelta7 = input('Hai 1 [*] Difesa. Ti rimangono solo 4 punti abilità,\n'
                            'li vuoi usare per la Forza, per la Salute oppure \n'
                            'li vuoi dividere tra la Forza e la Salute? F/S/FS: ')

            if scelta7 == 'F' or scelta7 == 'f':
                accumulatore_punti_Forza.append('****')
                print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                print('I tuoi punti Salute sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

                scelta_arma()

            elif scelta7 == 'S' or scelta7 == 's':
                accumulatore_punti_Salute.append('****')
                print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                print('I tuoi punti Forza sono: 0')
                print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                          + str(accumulatore_punti_Salute) \
                                                                          + str(accumulatore_punti_Difesa))

            elif scelta7 == 'FS' or scelta7 == 'fs':
                scelta8 = input('Come vuoi spartire i tuoi quattro punti?\n '
                                'Vuoi aggiungere 2[*] alla Forza e 2 [*] alla Salute?\n'
                                'Oppure vuoi aggiungere 3[*] alla Salute e 1[*] alla Forza?\n'
                                'Oppure vuoi aggiungere 3[*] alla Forza e 1[*] alla Salute?\n'
                                'Oppure vuoi aggiungere 2[*] alla Forza e 2[*] alla Salute?\n'
                                'Digita SS per dare 3[*] alla Salute e 1[*] alla Forza\n'
                                'Oppure digita FF per dare 3[*] alla Forza e 1[*] alla Salute\n'
                                'Oppure digita FFSS per dare 2[*] alla Forza e 2[*] alla Salute: ')

                if scelta8 == 'SS' or scelta8 == 'ss':
                    accumulatore_punti_Salute.append('***')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    accumulatore_punti_Forza.append('*')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

                elif scelta8 == 'FF' or scelta8 == 'ff':
                    accumulatore_punti_Forza.append('***')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    accumulatore_punti_Salute.append('*')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

                elif scelta8 == 'FFSS' or scelta8 == 'ffss':
                    accumulatore_punti_Forza.append('**')
                    print('I tuoi punti Forza sono: ' + str(accumulatore_punti_Forza))
                    accumulatore_punti_Salute.append('**')
                    print('I tuoi punti Salute sono: ' + str(accumulatore_punti_Salute))
                    print('La tua cronologia delle abilità è la seguente: \n' + str(accumulatore_punti_Forza) \
                                                                              + str(accumulatore_punti_Salute) \
                                                                              + str(accumulatore_punti_Difesa))

                    scelta_arma()

def scelta_arma():

    while True:
        chose_w = input('Vuoi prendere la pistola o il manganello celato?')
        if chose_w == 'Pistola' or chose_w == 'pistola' or chose_w == 'PISTOLA':
            inventario.append(chose_w)
            print('È stata aggiunta una nuova arma: ', inventario)
            chap1()
            
        elif chose_w == 'Manganello' or chose_w == 'manganello' or chose_w == 'MANGANELLO':
            print('È stata aggiunta una nuova arma: ', inventario)
            chap1()

def chap1():
    print('''
                        _              .|
                       | |              |
                       |'|            ._|___
               ___    |  |            |.   |' .---"|
       _    .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~NIGHTCITY~~~~~~~~~~~~~~~~~~~~~~~~


    ''')

    print('Benvenuto a Night City, città frenetica e piena di oppurtintà.\n'
          'Prima nella storia con un alto tasso di tecnologia e Cyborg sintetici.')

    while True:
        scelta_percorso = input('Ti trovi in una strada. Oh no! Ti sei perso! Cosa decidi di fare?: \n'
                   '\n1) Entri dentro un Bar là vicino.'
                   '\n2) Entri dentro un vicolo per controllare il GPS.'
                   '\n3) Cammini lungo la strada. Tanto prima o poi andrai da qualche parte, no?!'
                   '\n4) Chiedi informazioni.')

        if scelta_percorso == '1':
            print('Stai entrando dentro un bar.')
            time.sleep(1)
            print('Vedi intorno a te tantissima gente. Dai più loschi fino ai più normali.\n'
                  'Ti avvicini al barista e chiedi un drink.')
            sceltaDrink = input("Quale drink scegli? ")
        
        if scelta_percorso == '2':
            print('Sei entrato dentro un vicolo,\n'
                  'il GPS ti segnala la posizione di un Bar là vicino.')
            
        

def chap2():
    pass

def chap3():
    pass

def chap4():
    pass

def chap5():
    pass

def end():
    print('Complimenti hai finito il gioco!!! Ora cosa vuoi fare?')

def randomize_png():
    global png

    print(random.choice(png))
    scelto = png_scelto.append(png)
    pass

titolo()
menu()
